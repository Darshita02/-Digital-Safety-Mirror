import streamlit as st


def show_alert(message):
    st.error(message)


def show_warning(message):
    st.warning(message)


def show_success(message):
    st.success(message)