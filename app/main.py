#import standard required libraries
import streamlit as st
import urllib
import os
import time
import requests
import random
from collections import OrderedDict
from openai.error import OpenAIError

#import local libraries from utils.py
from utils import (
    get_answer
)

#import secret azure keys values from credentials.py
from credentials import (

    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_KEY,
    AZURE_OPENAI_API_VERSION

)

#load azure key values to local environment variables
os.environ["OPENAI_API_BASE"] = os.environ["AZURE_OPENAI_ENDPOINT"] = st.session_state["AZURE_OPENAI_ENDPOINT "] = AZURE_OPENAI_ENDPOINT
os.environ["OPENAI_API_KEY"] = os.environ["AZURE_OPENAI_API_KEY"] = st.session_state["AZURE_OPENAI_API_KEY"] = AZURE_OPENAI_KEY
os.environ["OPENAI_API_VERSION"] = os.environ["AZURE_OPENAI_API_VERSION"] = AZURE_OPENAI_API_VERSION


def clear_submit():
    st.session_state["submit"] = False

#design the webpage with title, header, instructions
st.set_page_config(page_title="GPT Smart Code Generation", page_icon="📖", layout="wide")
st.header("GPT Smart Code Generation")

with st.expander("Instructions"):
    st.markdown("""
                Enter instructions clearly and precisely, and as of now GPT is restricted to python and SQL language.
                """)


prompt_text = st.text_input("Enter the prompt:", value= """ Write a Python function that accepts first name, second name, 
and birth date in string format as a parameter values
and returns the full name, and the number of days from the birth date to today """
, on_change=clear_submit)

col1, col2 = st.columns([2,3])
with col1:
    generate = st.button('Generate Code')
with col2:
    temp = st.slider('Temperature :thermometer:', min_value=0.0, max_value=1.0, step=0.1, value=0.5)

if generate or st.session_state.get("submit"):
    if not prompt_text:
        st.error("Please enter a question!")
    else:
        st.session_state["submit"] = True
        # Output Columns
        placeholder = st.empty()
        
        try:
            answer = get_answer(prompt_text, engine="gpt-35-turbo", temperature=temp, max_tokens=150)
            
            with placeholder.container():
                st.markdown("#### Answer")
                try: 
                    for choice in answer['choices']:
                        st.markdown(choice['text']) 
                except:
                    st.markdown("N/A")
                    st.markdown("---")
                    st.markdown("#### Search Results")

        except OpenAIError as e:
            st.error(e._message)
            st.error(e._status_code)
