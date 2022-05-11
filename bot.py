"""A joke bot to retain the great Dabney Hovse tradition of Flamer of the
Keep - with automation!

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Responds in different ways depending on messages sent to it by user
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from zmq import Message
import commands
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
    """Starts the bot."""
    # Bot Token
    updater = Updater("5330839133:AAF7SIG31bD0e8dVN6AzAy2zpF_J9z_H_tw",
				use_context=True)
     # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Command handlers
    dp.add_handler(CommandHandler('start', commands.start))
    dp.add_handler(CommandHandler('help', commands.help))
    dp.add_handler(CommandHandler('poem', commands.poem))
    dp.add_handler(CommandHandler('jarjar', commands.jarjar))

    # Message handlers
    dp.add_handler(MessageHandler(Filters.text, commands.bot))
    dp.add_handler(MessageHandler(Filters.text, commands.ask))
    dp.add_handler(MessageHandler(Filters.text, commands.impeach))
    dp.add_handler(MessageHandler(Filters.text, commands.wee))

    # Start the bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()