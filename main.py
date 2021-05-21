#coding:utf-8
#By Mikcael.exe#8186 
#Created the 20/05/2021 @ 19:16
#Last modified the 21/05/2021 @ 16:21
#Version 1.0

import random
import os
import time
import discord
import asyncio
from discord.ext import commands
from discord.ext import tasks


os.system("cls")
print("VEAF Bot is starting...")
os.system("title VEAF Bot")
os.system("color 03")

liste = ["1 + 1 = 2 (Ou 11 par fois)", #Cette liste est inutile, mais ne la supprimez pas !
"VEAF veut dire 'Virtual European Air Force'",
"Les cookies c'est très bon !",
"Ce bot à été développé par Mikcael (Il est beau)",
"Le bot a été créer initialement le 20/05/2021 à 19:16",
"Si vous lisez ceci, vous êtes sûrement sur la Terre",
"Le F14 a été inaugué en 1970",
"Le A10 a un canon de calibre 30 × 173 mm",
"Brrrrrrrrrrrrrrrrrrrrrrrr",
"La Terre est ronde (Enfin je crois)",
"Bim bam boum",
"Ce bot a été fait en Python 3.9",
"Les pates c'est bon (Enfin moi j'aime bien)"]



print("Welcome ! (Current version is 1.0)") #Version actuelle du bot

client = commands.Bot(command_prefix = "&") #Changez le "&" pour changer le préfix du bot


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client)) #Ce message est envoyé quand le bot est prêt à fonctionné
	await client.change_presence(activity=discord.Game(name="Besoin d'aide ? Faites &needhelp"))


@client.command()
@commands.has_permissions(send_messages = True)
#@commands.has_any_role('Cadet', "Membres VEAF")
@commands.cooldown(1, 100, commands.BucketType.user)
async def act(ctx, *, descInput ="Rien"): 
	'''
	La commande &act est une commande qui permet de créer une activité
	'''
	channel = client.get_channel(845299069882728500)
	auteur = (ctx.author.name)
	print(f"\nLa commande \"&act\" est en cours d'execution par {auteur} ({ctx.author.id})...")
	await ctx.send("Quel est votre activité (Description, Timeout is 2000 seconds)")
	descInput = await client.wait_for("message", timeout = 2000)

	await ctx.send("Quel est la date de votre activité ``(Format : Jour/Mois)`` ? ``(Timeout is 30 seconds)``")
	dateInput = await client.wait_for("message", timeout = 30)

	await ctx.send("A quel heure commence votre activité ``(Format : HH:MM)`` ? ``(Timeout is 30 seconds)``")
	heureDebutInput = await client.wait_for("message", timeout = 30)

	await ctx.send("A quel heure se termine votre activité ``(Format : HH:MM)`` ? (Timeout is 30 seconds)``")
	heureFinInput = await client.wait_for("message", timeout = 30)

	embed = discord.Embed(title=f"**Activité de {auteur}**", description=f"{descInput.content}\n\nRépondez avec la réaction \"✅\" si cette activité vous intéresse", color=0xDCAB00)
#	embed.set_author(name="VEAF Bot")
	embed.set_thumbnail(url = ctx.author.avatar_url)
	embed.add_field(name = "Date", value = dateInput.content)
	embed.add_field(name = "Heure", value = f"De {heureDebutInput.content} à {heureFinInput.content}")
	embed.set_footer(text = random.choice(liste))
	message = await channel.send(embed = embed)
	await message.add_reaction("✅")
	save = f"La commande \"&act\" à été exectué avec succès par {auteur} ({ctx.author.id}), contenu :\n Description : {descInput.content}\n Date et heure : {dateInput.content} de {heureDebutInput.content} à {heureFinInput.content}"
	print(save)

