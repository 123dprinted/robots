from disnake.ext import commands
from dotenv import load_dotenv

import disnake
import os
import db

load_dotenv()

intents = disnake.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

TOKEN = os.getenv("TOKEN")
BATCH_SIZE = 100
ADMIN_USER_IDS = [726087545867468820]



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def ep(ctx): # Scrape, name obfuscated
    if ctx.author.id in ADMIN_USER_IDS[0]:
        async for message in ctx.channel.history(oldest_first = True, limit = 100000):
            annotated_message: disnake.Message = message # Makes it easy to use methods because the IDE knows the type of the variable
            ref = annotated_message.reference.message_id if annotated_message.reference else None

            db.add_message(annotated_message.id, annotated_message.author.id, annotated_message.channel.id, ref, annotated_message.content, annotated_message.created_at.isoformat())

        db.commit()
    else:
        await ctx.send("pen")


if __name__ == '__main__':
    client.run(TOKEN)
    db.close()