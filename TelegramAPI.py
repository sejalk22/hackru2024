import time
from datetime import datetime, timedelta
from telegram import Bot

# Replace 'YOUR_BOT_TOKEN' with your bot's token
bot_token = 'YOUR_BOT_TOKEN'
bot = Bot(token=bot_token)

# Function to send a message to the user
def send_message(chat_id, message):
    bot.send_message(chat_id=chat_id, text=message)

# Function to check the bus schedule and send a reminder 2 minutes before leaving
def check_bus_schedule_and_remind(chat_id):
    # Assume you have a function to get the time until the next bus
    time_until_next_bus = timedelta(minutes=2)  # Replace this with actual time until the next bus

    # Schedule the reminder
    reminder_time = datetime.now() + time_until_next_bus
    message = f"You have to leave to catch the bus in 2 minutes!"
    send_message(chat_id, message)

# Replace 'YOUR_CHAT_ID' with your chat ID
chat_id = 'YOUR_CHAT_ID'

# Main loop
while True:
    # Check the bus schedule and send a reminder if necessary
    check_bus_schedule_and_remind(chat_id)
    
    # Wait for some time before checking again (e.g., 1 minute)
    time.sleep(60)
x 