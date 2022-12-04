from backports.zoneinfo import ZoneInfo
from re import I
from datetime import datetime
from pyrogram import Client, filters
import asyncio
from pyrogram.errors import FloodWait
from pyrogram.raw.functions.messages import UpdatePinnedMessage

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

            
@bot.on_message(filters.command('fs'))
async def set_timer(bot, message):
    global stoptimer
    try:
        
            dt1 = datetime(2022,1,23,00,00,00,000000,tzinfo=ZoneInfo('Asia/Kolkata'))
            dt2 = datetime.now(pytz.timezone('Asia/Kolkata'))
            dt3 = int((dt1 - dt2).total_seconds())
            user_input_time = dt3
            user_input_event = str("⏰2022 උසස් පෙළ විභාගයට තව🎓,")
            get_user_input_time = await bot.send_message(message.chat.id, user_input_time)
            n=1
            await get_user_input_time.pin()
            if stoptimer: stoptimer = False
            if 0<user_input_time<=10 :
                while user_input_time and not stoptimer:
                    q=n
                    p=(42-q)
                    t=str(q*'●'+p*'○')
                    s=user_input_time%60
                    Countdown_TeLe_TiPs=f"***{ss}***,\n{t}\n\n\n◇ **තත්පර** {s}**ක** කාලයක් තිබෙයි. 📚\n\n<i>'Live Countdown Timer'</i>\n\n\n{t}\n\nPowered By ❤️‍🔥PRASADX"
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(1)
                    n+=1
                    if n>42:
                        n=n-42
                    user_input_time -=1 
            elif 10<user_input_time<60:
                while user_input_time>0 and not stoptimer:
                    q=n
                    p=(42-q)
                    t=str(q*'●'+p*'○')
                    s=user_input_time%60
                    Countdown_TeLe_TiPs=f"***{ss}***,\n{t}\n\n\n◇ **තත්පර** {s}**ක** කාලයක් තිබෙයි. 📚\n\n<i>'Live Countdown Timer'</i>\n\n\n{t}\n\nPowered By ❤️‍🔥PRASADX"
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(3)
                    n+=1
                    if n>42:
                        n=n-42
                    user_input_time -=3  
                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")    
            elif 60<=user_input_time<3600:
                while user_input_time>0 and not stoptimer:
                    q=n
                    p=(42-q)
                    t=str(q*'●'+p*'○')
                    m=user_input_time%3600//60
                    s=user_input_time%60
                    Countdown_TeLe_TiPs=f"***{ss}***,\n{t}\n\n\n◇ **මිනිත්තු** {m}**යි**  **තත්පර** {s}**ක** කාලයක් තිබෙයි. 📚\n\n<i>'Live Countdown Timer'</i>\n\n\n{t}\n\nPowered By ❤️‍🔥PRASADX"
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(7)
                    n+=1
                    if n>42:
                        n=n-42
                    user_input_time -=7
                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")
            elif user_input_time>=86400:
                while user_input_time>0 and not stoptimer:
                    q=n
                    p=(42-q)
                    t=str(q*'●'+p*'○')
                    d=user_input_time//(3600*24)
                    h=user_input_time%(3600*24)//3600
                    m=user_input_time%3600//60
                    s=user_input_time%60
                    
                    Countdown_TeLe_TiPs=f"***{ss}***,\n{t}\n\n\n◇ **දින** {d}**යි**  **පැය** {h}**යි** **මිනිත්තු** {m}**යි**  **තත්පර** {s}**ක** කාලයක් තිබෙයි. 📚\n\n<i>'Live Countdown Timer'</i>\n\n\n{t}\n\nPowered By ❤️‍🔥PRASADX"
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(9)
                    n+=1
                    if n>42:
                        n=n-42
                    user_input_time -=9
                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")
            else:
                pass

    except FloodWait as e:
        await asyncio.sleep(e.x)







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
        await asyncio.sleep(e.x) 
bot.run()