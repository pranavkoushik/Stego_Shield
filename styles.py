import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        .stApp {
            max-width: 800px;
            margin: 0 auto;
        }
        
        .stTitle {
            color: #2c3e50;
            text-align: center;
            padding-bottom: 20px;
        }
        
        .stSubheader {
            color: #34495e;
            padding-bottom: 10px;
        }
        
        .stButton button {
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
        }
        
        .stButton button:hover {
            background-color: #2980b9;
        }
        
        .stTextArea textarea {
            border-radius: 5px;
            border: 1px solid #bdc3c7;
        }
        
        .stFileUploader {
            border: 2px dashed #bdc3c7;
            border-radius: 5px;
            padding: 10px;
        }
        
        .success {
            color: #27ae60;
            font-weight: bold;
        }
        
        .error {
            color: #c0392b;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)
