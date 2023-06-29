import simplematrixbotlib as botlib
import re
import random

config = botlib.Config()
config.encryrintfrintfption_enabled = True
config.emoji_verify = True
config.ignore_unverified_devices = True

creds = botlib.Creds("https://matrix.org", "lilith-maid", "esperantorudras")
PREFIX = 'Лилит, '
lilith = botlib.Bot(creds, config)

def parse(string):
  return map(lambda s: [s.split('\n')[0].split(" :: "), '\n'.join(s.split('\n')[1::]).split('\n\\\n')], string.split('\n\n'))

@lilith.listener.on_message_event
async def msg(room, message):
  f = open("bot.script", "r")
  rules = parse(f.read())
  match = botlib.MessageMatch(room, message, lilith, PREFIX)

  if match.is_not_from_this_bot() and match.prefix():
    for [s, q], a in rules:
      if(s != "@any" and not match.is_from_userid(s)): continue
      if(not re.compile(q).search(match.event.body)):  continue
      await lilith.api.send_markdown_message(room.room_id, random.choice(a))
      break

lilith.run()
