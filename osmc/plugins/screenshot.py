# coding=utf8
import os,time,glob,re
import subprocess
from subprocess import Popen, PIPE
from slackbot.bot import respond_to
from slackbot.utils import download_file, create_tmp_file


@respond_to(r'upload \<?(.*)\>?',re.IGNORECASE)
def upload(message, thing):
    # message.channel.upload_file(slack_filename, local_filename,
    #                             initial_comment='')
    if thing == 'favicon':
        url = 'https://slack.com/favicon.ico'
        message.reply('uploading {}'.format(url))
        with create_tmp_file() as tmpf:
            download_file(url, tmpf)
            message.channel.upload_file(url, tmpf,
                                        'downloaded from {}'.format(url))
    elif thing == 'screenshot.png':
         message.reply('uploading screenshot.png')
         cwd = os.path.abspath(os.path.dirname(__file__))
#         fname = os.path.join('/home/osmc/slack/screenshot001.png')
#         subprocess.check_call(["kodi-send", "--action=TakeScreenshot"])
         Popen(["kodi-send", "--action=TakeScreenshot"], stdout=PIPE, stderr=PIPE)
         time.sleep(3)
         fname = max(glob.iglob('/home/osmc/slack/screen*.png'), key=os.path.getctime)
         message.channel.upload_file(thing, fname)

    elif thing == 'slack.png':
        message.reply('uploading slack.png')
        cwd = os.path.abspath(os.path.dirname(__file__))
        fname = os.path.join(cwd, '../../tests/functional/slack.png')
        message.channel.upload_file(thing, fname)


@respond_to('send_string_content')
def upload_content(message):
    # message.channel.upload_content(slack_filename, content,
    #                                initial_comment='')
    content=u"你好! here's some data\nthat will appear\nas a plain text snippet"
    message.channel.upload_content('content.txt', content)
