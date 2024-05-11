import telebot
import random
import requests
from telebot import types
from user_agent import generate_user_agent as ua
import time

# Initialize the bot with your token
bot = telebot.TeleBot("7031783178:AAFQKJuH6yGKT77BNrkm-tO_ojRxdGf-fDI")

# Dictionary to store the last time each user executed a command
user_last_command_time = {}

# Function to rotate proxies
def get_proxy(proxy_type):
    with open(f"{proxy_type}_proxies.txt", 'r') as file:
        proxies = file.readlines()
    return random.choice(proxies).strip()

# Custom report messages
custom_messages = [
    "This user is engaging in suspicious activities. Please investigate.",
    "I suspect this user of being involved in scams. Kindly take appropriate action.",
    "Reporting this user for suspicious behavior. Please review.",
    "I believe this user may be engaging in phishing attempts. Please look into it.",
    "Flagging this user for potential scam activity. Please take action."
]

# Command to report a scammer
@bot.message_handler(commands=['massreport'])
def mass_report_scammer(message):
    # Get the user's ID
    user_id = message.from_user.id

    # Check if the user has executed the command recently
    if user_id in user_last_command_time and time.time() - user_last_command_time[user_id] < 60:  # Limiting to one request per minute
        bot.reply_to(message, "You are sending reports too quickly. Please wait for a minute before sending another report.")
        return

    # Update the last command time for the user
    user_last_command_time[user_id] = time.time()

    # Get the username to report
    scammer_username = message.text.split()[1]

    # Define the number of reports to send
    num_reports = 100

    # Generate random email and phone number for each report
    names = ["raof", "fazel", "aymen", "abdulmalek", "mohammed", "Naseer", "Whis", "REEKY.", "spamkiller",
             "des.175", "deveing", "meraff", "viratkohli", "spammers", "hackers", "pleesa", "3nefa_iraq",
             "pagesouls", "erycka", "jessy", "lola", "mentezer", "frhon", "HackerAbdulah", "jasim", "karrar",
             "radwan", "haider", "zainab", "ahmed", "youssef"]

    start_time = time.time()
    progress_message = bot.send_message(message.chat.id, f"Sending reports for {scammer_username}... 0/{num_reports}")
    for i in range(num_reports):
        num = f"+91{random.randint(9392823620, 9994997058)}"
        email = f"{random.choice(names)}{random.randint(9392820, 9994958)}@gmail.com"

        # Select a random custom message
        message_text = random.choice(custom_messages)

        # Send the report with rotating proxies
        proxy_type = random.choice(['http', 'socks4', 'socks5'])
        proxy = get_proxy(proxy_type)
        res = requests.get('https://telegram.org/support', proxies={proxy_type: proxy}, headers={
            "Host": "telegram.org",
            "cache-control": "max-age=0",
            "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "upgrade-insecure-requests": "1",
            "user-agent": ua(),
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "referer": "https://www.google.com/",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7"
        }).cookies
        stel = res['stel_ssid']
        data = f'message={message_text}&email={email}&phone={num}&setln='
        req = requests.post('https://telegram.org/support', data=data, proxies={proxy_type: proxy}, headers={
            "Host": "telegram.org",
            "cache-control": "max-age=0",
            "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "upgrade-insecure-requests": "1",
            "origin": "https://telegram.org",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": ua(),
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "referer": "https://telegram.org/support",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7",
            "cookie": f"stel_ssid={stel}"
        }).text

        # Check if the report was successful
        if "Thanks" in req:
            bot.edit_message_text(chat_id=message.chat.id, message_id=progress_message.id, text=f"Sending reports for {scammer_username}... {i+1}/{num_reports}")
        else:
            bot.reply_to(message, f"Error reporting the scammer for report number {i + 1}.")

    end_time = time.time()
    total_time = end_time - start_time
    bot.edit_message_text(chat_id=message.chat.id, message_id=progress_message.id, text=f"Sent {num_reports} reports for {scammer_username}. Total time: {total_time:.2f} seconds.")

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Telegram Scammer Reporting Bot. To report a scammer, use the /report command followed by the scammer's username. To mass report a scammer, use the /massreport command followed by the scammer's username.")

# Start the bot
bot.polling()
