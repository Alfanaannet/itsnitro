import aiohttp
import os
import io
import json
import re
from discord.ext import commands
from discord import Embed, app_commands
from discord.ext import commands
import re
import aiohttp
import discord
from dotenv import load_dotenv
from flask import Flask
from threading import Thread
import requests
import json
import time
import random
import string

app = Flask('')

@app.route('/')
def main():
  return "Your bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
message_history = {}
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents, heartbeat_timeout=60)
load_dotenv()

# GOOGLE_AI_KEY = os.getenv("GOOGLE_AI_KEY")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DEVELOPER_ID = os.getenv("OWNER")

#CUSTOM_PERSONALITY = os.getenv("CUSTOM_PERSONALITY") --- this shit is disgusting asf and booring old skill for custom personality fuck it and fuck you if u enable it (gonna update it soon & set chatbo)


@bot.event
async def on_ready():
  await bot.tree.sync()
  num_commands = len(bot.commands)
  invite_link = discord.utils.oauth_url(bot.user.id,
                                        permissions=discord.Permissions(),
                                        scopes=("bot",
                                                "applications.commands"))

  def print_in_color(text, color):
    return f"\033[{color}m{text}\033[0m"

 # if os.name == 'posix':
    #os.system('clear')
  #elif os.name == 'nt':
   # os.system('cls')
  print(print_in_color(f"{bot.user} aka {bot.user.name} has connected to Discord!", "\033[1;97"))
  # print(print_in_color(f"  Loaded {num_commands} commands", "1;35"))
  # print(print_in_color(f"      Invite link: {invite_link}", "1;36"))
  keep_alive()
  await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="・💻┆ITS COMMUNITY"))

# Event handler for new messages
@bot.event
async def on_message(message):
  # Ignore messages sent by the bot
  if message.author == bot.user:
    return
 # if isinstance(message.channel, discord.DMChannel) and message.author.id != DEVELOPER_ID:
 #    # await message.author.send("Sorry, I'm currently not accepting direct messages.")
 #   return
  # Check if the bot is mentioned or the message is a DM
   if isinstance(message.channel, discord.DMChannel) and message.author.id != '775012312876711936':
       await split_and_send_messages(message, "Sorry, I'm currently not accepting direct messages.", 1700)
       return
   if bot.user.mentioned_in(message):
    #Start Typing to seem like something happened
    # cleaned_text = clean_discord_message(message.content)

    async with message.channel.typing():
      # Check for image attachments
      if __name__ == "__main__":
        url = 'https://api.discord.gx.games/v1/direct-fulfillment'
        headers = {
            'authority': 'api.discord.gx.games',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://www.opera.com',
            'referer': 'https://www.opera.com/',
            'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
        }

        data = {
            'partnerUserId': generate_random_string(64)
        }

        session = requests.Session()
        
        response = session.post(url, headers=headers, json=data)
        if response.status_code == 200:
          _token = response.json().get('token')
          if _token is not None:
              # Proceed with using the token
            # print(f"Token: {_token}")
            await message.add_reaction("💵")
            response_text = f'https://discord.com/billing/partner-promotions/1180231712274387115/{_token}\n'
            await split_and_send_messages(message, response_text, 1700)
            line ='https://media.discordapp.net/attachments/1072156951049408532/1072632717298114600/standKJrd.gif?ex=65f0cb90&is=65de5690&hm=1088ff9d1b757bd0722df304&'
            await split_and_send_messages(message, line, 1700)
          # with open('codes.txt', 'a') as file:
          #     file.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}\n")
          # print("Token saved to codes.txt file.\n\n")
          # print(f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}\n")
        else:
          eror = 'ERROR FOR GET NITRO'
          await split_and_send_messages(message, eror, 1700)
          # print(f"Request failed with status code {response.status_code}.")
          # print(f"Error message: {response.text}")

                #Split the Message so discord does not get upset
      # await split_and_send_messages(message, response_text, 1700)
      return
      #Not an Image do text response
      # else:
      #   print("New Message FROM:" + str(message.author.id) + ": " +
      #         cleaned_text)
      #   #Check for Keyword Reset
      #   if "RESET" in cleaned_text:
      #     #End back message
      #     if message.author.id in message_history:
      #       await message.channel.send("🤖 History Reset for user: " +
      #                                str(message.author.name))
      #     return
      #   await message.add_reaction(':credit_card:')

        # #Check if history is disabled just send response
        # #Add users question to history
        # update_message_history(message.author.id, cleaned_text)
        # response_text = await generate_response_with_text(
        #     get_formatted_message_history(message.author.id))
        # #add AI response to history
        # update_message_history(message.author.id, response_text)
        # #Split the Message so discord does not get upset
        # await split_and_send_messages(message, response_text, 1700)


#ry-------------------------------------------------

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

# async def generate_response_with_text(message_text):
#   prompt_parts = [message_text]
#   print("Got textPrompt: " + message_text)
#   response = text_model.generate_content(prompt_parts)
#   if (response._error):
#     return "❌" + str("العب بعيد ياسط بالله عليك ميجيش معاك اني بوت لا ده انا سوابق")
#   return response.text

#---------------------------------------------Sending Messages-------------------------------------------------
async def split_and_send_messages(message_system, text, max_length):

  # Split the string into parts
  messages = []
  for i in range(0, len(text), max_length):
    sub_message = text[i:i + max_length]
    messages.append(sub_message)

  # Send each part as a separate message
  for string in messages:
    await message_system.channel.send(string)


def clean_discord_message(input_string):
  # Create a regular expression pattern to match text between < and >
  bracket_pattern = re.compile(r'<[^>]+>')
  # Replace text between brackets with an empty string
  cleaned_content = bracket_pattern.sub('', input_string)
  return cleaned_content


#---------------------------------------------Run Bot-------------------------------------------------

bot.run(DISCORD_BOT_TOKEN)
