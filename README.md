# Streamlit Chatbot UI

A general-purpose, adaptable chatbot interface built using [Streamlit](https://streamlit.io/).  
This project enables fast and modular UI for chatbot systems, with a clear separation between UI and logic.
The interface is fully adaptable — you can plug in your own logic by modifying just the `qa.py` file in `core/`. No changes are required in the Streamlit UI code.

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/SotiriosKastanas/Streamlit-Chatbot

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # On Windows
   
3. **Install dependencies**
   ```bash
   cd Streamlit-Chatbot
   pip install -r requirements.txt

4. **Update config.yaml**
   ```bash
   Add your API keys and any necessary configuration values.
   
5. **Run the app**
   ```bash
   cd src
   streamlit run src/application/app.py

## Video Demo

https://github.com/user-attachments/assets/05ce7ae7-1dac-45ea-9968-056ce5c5adff

