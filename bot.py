from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_TOKEN_HERE' with your bot's token
TOKEN = '7031783178:AAFqPE0D6HSZFwFk7400_Hkx0Rl2nQqHTKE'

# Define a command handler function for the start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am a bot. How can I help you?')

# Define a message handler function for echoing messages
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    # Create an Updater object with the bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start command handler
    dispatcher.add_handler(CommandHandler('start', start))

    # Register a message handler for echoing messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
