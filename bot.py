import discord 
from discord.ext import commands 
from discord.ext.commands import Bot
import time

import random
import os


Bot = commands.Bot(command_prefix='!')


@Bot.event 
async def on_ready():
	print('Bot is online')

@Bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 719326703851274270:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, Bot.guilds)
    
    role = discord.utils.get(guild.roles, name=payload.emoji.name)
    if role is not None:
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        if member is not None:
            await member.add_roles(role)
            print ('Done')
        else:
            print ('Member not found')
    else:
        print ('Role not found') 


@Bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 719326703851274270:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, Bot.guilds)
    
    role = discord.utils.get(guild.roles, name=payload.emoji.name)
    if role is not None:
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        if member is not None:
            await member.remove_roles(role)
            print ('Done')
        else:
            print ('Member not found')
    else:
        print ('Role not found')
	
	
	
	
@Bot.command( pass_context=True )
async def battle( ctx ):

	mentionedUser = ctx.message.raw_mentions
	mUser = ' '.join(map(str, mentionedUser))
	fUser = '<@' + mUser + '>'


	a = random.randint(0, 10)
	b = random.randint(0, 10)

	if a < b:
		await ctx.send ( '{0.author.mention} напал на '.format(ctx) + fUser + ' , но отхватил в ебучку' ) 
		
	if a > b:
		await ctx.send( '{0.author.mention} напал на '.format(ctx) + fUser + ' и накидал лоху в ебучку' )
		
			
				

@Bot.command(pass_context=True)
async def xui(ctx):
	a = random.randint(0, 100)
	await ctx.send('{0.author.mention} твой хуй '.format(ctx) + str(a) + 'см')
	

@Bot.command(pass_context=True)
async def raspisanie(ctx):
	await ctx.send('Нет никакого расписания, анонсы в группе вк (!vk)')

@Bot.command(pass_context=True)
async def vk(ctx):
	await ctx.send('Неебические мемы + анонсы стримов тут: https://vk.com/bagickstreams')

@Bot.command(pass_context=True)
async def bagick(ctx):
	await ctx.send('<@228814070822731776> - местный лох-стример. Зовут Богдан (aka Богдакан), 19 лет, живет в Санкт-Петербурге. Так как он ну совсем долбоеб, он решил начать стримить. А еще у него есть собака Эри и канал трэч.тв https://www.twitch.tv/bagick')

@Bot.command(pass_context=True)
async def xyesos(ctx):
	await ctx.send("Эй, {0.author.mention} хуесос! ".format(ctx))
	
@Bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount+2)



@Bot.command(pass_context=True)
async def friends(ctx):
	a = random.randint(1, 200)
	
	if a != 1:
		await ctx.send('Нет у тебя друзей, хуйло')
	
	if a == 1:
		await ctx.send('Ахуеть чел, у тебя есть друзья, вау!')

@Bot.command(pass_context=True)
async def commandlist(ctx):
	await ctx.send('Все команды транслитом !xui !battle *тегай того, с кем баттлишься* !raspisanie !vk !bagick !xyesos !friends !commandlist')


token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
