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


from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.command("start") &
    filters.private
)
async def on_start(_, m: Message):
    await m.reply(f"Halo kamu {m.from_user.mention}")
