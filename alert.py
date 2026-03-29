from twilio.rest import Client
import time
from config import *

last_alert_time = 0
COOLDOWN = 10  # seconds

def send_sms(message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(
        body=message,
        from_=TWILIO_NUMBER,
        to=TARGET_NUMBER
    )

def trigger_alert(is_unsafe):
    global last_alert_time

    if not is_unsafe:
        return

    current_time = time.time()

    if current_time - last_alert_time > COOLDOWN:
        print("🚨 ALERT SENT")
        send_sms("Unsafe posture detected!")
        last_alert_time = current_time