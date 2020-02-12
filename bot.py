import random
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


@client.event
async def on_message ( message ):


	msg = message.content.lower()

	#сделано жесть как уебищно, найти как сделать через client.command

	if msg =='!хуй':
		a = random.randint(0, 30)
		await message.channel.send('Твой хуй ' + str(a) + 'см')


	if msg == '!лучший':
		await message.channel.send('Ну лучший в этом говнокоммьюнити бейджика это определенно {@rivalryy.mention}')
	
	
	if msg == '!расписание':
		await message.channel.send('Нет никакого расписания, анонсы в группе вк (!vk)')

	if msg == '!vk':
		await message.channel.send('Неебические мемы + анонсы стримов тут: https://vk.com/bagickstreams')


	if msg == '!bagick':
		await message.channel.send('@bagick - местный лох-стример. Зовут Богдан (aka Богдакан), 19 лет, живет в Санкт-Петербурге. Так как он ну совсем долбоеб, он решил начать стримить. А еще у него есть собака Эри и канал трэч.тв https://www.twitch.tv/bagick')

	if msg in hello_words:
		await message.channel.send('Zdarova yrod')


	if msg == "!xyй":
		await message.channel.send('Твой хуй 228 см')


	if msg == "!commandlist":
		await message.channel.send('!хуй !лучший !расписание !vk !bagick !хуесос')

	if msg == '!хуесос':
		 await message.channel.send("Эй, {0.author.mention} хуесос! ".format(message))

	if msg == '!друзья':
		await message.channel.send('Нет у тебя друзей, хуила')




#run the bot safely
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
