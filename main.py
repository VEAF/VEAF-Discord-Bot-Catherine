#coding:utf-8
#By Mikcael.exe#8186 
#Created the 20/05/2021 @ 19:16
#Last modified the 23/05/2021 @ 20:32
#Version Alpha 0.5.0

import random
import os
import time
import pickle
import discord
import asyncio
from discord.ext import commands
from discord.ext import tasks


os.system("cls")
print("VEAF Bot is starting...")
os.system("title VEAF Bot")
os.system("color 03")

liste = ["1 + 1 = 2 (Ou 11 par fois)", #This variable is useless, but do not delete it !
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
"Les pates c'est bon (Enfin moi j'aime bien)",
"Besoin d'aide, faites &aide",
"Le Huey a fait son premier vol le 22 octobre 1956",
"Le F18 a fait son premier vol le 18 novembre 1978",
"Le canon du F14 a un canon M61A1 Vulcan de 20 mm",
"Le F-14AM est une version améliorer du F14 effectuée par l'Iran, il est équipé de nouveaux missiles Fakour 90",
"Le A10 était initialement nommé le YA-10A",
"La premier atmosphérique normal est de 1013 hpa",
"Wayne Allwine (la voix de Mickey Mouse) et Russi Taylor (la voix de Minnie Mouse) étaient mariés dans la vraie vie",
"Quelque part dans le monde en ce moment, quelqu'un est en train de pousser une porte sur laquelle il y a écrit 'tirez'",
"Les loutres ont une petite poche dans leur peau pour y mettre leurs cailloux préférés, qu'elle utilise comme outils",
"Les marées dans les régions de Bretagne et de Normandie sont les plus fortes en Europe, avec une différence de niveau allant jusqu'à 15 mètres entre la marée basse et la marée haute.",
"KLM est la plus vieille compagnie aérienne, créé en 1919",
"En 1987, un compagnie aérienne Américaine a économisé $40,000 en retirant une olive de chaque salade servie en première classe",
"Un avion décolle ou se pose toues les 37 secondes au 'Chicago O’Hare’s International Airport'",
"Des compagnie aérienne Américaine on changé les manuelles papier des pilotes en IPad, ils ont économisé $1.2 million en fuel",
"Le pilote and et le co-pilote doivent manger de la nourritures différent en cas d'empoisoment alimentaire",
"Le vol de Sydney à Dallas en Qantas A380 est le vol le plus long en distance du monde",
"À l'heure ou j'écris ceci, le bot fait 391 lignes"]

intents = discord.Intents().all()

print("Welcome ! (Current version is Alpha 0.4)") #Current version
print(time.strftime("Démarrage le %d/%m/%Y à %H:%I:%S, %Z"))


client = commands.Bot(command_prefix = "&", intents=intents) #Change the "&" to change the bot's prefix


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client)) #This message is shown on the console when the bot is ready
	await client.change_presence(activity=discord.Game(name="Besoin d'aide ? Faites &aide")) #Enable RichPresence


JoinMessageChannel = "" #Declare JoinMessageChannel

with open('Data/JoinMessageChannel.bin', 'rb') as datafile:
	get_data = pickle.Unpickler(datafile)
	JoinMessageChannel = get_data.load() 
	JoinMessageChannel = int(''.join(map(str, JoinMessageChannel)))

LeaveMessageChannel = "" #Declare LeaveMessageChannel

with open('Data/LeaveMessageChannel.bin', 'rb') as datafile:
	get_data = pickle.Unpickler(datafile)
	LeaveMessageChannel = get_data.load() 
	LeaveMessageChannel = int(''.join(map(str, LeaveMessageChannel)))


#Message when a user join the guild
@client.event
async def on_member_join(member):
	channel = client.get_channel(JoinMessageChannel)
	embed = discord.Embed(title=f"**Bienvnenue à {member.name}**", description=f"Bienvenue sur le Discord de la veaf !", color=0xDCAB00)
	await channel.send(embed = embed)

