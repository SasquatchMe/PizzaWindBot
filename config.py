import os
import dotenv

dotenv.load_dotenv()
*** = os.getenv('***')


DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASS = os.getenv('DATABASE_PASS')
DATABASE_NAME = os.getenv('DATABASE_NAME')

DATABASE_URL = f'postgresql+asyncpg://{DATABASE_USERNAME}:{DATABASE_PASS}@localhost/{DATABASE_NAME}'


print(DATABASE_URL)