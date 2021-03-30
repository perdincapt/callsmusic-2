from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Halo, {message.from_user.first_name}!</b>
Saya bot musik yang di buat untuk mendengarkan lagu di vcg bersama.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner Bot", url="https://t.me/bintankgede"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "INSTAGRAM", url="https://www.instagram.com/perdincapt/"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "CARA PENGGUNAANNYA", url="https://telegra.ph/CARA-PAKAI-BOT-MUSIK-BINTANG-03-30"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "Hai, apakah anda ingin memainkan sebuah lagu?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⭕ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Tidak ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