@client.command()
@commands.has_permissions(send_messages = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def aide(ctx):
	embed = discord.Embed(title=f"Documentation du bot :", description=f"Voici la liste des information importante :", color = 0xFF00FF)
	embed.add_field(name = "Préfix : &", value = "Le préfix est a utliliser a chaque début de commmande\n ``Exemple : &commande``", inline=False)
	embed.add_field(name = "Commande act", value = "Cette commande permet de créer une activitée dans le salon \"Ready Room\"\n ``Utilisation : &act``", inline=True)
	embed.add_field(name = "Commande needhelp", value = "Cette commande permet d'afficher ce que vous êtes entrain de lire !\n ``Utilisation : &aide``", inline=True)
	embed.add_field(name = "Commande clear", value = "Cette commande permet de supprimer les derniers messages envoyés dans le salon ou elle est exectué\n ``Utilisation : &clear [number]``", inline=True)
	embed.add_field(name = "Commande Serverinfo", value = "Cette commande permet d'afficher des informations sur le serveur\n ``Utilisation : &serverinfo``", inline=True)
	embed.add_field(name = "Commande où effetuer les commandes ?", value = "Vous devez effectuer les commandes de le salon ``:Salon Prévu a cette effet:``", inline=False)
	embed.set_footer(text = random.choice(liste))
	embed.set_thumbnail(url = "https://bit.ly/3oyArah")
	await ctx.send(embed = embed)

'''
Commande d'administration
'''

@client.command()
@commands.has_permissions(manage_messages = True)
@commands.cooldown(1, 2, commands.BucketType.user)
async def clear(ctx, number : int):
	await ctx.channel.purge(limit=number+1)
	embed = discord.Embed(title=f"♻️  **{number}** messages ont été supprimés avec succès  ♻️", color=0x00ff80)
	await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(manage_guild = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def serverinfo(ctx):
	embed = discord.Embed(title = "Informations sur le serveur", color = 0xFFFFFE)
	embed.add_field(name = "Nom du serveur :", value=ctx.guild)
	embed.add_field(name = "Nombre de membres :", value=ctx.guild.member_count)
	embed.add_field(name = "Nombre de salon textuels :", value= len(ctx.guild.text_channels), inline = False)
	embed.add_field(name = "Nombre de salon vocaux :", value= len(ctx.guild.voice_channels), inline = True)
	embed.add_field(name = "Propriétaire :", value=ctx.guild.owner, inline = False)
	embed.add_field(name = "Nombre de rôle :", value= len(ctx.guild.roles), inline = True)
	embed.add_field(name = "Salon du règlement :", value=ctx.guild.rules_channel, inline = True)
	embed.add_field(name = "Niveau de vérification :", value= ctx.guild.verification_level, inline = True)
#	embed.add_field(name = "Description :", value= ctx.guild.description, inline = True)
	embed.add_field(name = "Région du serveur :", value= ctx.guild.region, inline = True)
	embed.add_field(name = "Niveau de boost :", value = ctx.guild.premium_tier, inline = False)
	embed.add_field(name = "Serveur créer le :", value = ctx.guild.created_at, inline = False)
	embed.set_footer(text = random.choice(liste))
	embed.set_thumbnail(url = ctx.guild.icon_url)
	await ctx.send(embed = embed)




@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"Cette commande est en cooldown, vous pourrez l'exectuter dans {round(error.retry_after, 1)} secondes")
	elif isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"Cette commande est en cooldown, vous pourrez l'exectuter dans {round(error.retry_after, 1)} secondes")

#async def update_presence():
#	while True:
#		await client.change_presence(activity=discord.Game(name="Site web : veaf.org"))
#		await asyncio.sleep(10)
#		await client.change_presence(activity=discord.Game(name="Teamspeak : ts.veaf.org"))
#		await asyncio.sleep(10)
#		await client.change_presence(activity=discord.Game(name="Besoin d'aide ? Faites &needhelp"))
#		await asyncio.sleep(10)
#		await client.change_presence(activity=discord.Game(name="Ce bot est le bot offciel de la VEAF"))
#		await asyncio.sleep(10)
#client.loop.create_task(update_presence())


token = open("token.txt","r").readline() 
client.run(token) #/!\ CETTE LIGNE N'EST A SURTOUT PAS PARTAGER /!\

print("\n\n\n VEAF Bot is shutting down... Bye bye !") #Le bot s'éteint
os.system("color 07") #La console ce remet en blanc