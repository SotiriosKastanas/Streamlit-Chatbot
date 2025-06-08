import streamlit as st
import sys
from utils import add_css, add_top_right_info, sidebar, set_background
import datetime
from openai import AzureOpenAI
sys.path.append("../src")
from core.qa import get_response
from core.utils import load_config

config = load_config()
azure_config = config["azure"]
paths_config = config["paths"]

client = AzureOpenAI(
    api_key=azure_config["api_key"],
    azure_endpoint=azure_config["endpoint"],
    api_version=azure_config["api_version"]
)
QA_model = azure_config["model"]

st.session_state['user_avatar'] = paths_config["user_avatar"]
st.session_state['assistant_avatar'] = paths_config["assistant_avatar"]
st.set_page_config(page_title='Chatbot', page_icon=paths_config["page_icon"])

####################################################################
if 'is_input_disabled' not in st.session_state:
    st.session_state.is_input_disabled = False

###################### STREAMLIT INTERFACE ######################

def main_interface():
    st.title('Streamlit Chatbot')
    st.markdown(
        """
        <p style="font-size: 24px; margin: 0;">
            Welcome to the <span style="color: blue; font-weight: bold;"> Streamlit Chatbot </span> interface
        </p>
        """,
        unsafe_allow_html=True,
    )

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    for entry in st.session_state.chat_history:
        if entry['role'] == 'user':
            with st.chat_message('user', avatar=st.session_state['user_avatar']):
                st.markdown(entry['content'])
                st.caption(f"{entry['timestamp']}")
        elif entry['role'] == 'assistant':
            with st.chat_message('assistant', avatar = st.session_state['assistant_avatar']):
                st.markdown(entry['content'])
                st.caption(f"{entry['timestamp']}") 
    user_input = st.chat_input("Type your message here...", disabled=st.session_state.is_input_disabled)

    if (user_input):
        st.session_state.is_input_disabled = True
        question_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state['user_input'] = user_input
        st.session_state['question_timestamp'] = question_timestamp
        st.session_state.chat_history.append({"role": "user", "content": user_input, 'timestamp': question_timestamp})
        st.rerun()


###################### USER MESSAGE ######################
def user_message(user_input):
    if 'user_input' in st.session_state:

        messages = st.session_state.chat_history
        question_timestamp = st.session_state.question_timestamp
        try:
            with st.spinner('loading...'):
                response = get_response(client, messages, 'gpt-4o')
                answer_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.session_state.chat_history.append({"role": "assistant", "content": response, 'timestamp': answer_timestamp})
                process_response(response)
        except Exception:
            error_message = (
                "An error occured"
            )
            with st.chat_message('assistant', avatar = st.session_state['assistant_avatar']):
                st.markdown(error_message)
            st.session_state.chat_history.append({'role': 'assistant', 'content': error_message})
            process_response(user_input, error_message, question_timestamp, answer_timestamp)
            del st.session_state['user_input']


def process_response(response):
    response = response.replace('\n', ' ')
    del st.session_state['user_input']
    st.session_state.is_input_disabled = False
    st.rerun()


def main():
    if "chat_history" not in st.session_state or not st.session_state.chat_history:
        st.session_state.chat_history = []
    main_interface()
    if 'user_input' in st.session_state:
        user_message(st.session_state['user_input'])


if __name__ == '__main__':
    if "email_entered" not in st.session_state:
        st.session_state["email_entered"] = False
    if not st.session_state.email_entered:
        email = st.text_input("Username:")
        if email:
            st.session_state.email = email
            st.session_state.email_entered = True
            st.rerun()
    else:
        email = st.session_state.email
        add_css()
        set_background(paths_config["background_image"])
        add_top_right_info(email)
        # sidebar()
        main()
