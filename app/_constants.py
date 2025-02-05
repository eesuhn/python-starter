import os

from dotenv import load_dotenv

from .utils import print_error


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    print_error("API key not found")
