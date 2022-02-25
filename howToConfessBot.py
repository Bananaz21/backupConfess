import discord
from discord.ext import commands

#READ THE INSTRUCTIONS AT THE BOTTOM

client = commands.Bot(command_prefix='!', help_command=None)
outputID = 941860143111487509 #This is channel id, change this to whatever channel you want this to be
BOT_ID = 'BOT_ID' #This is where the bot ID is stored


@client.event #Event trigger, basicly activates whenever anything happens
@commands.dm_only() #Makes the next few lines of code only run if a message is in a DM
async def on_message(message):
    output = client.get_channel(outputID) #Grabs the ID above and connects to the message channel

    if message.author == client.user: #Prevents the bot from looping on itself
        return   
    if isinstance(message.channel, discord.channel.DMChannel): #double-check to make sure the message it recieves is from DMs
        await output.send(message.content) #Actualy sends the message to the channel

@client.event
async def on_ready(): #Tells us when the bot is up or not
    print(f'We have logged in as {client.user}')
    activity = discord.Activity(name="DM me, and i'll send a message to venting anonymously", type=discord.ActivityType.playing) #Sets the status to explain what the bot does.
    await client.change_presence(activity=activity) #Updates the status

client.run(BOT_ID) #This tells the program what bot to take control of


#INSTRUCTIONS
    #The instructions are in order, so I would recommend you go through them one by one.

#How to Set the Channel ID
    #Line 5 contains the channel ID
    #If you go into settings > Advanced > Developer Mode in discord, you can right-click on any channel and copy it's ID. It should be a button at the bottom.
    #Replace the ID here with the one you have

#How to Set the Bot id  
    #Line 24 contains the Bot ID
    #Go to https://discord.com/developers/applications
    #New Application button in top left, name it whatever you want
    #Go to the Bot tab on the left, and add the bot. Set the username to something nice, as well as the profile picture
    #Click copy on the bot token just under the name, and replace BOT-KEY with the key that you copied. Keep the quotes though.

    #DO NOT GIVE THE KEY TO ANYONE THAT YOU DON'T 100% TRUST
    #IT WILL GIVE THEM FULL CONTROL OF THE BOT, AND CAN FULLY DESTROY YOUR SERVER IF SOMETHING GOES WRONG

#How to Invite the Bot to Your Discord Server
    #Go to https://discord.com/developers/applications
    #Go to your application
    #Go to OAuth2 > URL Generator
    #Check the bot box

    #Now, here are the permissions for the bot. The bare minimum the bot needs are Read Messages and Send Messages.
    #If you want the bot to work with any other features then it would be best to just give it Administrator.
    #HOWEVER, this does give the bot admin to your server. I would only recommend you do this if you plan to use the upgraded version of my bot (See the bottom)
    #and trust yourself to keep the key safe. Else, it would be too risky.

    #Anyway, copy the URL at the bottom of the pae ge when you're done with the permissions, and go to the URL
    #Add it to your server, and it should be fully set up.

#Running the bot
    #To run the bot, you need Python 3 https://www.python.org/downloads/
    #You also need the dpendancy, so open Command Prompt
    #run the command: py -m pip install discord.py

    #Now, to run the bot you can just double-click on this .py file :)
    #The program needs to run for the bot to work, so just leave it in the background.
    #It should just output "We have logged in as {Bot name}"
    #if you see anything else, justt DM me and i'll figure it out when i can

#Advanced bot
    #If you want to run a bot with more advanced features, download the one in https://github.com/Bananaz21/confession-bot
    #It does require more permissions, so it should be set to admin. If you want, I can figure out the exact permissions.

#DM me if u have any problems