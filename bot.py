﻿import random
import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot


client = commands.Bot(command_prefix='!')





#ключевые группы слов

hello_words = ['ky', 'привет', 'ку', 'здарова', 'хаэ' ]




@client.event 
async def on_ready():
	print('Bot is online')


@Bot.command( pass_context=True )
async def battle( ctx ):

	mentionedUser = ctx.message.raw_mentions
	mUser = ' '.join(map(str, mentionedUser))
	fUser = '<@' + mUser + '>'


	a = random.randint(0, 10)
	b = random.randint(0, 10)

	if a < b:
		await ctx.send ( fUser + ' накидал в ебучку {0.author.mention}'.format(ctx) )
	if a > b:
		await ctx.send( '{0.author.mention} накидал в ебучку '.format(ctx) + fUser )
			


@Bot.command(pass_context=True)
async def xui(ctx):
	a = random.randint(0, 30)
	await ctx.send('{0.author.mention} твой хуй '.format(ctx) + str(a) + 'см')

@Bot.command(pass_context=True)
async def raspisanie(ctx):
	await ctx.send('Нет никакого расписания, анонсы в группе вк (!vk)')

@Bot.command(pass_context=True)
async def vk(ctx):
	await ctx.send('Неебические мемы + анонсы стримов тут: https://vk.com/bagickstreams')

@Bot.command(pass_context=True)
async def bagick(ctx):
	await ctx.send('bagick - местный лох-стример. Зовут Богдан (aka Богдакан), 19 лет, живет в Санкт-Петербурге. Так как он ну совсем долбоеб, он решил начать стримить. А еще у него есть собака Эри и канал трэч.тв https://www.twitch.tv/bagick')

@Bot.command(pass_context=True)
async def xyesos(ctx):
	await ctx.send("Эй, {0.author.mention} хуесос! ".format(ctx))

@Bot.command(pass_context=True)
async def friends(ctx):
	await ctx.send('Нет у тебя друзей, хуила!')

@Bot.command(pass_context=True)
async def commandlist(ctx):
	await ctx.send('Все команды теперь транслитом !xui !raspisanie !vk !bagick !xyesos !friends !commandlist')



#run the bot safely
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
