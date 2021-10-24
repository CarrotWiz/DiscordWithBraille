# sendDiscMessage.py: sends a message in a discord server with a discord account

import requests
import discordConstants as dc

header = {'authorization': dc.authorization}

# sends a message to a given discord channel
# channelid: string of discord channel's id to be written to
# message: the string to be sent
def send_message(channelid, message):
    r = requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', data = {'content': message}, headers = header)
