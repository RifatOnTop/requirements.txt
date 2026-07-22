from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Courses"),
            KeyboardButton(text="💳 Payment")
        ],
        [
            KeyboardButton(text="📷 Verify Payment"),
            KeyboardButton(text="👤 Profile")
        ],
        [
            KeyboardButton(text="📢 Notice"),
            KeyboardButton(text="☎️ Support")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="একটি অপশন নির্বাচন করুন..."
)
