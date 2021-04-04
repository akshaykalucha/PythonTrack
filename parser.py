import html
import json
import html
import os
from typing import List, Optional

# from telegram import Bot, Update, ParseMode, TelegramError
# from telegram.ext import CommandHandler, run_async
# from telegram.utils.helpers import mention_html

# from bot import dispatcher, WHITELIST_USERS, SUPPORT_USERS, SUDO_USERS, DEV_USERS, OWNER_ID
# from bot.modules.helper_funcs.chat_status import whitelist_plus, dev_plus
# from bot.modules.helper_funcs.extraction import extract_user
# from bot.modules.log_channel import gloggable

ELEVATED_USERS_FILE = os.path.join(os.getcwd(), 'bot/elevated_users.json')


@run_async
@whitelist_plus
def whitelistlist(bot: Bot, update: Update):
    reply = "<b>Whitelist user🤍:</b>\n"
    for each_user in WHITELIST_USERS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)

            reply += f"• {mention_html(user_id, user.first_name)}\n"
        except TelegramError:
            pass
    update.effective_message.reply_text(reply, parse_mode=ParseMode.HTML)

@run_async
@whitelist_plus
def whitelistlist(bot: Bot, update: Update):
    reply = "<b>Whitelist user🤍:</b>\n"
    for each_user in WHITELIST_USERS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)

            reply += f"• {mention_html(user_id, user.first_name)}\n"
        except TelegramError:
            pass
    update.effective_message.reply_text(reply, parse_mode=ParseMode.HTML)


@run_async
@whitelist_plus
def supportlist(bot: Bot, update: Update):
    reply = "<b>Support List🧡:</b>\n"
    for each_user in SUPPORT_USERS:
        user_id = int(each_user)
    if user_id in WHITELIST_USERS:
            message.reply_text("Demoting to normal user")
        WHITELIST_USERS.remove(user_id)
        data['whitelists'].remove(user_id)

        with open(ELEVATED_USERS_FILE, 'w') as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (f"#UNWHITELIST\n"
                       f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
                       f"<b>User:</b> {mention_html(user_member.id, user_member.first_name)}")

        if chat.type != 'private':
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message
    else:
        message.reply_text("This user is not a whitelist!")
        return ""


def search(title="", author="", year="", isbn=""):       # To pass some empty strings as default values. 
    # (="") Even thougt you input only one value of one parameter, the system will not be error.
    conn=sqlite3.connect("books.db")       #build a connect to the database
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))       
    # select all the books where title equals to something and others are the same.
    # (title, author, year, isbn) is the second parameter of the argument.
    rows=cur.fetchall()       #a row function to return the tuple
    conn.close() 
    return rows

def delete(id):  # delete the tuple of data by it's ID
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))            # Don't forget the comma
    conn.commit()
    conn.close() 

def update(id, title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))  # 'id' is at the end of the tuple
    conn.commit()
    conn.close() 

connect()
#insert("The Sun","Andy Wang",1918,9131231132) 
#delete(7)
update(5, "The moon","John Smooth",1917,99999)
print(view())
print(search(author="John Smith"))