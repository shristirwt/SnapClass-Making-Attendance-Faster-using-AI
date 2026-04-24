import streamlit as st

def style_background_home():
    st.markdown("""
            <style>
                .stApp {
                    background: #5865F2 !important
                }
                
                .stApp div[data-testid='stColumn'] {
                    background-color: #E0E3FF !important;
                    padding: 1.5rem !important;
                    border-radius: 5rem !important;
                }
            </style>
""", unsafe_allow_html=True)
    
def style_background_dashboard():
    st.markdown("""
            <style>
                .stApp {
                    background: #E0E3FF !important
                }
            </style>
""", unsafe_allow_html=True)
    
def style_base_layout():
    st.markdown("""
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
                
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');
                
                
                /* Hide Top Toolbar of streamlit */
                
                #MainMenu, footer, header {
                    visibility: hidden;
                }
                
                .block-container {
                    padding-top: 1.5rem !important;
                }
                
                h1 {
                    font-family:'Climate Crisis', sans-serif !important;
                    font-size: 3.5 rem !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0rem !important;
                }
                
                h2 {
                    font-family:'Climate Crisis', sans-serif !important;
                    font-size: 2 rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem !important;
                    color: black !important;
                }
                
                h2.dashboard-title {
                    color: #5865F2 !important;
                }
                
                h3, h4, p {
                    font-family: 'Outfit', sans-serif;
                }
                
                h2, h3, h4 {
                    color: black !important;
                }


                [data-testid="stHeader"] h2 {
                    color: black !important;
                }
                
                
                input, textarea, [data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea {
                    background-color: white !important;
                    color: black !important;
                    caret-color: black !important;
                }
                
                
                label, [data-testid="stLabel"] {
                    color: black !important;
                }
                
                input::placeholder, textarea::placeholder, [data-testid="stTextInput"] input::placeholder, [data-testid="stTextArea"] textarea::placeholder {
                color: #999999 !important;
                opacity: 1 !important;
            }
                
                button {
                    background-color: #5865F2 !important;
                    border-radius: 1.5rem !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                
                button[kind='secondary'] {
                    background-color: #EB459E !important;
                    border-radius: 1.5rem !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                
                button[kind='tertiary'] {
                    background-color: black !important;
                    border-radius: 1.5rem !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                
                button:hover {
                    transform: scale(1.05)
                }
            </style>
""", unsafe_allow_html=True)