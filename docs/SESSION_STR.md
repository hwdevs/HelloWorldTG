<h1 align="center">Session String</h1>
Session String adalah session yang berbentuk text seperti token yang sangat panjang, kelebihan session string adalah tidak perlu menambahkan parameter api_id, api_hash, bot_token. Jadi tidak perlu membuat .session file ke dalam work root directory, memakai session string adalah sangat direkomendasikan. Cara membuat session string seperti di bawah ini:
<br>
<br>

```python
from pyrogram import Client

with Client(
    "YourSessionName",
    api_id=123131,
    api_hash="AdnackwjdAWOIjad",
    bot_token="12313:wadajscnawid",
    in_memory=True
) as bot:
    # pastikan start botnya dulu, karena bot akan mengirim
    # session stringnya ke pm kamu
    bot.send_message("@your_username", bot.export_session_string())
```

Jika sudah maka selanjutnya kamu hanya menjalankan botnya hanya dengan:

```python
from pyrogram import Client

bot = Client(
    "YourSessionName",
    session_string="place exported session str here",
    in_memory=True
)

if __name__ == "__main__":
    bot.run()
```

Punya pertanyaan, tutorial di atas kurang jelas, atau ga bekerja sesuai ekspektasi?
### Join us
<a href="https://t.me/Hello_World_OC" target="_blank">
        <img src="https://img.shields.io/badge/Telegram-3f5ed8.svg?&?style=social&logo=telegram&color=blue" alt="Telegram"/>
</a>