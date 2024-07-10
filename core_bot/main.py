from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from datetime import datetime as DT

from environs import Env

from gpt_handler import get_comment

env = Env()
env.read_env()
API_ID = env.str("API_ID")
API_HASH = env.str("API_HASH")
TARGET = int(env.str("CHAT_ID"))


print(f"Start App {DT.now()}")
client = Client(name='.data/john_smith', api_id=API_ID, api_hash=API_HASH)


@client.on_message(filters.chat(TARGET))
async def all_messages(client: Client, message: Message):
	print(message.id)
	m = await client.get_discussion_message(TARGET, message.id)
	print(m.text)
	answer = await get_comment(m.text)
	await m.reply(answer)

# client.add_handler(MessageHandler(all_messages, filters.chat(CHAT_ID)))
# client.start()

# client.run()

if __name__ == '__main__':
	client.run()
