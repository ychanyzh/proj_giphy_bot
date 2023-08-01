import requests
import utils
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def giphy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a GIF to your message"""
    str_args = " ".join(context.args)
    if str_args:
        url = f"https://api.giphy.com/v1/gifs/translate?api_key={utils.GIPHY_TOKEN}&s={str_args}"
        resp = requests.get(url)
        data = resp.json()["data"]["images"]["original"]["url"]
        await update.message.reply_animation(data)
    else:
        await update.message.reply_text("(Please enter word or sentence after the command: )")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Help message to user"""
    await update.message.reply_text(
        '''Please enter\n<b>/giphy {keyword}</b>\ncommand to get the GIF from Giphy service.''', parse_mode="HTML"
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start message to user"""
    await update.message.reply_text(
        "Welcome! This bot allows you to search for GIFs using the /giphy command. "
        "Type /help to see how to use the bot."
    )


def main() -> None:
    """Start the bot"""
    # Create the Application
    application = Application.builder().token(utils.TG_TOKEN).build()
    # Command sends a GIF to your message
    application.add_handler(CommandHandler("giphy", giphy))
    # Help Command
    application.add_handler(CommandHandler("help", help))
    # Start Command
    application.add_handler(CommandHandler("start", start))
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
