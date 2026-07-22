from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards import main_menu
from database import add_user, total_users

router = Router()


@router.message(Command("start"))
async def start(message: Message):

    await add_user(
        message.from_user.id,
        message.from_user.full_name,
        message.from_user.username or "None"
    )

    text = f"""
🎓 <b>HSC Batch 2026 Official Bot</b>

👋 Welcome, <b>{message.from_user.full_name}</b>

━━━━━━━━━━━━━━
📚 Courses
💳 Payment
📷 Verify Payment
👤 Profile
📢 Notice
☎️ Support
━━━━━━━━━━━━━━

নিচের Menu থেকে একটি অপশন নির্বাচন করুন।
"""

    await message.answer(
        text,
        parse_mode="HTML",
        reply_markup=main_menu
    )


@router.message()
async def menu(message: Message):

    if message.text == "📚 Courses":

        await message.answer(
            "📚 এখানে সকল কোর্স দেখানো হবে।"
        )

    elif message.text == "💳 Payment":

        await message.answer(
            "💳 বিকাশ: 01XXXXXXXXX\n"
            "💳 নগদ: 01XXXXXXXXX"
        )

    elif message.text == "👤 Profile":

        count = await total_users()

        await message.answer(
            f"""
👤 Name: {message.from_user.full_name}
🆔 ID: {message.from_user.id}

👥 Total Users: {count}
"""
        )

    elif message.text == "📢 Notice":

        await message.answer(
            "📢 বর্তমানে কোনো Notice নেই।"
        )

    elif message.text == "☎️ Support":

        await message.answer(
            "👨‍💻 Admin: @Rifat_tour"
        )

    elif message.text == "📷 Verify Payment":

        await message.answer(
            "📸 আপনার Payment Screenshot পাঠান।"
        )

    elif message.photo:

        await message.answer(
            "✅ Screenshot Received.\nAdmin খুব দ্রুত Verify করবে।"
        )

    else:

        await message.answer(
            "❌ নিচের Menu ব্যবহার করুন।"
        )
