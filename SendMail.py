import smtplib
import os
from email.message import EmailMessage
import filetype
# from secrets import EMAIL_PASSWORD, EMAIL_ADDRESS


EMAIL_ADDRESS = os.environ['EMAIL_ADDRESS']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
# Access_token = os.environ['Access_token']
# Access_Token_Secret = os.environ['Access_Token_Secret']


def send_video_mail(fn):

    msg = EmailMessage()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)


    msg['Subject'] = 'Here is the Twitter video you requested for'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'akshaykalucha@gmail.com'
    msg.set_content("Find the video attached")

    ddir = './videos/'
    op_dir = os.path.join(ddir, fn)
    with open(op_dir, 'rb') as f:
        file_data = f.read()
        file_type = filetype.guess_extension(op_dir)
    
    msg.add_attachment(file_data, maintype='video', subtype=file_type, filename=fn)

    server.send_message(msg)
    print('Hey email sent')
    server.quit

    @run_async
def reply_filter(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    message = update.effective_message  # type: Optional[Message]
    to_match = extract_text(message)
    if not to_match:
        return

    if message.reply_to_message:
        message = message.reply_to_message


    chat_filters = sql.get_chat_triggers(chat.id)
    for keyword in chat_filters:
        pattern = r"( |^|[^\w])" + re.escape(keyword) + r"( |$|[^\w])"
        if re.search(pattern, to_match, flags=re.IGNORECASE):
            filt = sql.get_filter(chat.id, keyword)
            buttons = sql.get_buttons(chat.id, filt.keyword)
            media_caption = filt.caption if filt.caption is not None else ""
            if filt.is_sticker:
                message.reply_sticker(filt.reply)
            elif filt.is_document:
                message.reply_document(filt.reply, caption=media_caption, parse_mode=ParseMode.MARKDOWN)
            elif filt.is_image:
                if len(buttons) > 0:
                    keyb = build_keyboard(buttons)
                    keyboard = InlineKeyboardMarkup(keyb)
                    message.reply_photo(filt.reply, caption=media_caption, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
                else:
                    message.reply_photo(filt.reply, caption=media_caption, parse_mode=ParseMode.MARKDOWN)
            elif filt.is_audio:
                message.reply_audio(filt.reply, caption=media_caption, parse_mode=ParseMode.MARKDOWN)
            elif filt.is_voice:
                message.reply_voice(filt.reply, caption=media_caption, parse_mode=ParseMode.MARKDOWN)
            elif filt.is_video:
                message.reply_video(filt.reply, caption=media_caption, parse_mode=ParseMode.MARKDOWN)
            elif filt.has_markdown:
                keyb = build_keyboard(buttons)
                keyboard = InlineKeyboardMarkup(keyb)

                should_preview_disabled = True
                if "telegra.ph" in filt.reply or "youtu.be" in filt.reply:
                    should_preview_disabled = False

@run_async
@user_admin
def stop_all_filters(bot: Bot, update: Update):
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message

    if chat.type == "private":
        chat.title = "local filters"
    else:
        owner = chat.get_member(user.id)
        chat.title = chat.title	
        if owner.status != 'creator':	
            message.reply_text("You must be this chat creator.")	
            return

    x = 0
    flist = sql.get_chat_triggers(chat.id)

    if not flist:
        message.reply_text("There aren't any active filters in {} !".format(chat.title))
        return

    f_flist = []
    for f in flist:
        x += 1
        f_flist.append(f)

    for fx in f_flist:
        sql.remove_filter(chat.id, fx)

    message.reply_text("{} filters from this chat have been removed.".format(x))


def __stats__():
    return "{} filters, across {} chats.".format(sql.num_filters(), sql.num_chats())


def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)


def __chat_settings__(chat_id, user_id):
    cust_filters = sql.get_chat_triggers(chat_id)
    return "There are `{}` custom filters here.".format(len(cust_filters))


__mod_name__ = "FILTERS 📜"

FILTER_HANDLER = CommandHandler("filter", filters)
STOP_HANDLER = CommandHandler("stop", stop_filter)
STOPALL_HANDLER = DisableAbleCommandHandler("stopall", stop_all_filters)
LIST_HANDLER = DisableAbleCommandHandler("filters", list_handlers, admin_ok=True)
CUST_FILTER_HANDLER = MessageHandler(CustomFilters.has_text, reply_filter)

dispatcher.add_handler(FILTER_HANDLER)
dispatcher.add_handler(STOP_HANDLER)
dispatcher.add_handler(STOPALL_HANDLER)
dispatcher.add_handler(LIST_HANDLER)
dispatcher.add_handler(CUST_FILTER_HANDLER, HANDLER_GROUP)