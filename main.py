#  HelloWorldTG - The example use of Pyrogram library and for learning
#  Copyright (C) 2022 HelloWorld <https://github.com/hwdevs>
#
#  This file is part of HelloWorldTG.
#
#  HelloWorldTG is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  HelloWorldTG is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with HelloWorldTG.  If not, see <http://www.gnu.org/licenses/>.


from pyrogram import Client
from dotenv import load_dotenv
import os

load_dotenv()

bot = Client(
    "kiizu@HelloWorld",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN"),
    plugins=dict(
        root="helloworld.plugins"
    )
)

if __name__ == "__main__":
    bot.run()