#Message when a user leave the guild
@client.event
async def on_member_remove(member):
	channel = client.get_channel(LeaveMessageChannel)
	embed = discord.Embed(title=f"**Au revoir à {member.name}**", description=f"À la prochaine, à plus !", color=0xDCAB00)
	await channel.send(embed = embed)

#Message when a user got banned from the guild
@client.event
async def on_member_ban(user):
	channel = client.get_channel(LeaveMessageChannel)
	embed = discord.Embed(title=f"**⛔ {user.name} a été banni(e) ⛔!**", description=f"À la prochaine, à plus !", color=0xDCAB00)
	await channel.send(embed = embed)

#Message when the bot got removed from a server
@client.event
async def on_guild_remove(guild):
	print(f"Le bot a été retiré du serveur suivant : {guild}")

#Message when the bot got added to a server
@client.event
async def on_guild_join(guild):
	print(f"Le bot a été ajouté au serveur suivant : {guild}")


CommandChannel = "" #Declare CommandChannel

with open('Data/CommandChannel.bin', 'rb') as datafile:
	get_data = pickle.Unpickler(datafile)
	CommandChannel = get_data.load() 
	CommandChannel = int(''.join(map(str, CommandChannel)))

def wrong_channel(ctx):
	return ctx.message.channel.id == CommandChannel


@client.command()
@commands.has_permissions(send_messages = True)
@commands.check(wrong_channel)
#@commands.has_any_role('Cadet', "Membres VEAF")
@commands.cooldown(1, 100, commands.BucketType.user)
async def act(ctx, *, descInput ="Rien"): 
	'''
	The command &act is a commande to create an activity
	'''
	with open('Data/ReadyRoomChannel.bin', 'rb') as datafile:
		get_data = pickle.Unpickler(datafile)
		ReadyRoomChannel = get_data.load() 
	res = int(''.join(map(str, ReadyRoomChannel)))
	channel = client.get_channel(res)
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
@commands.check(wrong_channel)
#@commands.has_any_role('Cadet', "Membres VEAF")
@commands.cooldown(1, 100, commands.BucketType.user)
async def acti(ctx, *descInput): 
	'''
	The command &acti is a commande to create an activity
	'''

	content = " ".join(descInput)
	with open('Data/ReadyRoomChannel.bin', 'rb') as datafile:
		get_data = pickle.Unpickler(datafile)
		ReadyRoomChannel = get_data.load() 
	res = int(''.join(map(str, ReadyRoomChannel)))
	channel = client.get_channel(res)
	auteur = (ctx.author.name)
	print(f"\nLa commande \"&act\" est en cours d'execution par {auteur} ({ctx.author.id})...")
	embed = discord.Embed(title=f"**Activité de {auteur}**", description=f"{content}\n\nRépondez avec la réaction \"✅\" si cette activité vous intéresse", color=0xDCAB00)
#	embed.set_author(name="VEAF Bot")
	embed.set_thumbnail(url = ctx.author.avatar_url)
#	embed.add_field(name = "Date", value = dateInput.content)
#	embed.add_field(name = "Heure", value = f"De {heureDebutInput.content} à {heureFinInput.content}")
	embed.set_footer(text = random.choice(liste))
	message = await channel.send(embed = embed)
	await message.add_reaction("✅")
	embed = discord.Embed(title=f"La commande a été exectué avec succès par {auteur}")
	ctx.send("La commande a étét exectué avec succès")
	save = f"La commande \"&act\" a été exectué avec succès par {auteur} ({ctx.author.id}), contenu :\n Description : {content}"
	print(save)



