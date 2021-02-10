# -*- coding: UTF-8 -*-

import pekobot
from pekobot import *

from . import main

bot = get_bot()


# @bot.on("group.message") 另一种写法
@bot.on_message("group")
async def elp(context):
    qun = context['target_id']
    msg = context['content']
    if msg[:5] == "1echo":
        await bot.send(group_id=qun, message=msg[6:])


# @bot.on("message.group.text") 事件：群组（频道）文本消息
# @bot.on("message.group.image") 事件：群组（频道）图片消息
# 其余的参照文档 “Events” 部分

@bot.on("added_reaction")
async def elp(context):
    qun = context['extra']['body']['channel_id']
    await bot.send(group_id=qun, message="添加了反应")
