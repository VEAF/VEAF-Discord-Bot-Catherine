#coding:utf-8

####################################
#       By Mikcael.exe#8186        #
###############################################################################################################
#       _..._                                                                                                 #
#    .-'_..._''.                                                                                              #
#  .' .'      '.\                    .              __.....__             .--.   _..._         __.....__      #
# / .'                             .'|          .-''         '.           |__| .'     '.   .-''         '.    #
#. '                           .| <  |         /     .-''"'-.  `. .-,.--. .--..   .-.   . /     .-''"'-.  `.  #
#| |                 __      .' |_ | |        /     /________\   \|  .-. ||  ||  '   '  |/     /________\   \ #
#| |              .:--.'.  .'     || | .'''-. |                  || |  | ||  ||  |   |  ||                  | #
#. '             / |   \ |'--.  .-'| |/.'''. \\    .-------------'| |  | ||  ||  |   |  |\    .-------------' #
# \ '.          .`" __ | |   |  |  |  /    | | \    '-.____...---.| |  '- |  ||  |   |  | \    '-.____...---. #
#  '. `._____.-'/ .'.''| |   |  |  | |     | |  `.             .' | |     |__||  |   |  |  `.             .'  #
#    `-.______ / / /   | |_  |  '.'| |     | |    `''-...... -'   | |         |  |   |  |    `''-...... -'    #
#             `  \ \._,\ '/  |   / | '.    | '.                   |_|         |  |   |  |                     #
#                 `--'  `"   `'-'  '---'   '---'                              '--'   '--'                     #
#  _____  _                       _   ____        _                                                           #
# |  __ \(_)                     | | |  _ \      | |                                                          #
# | |  | |_ ___  ___ ___  _ __ __| | | |_) | ___ | |_                                                         #
# | |  | | / __|/ __/ _ \| '__/ _` | |  _ < / _ \| __|                                                        #
# | |__| | \__ \ (_| (_) | | | (_| | | |_) | (_) | |_                                                         #
# |_____/|_|___/\___\___/|_|  \__,_| |____/ \___/ \__|                                                        #
###############################################################################################################


import os
import time
import discord
import asyncio
import json
import logging
import datetime
from discord.ext import commands
from discord.ext import tasks

version = "0.0.1"
errorCatched = 0

def printAndLog(msg):
	print(msg)	
	logging.log(logging.INFO, msg)

logging.basicConfig(level=logging.INFO,filename="log.log",format="%(asctime)s:%(levelname)s:%(message)s")

printAndLog("VEAF Bot version is " + version + " starting...")
print(time.strftime("Démarrage le %d/%m/%Y à %H:%I:%S, %Z"))

intents = discord.Intents().all()

with open('data.json') as i: #Load json parameters
	data = json.load(i)

ServerID = data["ServerID"]
CommandChannel = data["CommandChannel"]
AutopurgedChannel = data["AutopurgedChannel"]
AutoPurgeMaxMessageAgeInMinutes = int(data["AutoPurgeMaxMessageAgeInMinutes"])
AutoPurgeTimer = int(data["AutoPurgeTimerInMinutes"]) * 60
AutoPurgeOn = 0
AutoTriggerAutoPurge = data["AutoTriggerAutoPurge"]
if AutoTriggerAutoPurge == 1 or AutoTriggerAutoPurge == 0
	AutoTriggerAutoPurge = bool(AutoTriggerAutoPurge)
except:
	print("An exception occured in the data.json file, AutoTriggerAutoPurge must be 0 or 1 (as an integer)")
	errorCatched += 1

client = commands.Bot(command_prefix = "&", intents=intents) #Change the "&" to change the bot's prefix

async def _purge():
	while True:
		if AutoPurgeOn == 0:
			break
		purgedChannel, timelimit = preparePurge(client, AutoPurgeMaxMessageAgeInMinutes)
		await purgedChannel.purge(limit=500, before=timelimit, check=lambda msg: not msg.pinned)
		await asyncio.sleep(AutoPurgeTimer)

@client.event
async def on_ready():
	printAndLog('Enregistré avec succès en tant que {0.user}'.format(client)) #This message is shown on the console when the bot is ready
	client.loop.create_task(update_presence()) #Enable dynamic RichPresence
	if AutoTriggerAutoPurge:
		global AutoPurgeOn
		if AutoPurgeOn == 0:
			AutoPurgeOn = 1
			printAndLog("Enabling automatic purge")
			#await ctx.send(":recycle:  La purge automatique est maintenant activée !")
			await _purge()

#Message when the bot got removed from a server
@client.event
async def on_guild_remove(guild):
	printAndLog(f"Le bot a été retiré du serveur suivant : {guild}")

#Message when the bot got added to a server
@client.event
async def on_guild_join(guild):
	printAndLog(f"Le bot a été ajouté au serveur suivant : {guild}")


def isOnCommandChannel(ctx):
	return ctx.message.channel.id == int(CommandChannel)

#It's a basic &help command
@client.command()
@commands.has_permissions(send_messages = True)
async def aide(ctx):
	if isOnCommandChannel(ctx):
		embed = discord.Embed(title=f"Documentation du bot :", description=f"Voici la liste des informations importantes :", color = 0xFF00FF)
		embed.add_field(name = "Préfix : &", value = "Le préfixe est à utiliser à chaque début de commmande\n ``Exemple : &commande``", inline=False)
		embed.add_field(name = "Commande aide", value = "Cette commande permet d'afficher ce que vous êtes en train de lire !\n ``Utilisation : &aide``", inline=True)
		embed.add_field(name = "Commande purge", value = "Cette commande permet de déclencher la purge des messages plus vieux que l'argument (en minutes)\n ``Utilisation : &purge 10``", inline=True)
		embed.add_field(name = "Commande autopurge", value = "Cette commande permet d'activer ou de désactiver la purge automatique\n ``Utilisation : &autopurge``", inline=True)
		embed.add_field(name = "Où effectuer les commandes ?", value = "Vous devez effectuer les commandes dans le salon ``#catherine-command-channel``", inline=False)
		embed.set_thumbnail(url = "https://bit.ly/3oyArah")
		await ctx.author.send(embed = embed)
	else:
		await ctx.author.send("Catherine est un bot actuellement réservé aux administrateurs, et ne répond qu'aux commandes envoyées dans le salon ``#catherine-command-channel``")

