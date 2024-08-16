from db.models.models import init_db, AsyncSessionLocal, User
import asyncio


async def main():
    await init_db()
    async with AsyncSessionLocal() as s:
        new_user = User(name='example')
        s.add(new_user)
        await s.commit()


if __name__ == '__main__':
    asyncio.run(main())
