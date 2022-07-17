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
from pyrogram.types import CallbackQuery

# Contoh 1 menggunakan custom filter

async def alert(_, __, cb: CallbackQuery):
    return cb.data == "alert"
alert_filter = filters.create(alert)

@Client.on_callback_query(alert_filter)
async def alert_cb(_, cb: CallbackQuery):
    await cb.answer("Halo, ini adalah pesan alert", show_alert=True)


# Contoh 2 tidak menggunakan filter, melainkan menggunakan if

@Client.on_callback_query()
async def alert_cb_2(_, cb: CallbackQuery):
    if cb.data == "alert_2":
        await cb.answer("Halo, ini adalah pesan alert", show_alert=True)
