import time
import json
import telepot
import random
import schedule
import wikiquote
from telepot.loop import MessageLoop
from difflib import get_close_matches

bot=telepot.Bot("Telegram key")
knowledge =json.load(open('knowledge.json'))

greeting = ['hi', 'hello', 'niaje', 'mambo']
sending  = ['nitumie', 'send me ', 'send', 'tuma']
define = ['define', 'maana', 'meaning']
picture = ['picha', 'picture', 'pic']
audio = ['audio', 'mp3', 'music']
video = ['video', 'movie']