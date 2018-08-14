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


@respond_to('kplay')
def love(message):
    message.reply('playing Osmc Now!')
    os.system('kodi-send --action="PlayMedia({})"').format(message)
'''
@respond_to('kboot',re.IGNORECASE)
def love(message):
    message.reply('Reboting Osmc Now!')
    Popen(["sudo","systemctl","restart","mediacenter" ], stdout=PIPE, stderr=PIPE)

aws ec2 describe-instances --query 'Reservations[].Instances[].[Tags[?Key==`Name`].Value[],InstanceType,PrivateIpAddress,LaunchTime]' --output text | sed '$!N;s/\n/ /'

'''

@respond_to('aws-dev',re.IGNORECASE)
def love(message):
    message.reply('Getting list of dev!')
#    Popen(["aws ec2 describe-instances --query 'Reservations[].Instances[].[Tags[?Key==`Name`].Value[],InstanceType,PrivateIpAddress,LaunchTime]' --output text | sed '$!N;s/\n/ /'" ], stdout=PIPE, stderr=PIPE)
#    rk = os.system("aws ec2 describe-instances --query 'Reservations[].Instances[].[Tags[?Key==`Name`].Value[],InstanceType,PrivateIpAddress,LaunchTime]' --output text " )
#    pk=subprocess.check_output("aws ec2 describe-instances --query 'Reservations[].Instances[].[Tags[?Key==`Name`].Value[],InstanceType,PrivateIpAddress,LaunchTime]' --output text", shell=True).strip()
#    tk=subprocess.check_output(["aws ec2 describe-instances --query 'Reservations[].Instances[].[Tags[?Key==`Name`].Value[],InstanceType,PrivateIpAddress,LaunchTime]' --output text", 'sed', '$!N;s/\n/ /'], shell=True)
#    tk=subprocess.Popen("aws ec2 describe-instances --query 'Reservations[].Instances[].[Tags[?Key==`Name`].Value[],InstanceType,PrivateIpAddress]' --output text | sed 's/.*: //g' | sed 's/,/ \//g'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0].strip()
#    ck=subprocess.check_output( 'aws ec2 describe-instances --output text --query "PrivateIpAddress,Reservations[*].Instances[*].[InstanceId,State.Name,Tags[0].Value]"', shell=True, stderr=subprocess.STDOUT )
    tk=subprocess.check_output( 'aws ec2 describe-instances --output text --profile=helix-dev --query "Reservations[*].Instances[*].[PrivateIpAddress,InstanceId,State.Name,Tags[0].Value]"', shell=True, stderr=subprocess.STDOUT )

    message.reply(tk)

@respond_to(r'aws \<?(.*)\>?',re.IGNORECASE)
def aws(message, thing):
    if thing == 'helix-dev':
       tk=subprocess.check_output( 'aws ec2 describe-instances --output text --profile=helix-dev --query "Reservations[*].Instances[*].[PrivateIpAddress,InstanceId,State.Name,Tags[0].Value]"', shell=True, stderr=subprocess.STDOUT )
       message.reply(tk)

    elif thing == 'helix-qa':
       tk=subprocess.check_output( 'aws ec2 describe-instances --output text --profile=helix-qa --query "Reservations[*].Instances[*].[PrivateIpAddress,InstanceId,State.Name,Tags[0].Value]"', shell=True, stderr=subprocess.STDOUT )
       message.reply(tk)


    elif thing == 'ecomm-dev':
       tk=subprocess.check_output( 'aws ec2 describe-instances --output text --profile=ecomm-dev --query "Reservations[*].Instances[*].[PrivateIpAddress,InstanceId,State.Name,Tags[0].Value]"', shell=True, stderr=subprocess.STDOUT )
       message.reply(tk)


    elif thing == 'ecomm-qa':
       tk=subprocess.check_output( 'aws ec2 describe-instances --output text --profile=ecomm-qa --query "Reservations[*].Instances[*].[PrivateIpAddress,InstanceId,State.Name,Tags[0].Value]"', shell=True, stderr=subprocess.STDOUT )
       message.reply(tk)

@listen_to('Can someone help me?')
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')

    # Message is sent on the channel
    message.send('I can help everybody!')

    # Start a thread on the original message
    message.reply("Here's a threaded reply", in_thread=True)
