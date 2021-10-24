# getDiscMessage.py: gets the most recent discord message's content and sends the braille's binary representation to serial
# referenced code: https://www.youtube.com/watch?v=xh28F6f-Cds

import requests
import json
import time
import toBraille as tm
import serial
import discordConstants as dc

content = ""

# initialization of the serial
ser = serial.Serial('COM3', 9600) # change 'COM3' and 9600 to match your port and baud

# gets the most recent message's content in given discord channel
# channelid: string of discord channel's id to be read from / written to
# content: the previously read message's content
# output: the message's content
def retrieve_messages(channelid, content):
    headers = {'authorization': dc.authorization}
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)

    # check if the most recent content has changed
    if jsonn[0]['content'] != content:
        content = jsonn[0]['content']
        time.sleep(3)
        str = content
        # convert string to binary representation of braille matrix
        temp = tm.stringToBinary(str)
        # sends string of 1s and 0s to serial one by one
        # can later change to send a base 8 value instead of binary to decrease amount sent
        for x in range(len(temp)):
            num = temp[x]
            ser.write(num.encode())
        return content

# infinite loop getting retrieving most recent message
while True:
    content = retrieve_messages(dc.channel, content)
    