#It's a basic &help command
@client.command()
@commands.has_permissions(send_messages = True)
@commands.check(wrong_channel)
@commands.cooldown(1, 10, commands.BucketType.user)
async def aide(ctx):
	embed = discord.Embed(title=f"Documentation du bot :", description=f"Voici la liste des information importante :", color = 0xFF00FF)
	embed.add_field(name = "Préfix : &", value = "Le préfix est a utliliser a chaque début de commmande\n ``Exemple : &commande``", inline=False)
	embed.add_field(name = "Commande act", value = "Cette commande permet de créer une activitée dans le salon \"Ready Room\"\n ``Utilisation : &act``", inline=True)
	embed.add_field(name = "Commande acti", value = "Cette commande permet de créer une activitée dans le salon \"Ready Room\" en une seule ligne\n ``Utilisation : &acti [description]``", inline=True)
	embed.add_field(name = "Commande aide", value = "Cette commande permet d'afficher ce que vous êtes entrain de lire !\n ``Utilisation : &aide``", inline=True)
	embed.add_field(name = "Commande say", value = "Cette commande permet de me faire dire ce que vous voulez\n ``Utilisation : &say [message]``", inline=True)
	embed.add_field(name = "Commande clear", value = "Cette commande permet de supprimer les derniers messages envoyés dans le salon ou elle est exectué\n ``Utilisation : &clear [number]``", inline=True)
	embed.add_field(name = "Commande serverinfo", value = "Cette commande permet d'afficher des informations sur le serveur\n ``Utilisation : &serverinfo``", inline=True)
	embed.add_field(name = "Commande userinfo", value = "Cette commande permet d'afficher des informations sur un utilisateur spécifique\n ``Utilisation : &userinfo [Mention d'utilisateur]``", inline=True)
	embed.add_field(name = "Commande settings", value = "Cette commande permet de modifier des informations pour le bot\n ``Utilisation : &settings help``", inline=True)
	embed.add_field(name = "Commande où effetuer les commandes ?", value = "Vous devez effectuer les commandes de le salon ``:Salon Prévu a cette effet:``", inline=False)
	embed.set_footer(text = random.choice(liste))
	embed.set_thumbnail(url = "https://bit.ly/3oyArah")
	await ctx.send(embed = embed)



#Purge messages
@client.command()
@commands.has_permissions(manage_messages = True)
@commands.cooldown(1, 2, commands.BucketType.user)
async def clear(ctx, number : int):
	await ctx.channel.purge(limit=number+1)
	embed = discord.Embed(title=f"♻️  **{number}** messages ont été supprimés avec succès  ♻️", color=0x00ff80)
	await ctx.send(embed = embed)