def preparePurge(client, minutes):
		timelimit = datetime.datetime.utcnow() - datetime.timedelta(minutes=minutes)
		logging.log(logging.DEBUG, "purge called, minutes=%s, timelimit=%s", minutes, timelimit)
		purgedChannel = client.get_guild(ServerID).get_channel(AutopurgedChannel)
		return purgedChannel, timelimit

#Purge messages
@client.command()
@commands.has_permissions(manage_messages = True)
async def purge(ctx, minutes:int=AutoPurgeMaxMessageAgeInMinutes):
	if isOnCommandChannel(ctx):
		purgedChannel, timelimit = preparePurge(client, minutes)
		await purgedChannel.purge(limit=500, before=timelimit, check=lambda msg: not msg.pinned)

#Timed messages purge
@client.command()
@commands.has_permissions(manage_messages = True)
async def autopurge(ctx):
	if isOnCommandChannel(ctx):
		global AutoPurgeOn
		if AutoPurgeOn == 0:
			AutoPurgeOn = 1
			printAndLog("Enabling automatic purge")
			await ctx.send(":recycle:  La purge automatique est maintenant activée !")
			await _purge()
		else:
			printAndLog("Disabling automatic purge")
			await ctx.send(":recycle:  La purge automatique est maintenant désactivée !")
			AutoPurgeOn = 0

@client.command()
@commands.has_permissions(manage_messages = True)
async def test(ctx):
	print(ctx)

#Error management
@client.event
async def on_command_error(ctx, error):
	print(error)
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"⌛ Cette commande est en cooldown, vous pourrez l'exécuter dans {round(error.retry_after, 1)} secondes (CommandOnCooldown)")
	elif isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("<:signwarningicon:846112477997301771> Au moins un argument est manquant, pour plus d'informations, faites `&aide`. (MissingRequiredArgument)")
	elif isinstance(error, discord.DMChannel):
		await ctx.send(f"<:mapmarkericon:846110289203560448> La commande doit être exectué dans un serveur (DMChannel)")
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send("<:shieldwarningicon:847082331823144961> Vous ne possédez pas la/les permission(s) requise pour exectuer cette commande ! (MissingPermissions)")
	elif isinstance(error, commands.CommandNotFound):
		await ctx.send("<:signwarningicon:846112477997301771> Votre demande est inconue ! Si vous n'êtes pas sur de l'orthographe de votre requête, `faites &aide` (CommmandNotFound)")
	elif isinstance(error, commands.MissingAnyRole):
		await ctx.send(f"<:shielderroricon:847082331365441537> Il vous manque un role pour effecter cette commande.")
	elif isinstance(error, commands.BotMissingPermissions):
		await ctx.send("On dirai que je n'ai pas la permission d'effectuer ceci, veuillez contacter un administrateur.")
		print("On dirai que je n'ai pas la permission d'effectuer ceci, veuillez contacter un administrateur.")
	elif isinstance(error, commands.MemberNotFound):
		await ctx.send("<:username:846107877798182923> L'utilisateur est introuvable, vérifiez l'orthographe et réessayer. (MemberNotFound)")
	elif isinstance(error, commands.BadArgument):
		await ctx.send("<:signwarningicon:846112477997301771> Une erreur est survenue durant la conversion, veuillez réessayer (BadArgument)")
#	elif isinstance(error.original, discord.Forbidden):
#		await ctx.send("<:shieldwarningicon:847082331823144961> On dirai que vous n'avez pas la permission d'effectuer ceci ! <:shieldwarningicon:847082331823144961> (Forbidden)")
	elif isinstance(error, commands.ConversionError):
		await ctx.send("<:shieldwarningicon:847082331823144961> Une erreur est survenue durant la conversion, veuillez réessayer (ConversionError)")
	elif isinstance(error, commands.PrivateMessageOnly):
		await ctx.send("Cette commande doit être effectuée en message privé (PrivateMessageOnly)")
	elif isinstance(error, commands.CheckFailure):
		message = await ctx.send("<:signwarningicon:846112477997301771> Une erreur est survenue, veuillez vérifier les faits suivant :\n-La commande est exectuté dans le bon salon\n-Vos arguments sont correctes\nSi le problème persiste, veuillez contacter le développeur/un administateur (CheckFailure)")
		await asyncio.sleep(7)
		await message.delete()


#Dynamic rich presence
async def update_presence():
	while True:
		await client.change_presence(activity=discord.Game(name="Site web : veaf.org"))
		await asyncio.sleep(5)
		await client.change_presence(activity=discord.Game(name="Besoin d'aide ? Faites &aide"))
		await asyncio.sleep(30)
		await client.change_presence(activity=discord.Game(name="Ce bot est le bot offciel de la VEAF"))
		await asyncio.sleep(5)

if errorCatched == 0:
	token = open("token.txt","r").readline() #Put your token in this file (token.txt)
	client.run(token) #/!\ DO NOT SHARE YOUR TOKEN ! /!\
	printAndLog("[i] VEAF Bot is shutting down... Bye bye !") #The bot is shutting down...
else:
	printAndLog("[!] Some exception occured, aborting...")


'''
Tout doux : / 
'''