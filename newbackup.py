import telebot
import random
import pyfiglet
import requests
from telebot import types
from user_agent import generate_user_agent as ua
import time

# Initialize the bot with your token
bot = telebot.TeleBot("7031783178:AAFMSnCLKn4Cvh5WBEzn4uZy_9xWllxV6Qk")

# Command to report a scammer
@bot.message_handler(commands=['massreport'])
def mass_report_scammer(message):
    # Get the username to report
    scammer_username = message.text.split()[1]

    # Define the number of reports to send
    num_reports = 50

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

        # Message to be sent for each report
        message_text = f"""Hello sir/ma'am,

I would like to report a Telegram user who is engaging in suspicious and harmful activities. Their username is {scammer_username}. I believe they may be involved in scams and phishing attempts, which is causing harm to the community. I would appreciate it if you could look into this matter and take appropriate action.

Thank you for your attention to this matter.
@SOLDIERX"""

        # Send the report
        res = requests.get('https://telegram.org/support', headers={
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
            "accept-language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5"
        }).cookies
        stel = res['stel_ssid']
        data = f'message={message_text}&email={email}&phone={num}&setln='
        req = requests.post('https://telegram.org/support', data=data, headers={
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
    bot.reply_to(message, "Welcome to the Telegram Scammer Reporting Bot. To report a scammer, use the /report command followed by the scammer's username. To mass report a scammer, use the /massreport command followed by the scammer's username. Regards @remoswipe")

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "I'm just a reporting bot. Please use the /report command to report scammers or the /massreport command to mass report scammers. Regards @remoswipe")

# Start the bot
bot.polling()