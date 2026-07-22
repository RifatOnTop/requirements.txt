import aiosqlite

DB = "users.db"

async def create_db():
    async with aiosqlite.connect(DB) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            full_name TEXT,
            username TEXT
        )
        """)
        await db.commit()

async def add_user(user_id, full_name, username):
    async with aiosqlite.connect(DB) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users VALUES(?,?,?)",
            (user_id, full_name, username)
        )
        await db.commit()

async def total_users():
    async with aiosqlite.connect(DB) as db:
        cursor = await db.execute("SELECT COUNT(*) FROM users")
        return (await cursor.fetchone())[0]
