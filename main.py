from backports.zoneinfo import ZoneInfo
from re import I
from datetime import datetime
from pyrogram import Client, filters
import asyncio
from pyrogram.errors import FloodWait
from pyrogram.raw.functions.messages import UpdatePinnedMessage
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, input_message_content, user_and_chats ,ReplyKeyboardMarkup ,ReplyKeyboardRemove
import os
import time
import pytz

sl = pytz.timezone("Asia/Colombo") 
fmt='%Y-%m-%d %H:%M:%S'

bot = Client(
    'MY first project',
    api_id=7009965,
    api_hash='06651b174c4f0591deb0ed1e5663c996',
    bot_token='5339643413:AAFo7h6kndLWePwleblvOawnxlIA53FnhEY'
    
)
stoptimer = False
ss='⏰2022 උසස් පෙළ විභාගයට තව'

START_MESSAGE="I'm Alive"
START_BUTTONS=[
    [InlineKeyboardButton('OWNER',url='https://t.me/PUBUDUPRASAD')],
    [InlineKeyboardButton('❌CLOSE❌',callback_data='CLOSE')],
]

@bot.on_message(filters.command('start')) #start
def start(bot, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_BUTTONS)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@bot.on_callback_query()
async def UpdateBotCallbackQuery(client: Client, query: CallbackQuery):
  if query.data=="CLOSE":
        await query.message.delete()


@bot.on_message(filters.command('al'))
async def set_timer(bot, message):
    global stoptimer
    try:
        
            dt1 = datetime(2023,1,23,00,00,00,000000,tzinfo=ZoneInfo('Asia/Kolkata'))
            dt2 = datetime.now(pytz.timezone('Asia/Kolkata'))
            dt3 = int((dt1 - dt2).total_seconds())
            user_input_time = dt3
            user_input_event = str("⏰2022 උසස් පෙළ විභාගයට තව 🎓,")
            get_user_input_time = await bot.send_message(message.chat.id, user_input_time)
            n=1
            
            await get_user_input_time.pin()
            if stoptimer: stoptimer = False
            if user_input_time>=1:
                while user_input_time>0 and not stoptimer:
                    q=n
                    p=(28-q)
                    t=str(q*'●'+p*'○')
                    d=user_input_time//(3600*24)
                    h=user_input_time%(3600*24)//3600
                    m=user_input_time%3600//60
                    s=user_input_time%60
                    
                    Countdown_TeLe_TiPs=f"***{ss}***,\n{t}\n\n\n◇ **දින** [{d}]**යි**  **පැය** [{h}]**යි** **මිනිත්තු** [{m}]**යි**  **තත්පර** [{s}]**ක** **කාලයක්** **තිබෙයි**. 📚\n\n<i>'Live Countdown Timer'</i>\n\n\n{t}\n\n**[Powered By ScienceEDU⚡️]**"
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(9)
                    n+=1
                    if n>28:
                        n=n-28
                    user_input_time -=9
                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")
            else:
                pass

    except FloodWait as e:
        await asyncio.sleep(e.value)







@bot.on_message(filters.command('stopc'))
async def stop_timer(bot, message):
    global stoptimer
    try:
        if (await bot.get_chat_member(message.chat.id,message.from_user.id)):
            stoptimer = True
            await message.reply('🛑 Countdown stopped.')
        else:
            await message.reply('👮🏻‍♂️ Sorry, **only admins** can execute this command.')
    except FloodWait as e:
        await asyncio.sleep(e.value) 
bot.run()
