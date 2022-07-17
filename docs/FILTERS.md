<h1 align="center">Filters</h1>
Filters adalah untuk menyaring pesan masuk yang akan diterima sehingga
pesan masuk hanya akan menerima pesan yang telah difilters saja, mereka
akan mengabaikan pesan yang tidak difilter.
<br>
<br>

<details>
<summary><code>filters.command()</code></summary>
&nbsp;&nbsp;&nbsp; Filter ini untuk menyaring pesan slash command atau pesan perintah, namun filter ini bisa juga diubah prefixnya menjadi seperti .start, !start, $start, tetapi defaultnya adalah (/), sebagai contoh.
<br>
<br>

```python
from pyrogram import Client, filters
from pyrogram.types import Message

bot = Client(
    "YourSession",
    api_id=123124,
    api_hash="ADaskcAWKdjaoiDjaawid",
    bot_token="1231312:abccsaiddjwi"
)

@bot.on_message(filters.command("start"))
async def on_start_cmd(_, m: Message):
    await m.reply(f"Halo kamu {m.from_user.mention}")

if __name__ == "__main__":
    bot.run()
```
</details>

<details>
<summary><code>filters.private</code></summary>
&nbsp;&nbsp;&nbsp; Filter ini untuk menyaring pesan private seperti personal chat dan tidak akan menerima pesan dari grup ataupun yang lain.
<br>
<br>

```python
from pyrogram import Client, filters
from pyrogram.types import Message

bot = Client(
    "YourSession",
    api_id=123124,
    api_hash="ADaskcAWKdjaoiDjaawid",
    bot_token="1231312:abccsaiddjwi"
)

@bot.on_message(
    filters.command("start") &
    filters.private
)
async def on_start_cmd(_, m: Message):
    await m.reply(f"Halo kamu {m.from_user.mention}")

if __name__ == "__main__":
    bot.run()
```
</details>

Kalian bisa melihat versi lengkap `filters` pada official dokumentasi [Pyrogram's Filters](https://docs.pyrogram.org/api/filters "Dokumentasi terbaik versi saya hehe.")