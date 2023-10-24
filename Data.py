from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
أهلا عزيزي  {}

 يمكنك استخراج جميع الجلسات التي سوف تحتاجها ▶

🎯جلسة تيرمكس تليثون 
🎯تيرمكس تليثون للبوتات
🎯بايروجرام تليثون للحسابات 
🎯بايروجرام للبوتات 

¤🕷صاحب البوت |    ⌯ ˹𝘿𝙚𝙫˼ ♕. 𓃬
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(" ¤¦ بدأ استخراج الكود ", callback_data="generate")],
        [InlineKeyboardButton(text="¤¦ رجــوع", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton(" ¤¦ بدأ استخراج الكود ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton(" ¤¦ بدأ استخراج الكود ", callback_data="generate")],
        [
            InlineKeyboardButton("¤¦ كيف تستخدمني", callback_data="help"),
            InlineKeyboardButton("¤¦ حــول", callback_data="about")
        ]
    ]

    # Help Message
    HELP = """
✨ **📬 ¦ كـيف تستخـدمني** ✨

× /about - حول البوت
× /help - لتسوي روحك كلشي متعرف
× /start - حتى تشغل البوت
× /generate - حتى تبدا بأستخراج جلسة
× /cancel - لألغاء الاستخراج
× /restart - اعادة تشغيل البوت
"""

    # About Message
    ABOUT = """
**¤¦حـول البـوت** 

- بـوت استخـراج جـلـسـات

[قناة البوت](https://t.me/sessions78)

[جروب البوت](https://t.me/sessions77)

استخدم البوت : 

»[Pyrogram](docs.pyrogram.org)
🕹
»[Python](www.python.org)

لغة البوت : [بايثون](www.python.org)

🇲🇦 ¦ المطور  : [⌯ ˹𝘿𝙚𝙫˼ ♕. 𓃬](https://t.me/sw_vx)
    """
