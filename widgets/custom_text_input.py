import streamlit as st

def show_normal_text_input(title_label, placeholder_label):
    return st.text_input(label=title_label, placeholder=placeholder_label)