import logging
from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define a command handler. Usually takes two arguments: update and context
def start(update, context):
    update.message.reply_text('Hi!')

def help_command(update, context):
    update.message.reply_text('Help!')

def main():
    # Replace 'YOUR_TOKEN' with your actual bot token
    updater = Updater("6726592936:AAECEtZEt7noWVa_ZHUCovUDq2uLb0vKr0c", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
