import streamlit as st
import base64

def sidebar():
    with st.sidebar:
        st.write('**Welcome to the Streamlit Chatbot**')

def add_top_right_info(email):
    st.markdown(f"""
    <style>
    header[data-testid="stHeader"]::after {{
        content: "User: {email}";
        /* Line breaks for \\A */
        white-space: pre-line;
        
        position: absolute;
        right: 2rem;
        top: 10px;
        
        /* Styling */
        font-size: 14px;
        font-weight: bold;
        color: white;
        background: #2E3B4E;
        padding: 10px 15px;
        border-radius: 12px;
    }}
    </style>
    """, unsafe_allow_html=True)

def add_css():
    st.markdown(
        """
        <style>
        div[data-testid="stToolbar"] {display: none;}
        </style>
        """, unsafe_allow_html=True
    )

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(image_path):
    encoded_image = get_base64(image_path)
    st.markdown(f"""
    <style>
    html, body, .stApp {{
        height: 100vh !important;
        width: 100vw !important;
        margin: 0;
        padding: 0;
        overflow: hidden !important;
        background: url("data:image/png;base64,{encoded_image}") no-repeat center center fixed !important;
        background-size: cover !important;
        background-attachment: fixed !important;
        background-color: transparent !important;
    }}

    div[data-testid="stMainBlockContainer"] {{
        flex: 1 1 auto;
        overflow-y: auto;
        padding-bottom: 140px;
        background-color: transparent !important;
    }}

    /* ✅ White box override */
    div.st-emotion-cache-128upt6 {{
        background-color: transparent !important;
    }}

    div.st-emotion-cache-a4s44t {{
        background-color: transparent !important;
    }}

    header[data-testid="stHeader"] {{
        background-color: transparent !important;
    }}
    </style>
    """, unsafe_allow_html=True)

