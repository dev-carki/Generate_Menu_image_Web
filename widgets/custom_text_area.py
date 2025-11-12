import streamlit as st

def show_normal_text_area(title_label, placeholder_label):
    return st.text_area(label=title_label, placeholder=placeholder_label)