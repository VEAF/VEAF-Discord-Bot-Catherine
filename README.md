# Catherine - a discord bot for the VEAF
Written and maintained by Mikcael.exe

## What is Catherine ?
  
Catherine is a Discord Bot made for the VEAF (Virtual European Air Force).

We had some specific needs, among which : 
 
 - purging messages older than a certain date in a specific channel

## How to install Catherine ?

Catherine is coded on Python 3.10, and uses the following libraries:

- discord
- asyncio
- logging
- datetime

You can download and install them with **pip** with the following command :

``pip install -r requirements.txt``

## How to configure Catherine ?

### The token.txt file

This file contains the token that allows you to run Catherine on your server.

Create it by copying `token.txt.sample` and changing the default (dummy) values.

The token is accessible on the Discord Developer Portal, on the Catherine bot page.

Ask a VEAF developer or admin if you want to install Catherine on your server.

### The data.json file

This file is used to customize the bot.

Create it by copying `data.json.sample` and changing the default (dummy) values.

Details about each of the parameters is available in the file itself.

## How to use Catherine ?

In the command channel (the only channel where Catherine can accept commands from), issue one of the existing commands, with the `&` prefix:

- `&aide` to get help
- `&purge xxxx` to purge messages older than `xxxx` minutes in the autopurged channel
- `&autopurge` to toggle autopurge on and off