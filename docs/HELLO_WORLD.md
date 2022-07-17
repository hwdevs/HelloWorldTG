<h1 align="center">Hello World</h1>
Membuat program pertamamu hanya dengan hitungan detik saja<br>Dapatkan API ID dan API Hash di <a href="https://my.telegram.org/apps">Official Telegram Apps</a> dan Bot Token di <a href="https://t.me/botfather">Bot Father</a>.
<br>
<br>

```python
from pyrogram import Client, filters
from pyrogram.types import Message

bot = Client(
    "kiizu@HelloWorld",
    api_id=1231231, # Your API ID
    api_hash="Your API Hash",
    bot_token="Your bot token"
)

@bot.on_message(
	filters.command(["start"]) &
	filters.private
)
async def on_start(_, m: Message):
	await m.reply(f"Hello {m.from_user.mention}!")

if __name__ == "__main__":
    bot.run()
```

Apa itu filters? kamu bisa melihatnya [di sini](FILTERS.md).<br>
Punya pertanyaan, tutorial di atas kurang jelas, atau ga bekerja sesuai ekspektasi?

### Join us
<a href="https://t.me/Hello_World_OC" target="_blank">
        <img src="https://img.shields.io/badge/Telegram-3f5ed8.svg?&?style=social&logo=telegram&color=blue" alt="Telegram"/>
</a>