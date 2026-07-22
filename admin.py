from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import ADMIN_ID
from database import total_users

router = Router()


@router.message(Command("users"))
async def users(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    count = await total_users()

    await message.answer(
        f"👥 Total Users: {count}"
    )


@router.message(Command("broadcast"))
async def broadcast(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        "📢 Broadcast System\n\n"
        "এই অংশটি পরবর্তী ধাপে সম্পূর্ণ করা হবে।"
    )
