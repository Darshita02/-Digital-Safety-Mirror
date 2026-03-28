import streamlit as st
import os

def show_alert(message):
    st.error(message)

def show_warning(message):
    st.warning(message)

def show_success(message):
    st.success(message)

def play_sound():
    os.system("echo \a")


# OPTIONAL SMS ALERT
def send_sms_alert():
    try:
        from twilio.rest import Client

        account_sid = "your_sid"
        auth_token = "your_auth_token"

        client = Client(account_sid, auth_token)

        client.messages.create(
            body="⚠ Unsafe condition detected!",
            from_="+1234567890",
            to="+91XXXXXXXXXX"
        )

    except:
        print("SMS not configured")