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

        account_sid = "US6c9f35daf413c673ca25a504782c9882"
        auth_token = "91498089ae6a7732b9f0ae1a31407a89"

        client = Client(account_sid, auth_token)

        client.messages.create(
            body="⚠ Unsafe condition detected!",
            from_="+14155238886",
            to="+919326182564"
        )

    except:
        print("SMS not configured")