#Show server information
@client.command()
@commands.has_permissions(manage_guild = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def serverinfo(ctx):
	embed = discord.Embed(title = "Informations sur le serveur", color = 0xFFFFFE)
	embed.add_field(name = "Nom du serveur :", value= f"```{ctx.guild}```")
	embed.add_field(name = "Nombre de membres :", value= f"```{ctx.guild.member_count}```")
	embed.add_field(name = "Nombre de salon textuels :", value= f"```{len(ctx.guild.text_channels)}```", inline = False)
	embed.add_field(name = "Nombre de salon vocaux :", value= f"```{len(ctx.guild.voice_channels)}```", inline = True)
	embed.add_field(name = "Propriétaire :", value=f"```{ctx.guild.owner}```", inline = False)
	embed.add_field(name = "Nombre de rôle :", value= f"```{len(ctx.guild.roles)}```", inline = True)
	embed.add_field(name = "Salon du règlement :", value=f"```{ctx.guild.rules_channel}```", inline = True)
	embed.add_field(name = "Niveau de vérification :", value= f"```{ctx.guild.verification_level}```", inline = True)
#	embed.add_field(name = "Description :", value= ctx.guild.description, inline = True)
	embed.add_field(name = "Région du serveur :", value= f"```{ctx.guild.region}```", inline = True)
	embed.add_field(name = "Niveau de boost :", value = f"```{ctx.guild.premium_tier}```", inline = True)
	embed.add_field(name = "Serveur créer le :", value = f"```{ctx.guild.created_at}```", inline = False)
	embed.set_footer(text = random.choice(liste))
#	embed.set_thumbnail(url = ctx.guild.icon_url)
	await ctx.send(embed = embed)


@client.command()
@commands.has_permissions(manage_guild = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def userinfo(ctx, *, user: discord.Member = None):
	date_format = "%a, %d %b %Y %I:%M %p"
	embed = discord.Embed(title = f"Information sur {user.name}")
	embed.set_thumbnail(url=user.avatar_url)
	embed.add_field(name="Id de l'utilisateur :", value=f"```{user.id}```", inline = False)
	embed.add_field(name="Bot :", value=f"```{user.bot}```", inline = True)
	embed.add_field(name="Nickname :", value=f"```{user.display_name}```", inline = True)
	embed.add_field(name="Username :", value=f"```{user.name}```", inline = True)
	embed.add_field(name="Rendu de couleur :", value=f"```{user.color}```", inline = False)
	embed.add_field(name="À Rejoint le :", value=f"```{user.joined_at.strftime(date_format)}```", inline = True)
	embed.add_field(name="Compte Créé le :", value=f"```{user.created_at.strftime(date_format)}```", inline = True)
	perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
	embed.add_field(name="Permissions :", value=perm_string, inline=False)
	await ctx.send(embed = embed)

#Send the message you want
@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def say(ctx, *, msg=""):
	await ctx.send(msg)


#Settings Command

@client.command()
@commands.has_permissions(manage_guild = True)
async def settings(ctx, setting, *arg):
	global ReadyRoomChannel
	global CommandChannel
	global JoinMessageChannel
	global LeaveMessageChannel
	if setting == "ReadyRoomChannel":
		ReadyRoomChannel = arg
		with open('Data/ReadyRoomChannel.bin', 'wb') as datafile:
			ReadyRoomChannel = pickle.Pickler(datafile)
			ReadyRoomChannel.dump(arg)
		await ctx.send(f"L'option ReadyRoomChannel a bien été changé pour {arg}")
	if setting == "CommandChannel":
		CommandChannel = arg
		with open('Data/CommandChannel.bin', 'wb') as datafile:
			CommandChannel = pickle.Pickler(datafile)
			CommandChannel.dump(arg)
		await ctx.send(f"L'option CommandChannel a bien été changé pour {arg}")
		with open('Data/CommandChannel.bin', 'rb') as datafile:
			get_data = pickle.Unpickler(datafile)
			CommandChannel = get_data.load() 
			CommandChannel = int(''.join(map(str, CommandChannel)))
	if setting == "JoinMessageChannel":
		JoinMessageChannel = arg
		with open('Data/JoinMessageChannel.bin', 'wb') as datafile:
			JoinMessageChannel = pickle.Pickler(datafile)
			JoinMessageChannel.dump(arg)
		await ctx.send(f"L'option JoinMessageChannel a bien été changé pour {arg}")
		with open('Data/JoinMessageChannel.bin', 'rb') as datafile:
			get_data = pickle.Unpickler(datafile)
			JoinMessageChannel = get_data.load() 
			JoinMessageChannel = int(''.join(map(str, JoinMessageChannel)))
	if setting == "LeaveMessageChannel":
		JoinMessageChannel = arg
		with open('Data/LeaveMessageChannel.bin', 'wb') as datafile:
			LeaveMessageChannel = pickle.Pickler(datafile)
			LeaveMessageChannel.dump(arg)
		await ctx.send(f"L'option LeaveMessageChannel a bien été changé pour {arg}")
		with open('Data/LeaveMessageChannel.bin', 'rb') as datafile:
			get_data = pickle.Unpickler(datafile)
			LeaveMessageChannel = get_data.load() 
			LeaveMessageChannel = int(''.join(map(str, LeaveMessageChannel)))
	if setting == "help":
		embed = discord.Embed(title = "Listes des paramètres disponibles :", color = 0x666666)
		embed.add_field(name = "Comment utiliser la commande &settings ?", value = "```&settings <setting> <arg>\n```", inline = False)
		embed.add_field(name = "ReadyRoomChannel", value = "```Modifier le salon utilisé entant que \"ReadyRoom\"\n```", inline = False)
		embed.add_field(name = "CommandChannel", value = "```Modifier le salon utilisé entant que salon de commande\n```", inline = False)
		embed.add_field(name = "JoinMessageChannel", value = "```Modifier le salon utilisé entant que salon de bienvenue\n```", inline = False)
		embed.add_field(name = "LeaveMessageChannel", value = "```Modifier le salon utilisé entant que salon d'adieu\n```", inline = False)
		await ctx.send(embed = embed)
	#print(CommandChannel)
	#return ReadyRoomChannel and CommandChannel




#Error management
@client.event
async def on_command_error(ctx, error):
	print(error)
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"Cette commande est en cooldown, vous pourrez l'exectuter dans {round(error.retry_after, 1)} secondes (CommandOnCooldown)")
	elif isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Au moins un argument est manquant (MissingRequiredArgument)")
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send("Vous ne possédez pas les permissions requise pour exectuer cette commande ! (MissingPermissions)")
	elif isinstance(error, commands.CheckFailure):
		await ctx.send("Une erreur est survenue, si le problème persiste, veuillez contacter le développeur (CheckFailure)")
	elif isinstance(error, commands.CommandNotFound):
		await ctx.send("Impossible de trouver votre commande, verifiez l'orthographe et réessayez, si le problème persiste, exectuez la commande &aide (CommmandNotFound)")
	elif isinstance(error, commands.BotMissingPermissions):
		await ctx.send("On dirai que je n'ai pas la permission d'effectuer ceci, veuillez contacter un administrateur.")
		print("On dirai que je n'ai pas la permission d'effectuer ceci, veuillez contacter un administrateur.")
	elif isinstance(error.original, discord.Forbidden):
		await ctx.send("On dirai que je n'ai pas la permission d'effectuer ceci, veuillez contacter un administrateur. (Forbidden)")
		print("On dirai que je n'ai pas la permission d'effectuer ceci, veuillez contacter un administrateur. (Forbidden)")
	elif isinstance(error, commands.ConversionError):
		await ctx.send("Une erreur est survenue durant la conversion, veuillez reessayer (ConversionError)")
	elif isinstance(error, commands.BadArgument):
		await ctx.send("Une erreur est survenue durant la conversion, veuillez reessayer (BadArgument)")
	elif isinstance(error, commands.PrivateMessageOnly):
		await ctx.send("Cette commande doit être effectuée en message privé (PrivateMessageOnly)")
	elif isinstance(error, commands.MemberNotFound):
		await ctx.send("L'utilisateur entré est introuvable... (MemberNotFound)")
	elif isinstance(error, commands.MissingAnyRole):
		await ctx.send(f"Il vous manque le role {missing_roles} pour effecter cette commande.")
	elif isinstance(error, discord.DMChannel):
		await ctx.send(f"La commande doit être exectué dans un serveur (DMChannel)")

#Dynamic rich presence
#async def update_presence():
#	while True:
#		await client.change_presence(activity=discord.Game(name="Site web : veaf.org"))
#		await asyncio.sleep(10)
#		await client.change_presence(activity=discord.Game(name="Teamspeak : ts.veaf.org"))
#		await asyncio.sleep(10)
#		await client.change_presence(activity=discord.Game(name="Besoin d'aide ? Faites &aide"))
#		await asyncio.sleep(10)
#		await client.change_presence(activity=discord.Game(name="Ce bot est le bot offciel de la VEAF"))
#		await asyncio.sleep(10)
#client.loop.create_task(update_presence())


token = open("token.txt","r").readline() #Put your token in this file (token.txt)
client.run(token) #/!\ DO NOT SHARE YOUR TOKEN ! /!\

print("\n\n\n VEAF Bot is shutting down... Bye bye !") #The bot is shutting down...
os.system("color 07")