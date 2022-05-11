from ast import Call
from telegram.update import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
		"I am the Dabney Flamer of the Keep Bot. Lilia, when's the " +
        "woordworking competition?")

def help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    if (update.message.from_user.username == 'dominusdraconis'):
        update.message.reply_text('No help for you until you tell us when' +
                                  'the woodworking competition is.')
    else:
        update.message.reply_text('help: Lists commands\n' +
                                  'poem: Says a nice poem.')

def poem(update: Update, context: CallbackContext):
    """Replies with the poem that I wrote for the woodworking
    competition
    """
    update.message.reply_text("For years I have waited for the day\n" +
                              "Where I can finally achieve my mission\n" +
                              "So there's only one question left to ask:\n" +
                              "Lilia, when's the woodworking competition?")

def jarjar(update: Update, context: CallbackContext):
    """Asks Lilia when the woodworking competition is in Gungan"""
    update.message.reply_text('Lilia, whensa da woodworken competition?')

def impeach(update: Update, context: CallbackContext):
    """Calls for Lilia's impeachment."""
    msg = update.message.text
    if (msg.lower() == 'impeach' or msg.lower() == 'impeach!'):
        update.message.reply_text(msg)

def bot(update: Update, context: CallbackContext):
    """Shames Lilia for using a bot. Only replies to the
    Keeper of the Flame bot
    """
    if (update.message.from_user.username == 'flame_keeper_bot'):
        update.message.reply_text('Wow, Lilia... Using a bot? So pathetic.')

def ask(update: Update, context: CallbackContext):
    """Asks Lilia when the woodworking competition is.
    Responds to any message by Lilia
    """
    if (update.message.from_user.username == 'dominusdraconis'):
        update.message.reply_text('Lilia, when\'s the woodworking competition?')

def wee(update: Update, context: CallbackContext):
    """Hoo?"""
    if ('wee' in update.message.text.lower()):
        update.message.reply_text('Hoo?')
    
