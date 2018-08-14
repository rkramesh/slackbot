import os,time,glob
import subprocess
from subprocess import Popen, PIPE
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@respond_to('I love you')
def love(message):
    message.reply('I love you too!')
'''
@respond_to(r'\cmd \<?(.*)\>?',re.IGNORECASE)
def cmd(message):
    message=message.replace("\cmd ","",1)
    cmdmsg=(subprocess.Popen(message, stdout=subprocess.PIPE, shell=True).communicate()[0]).decode(encoding='utf-8')
    message.reply(cmdmsg)
'''
@respond_to(r'\cmd \<?(.*)\>?',re.IGNORECASE)
def cmd(message, thing):
    # message.channel.upload_file(slack_filename, local_filename,
    #                              initial_comment='')
    print (thing)
    if message != '\cmd':
        cmdmsg=(subprocess.Popen(thing, stdout=subprocess.PIPE, shell=True).communicate()[0]).decode(encoding='utf-8')
        message.reply('Output: {}'.format(cmdmsg))



@respond_to('kplay')
def love(message):
    message.reply('playing Osmc Now!')
    os.system('kodi-send --action="PlayMedia({})"').format(message)

@respond_to('kboot',re.IGNORECASE)
def love(message):
    message.reply('Reboting Osmc Now!')
    Popen(["sudo","systemctl","restart","mediacenter" ], stdout=PIPE, stderr=PIPE)


@respond_to('Fuck')
def fuck(message):
    message.reply('Fuck you too!')

@listen_to('Can someone help me?')
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')

    # Message is sent on the channel
    message.send('I can help everybody!')

    # Start a thread on the original message
    message.reply("Here's a threaded reply", in_thread=True)
