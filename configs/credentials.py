"""TEST CREDENTIALS"""
from dotenv import load_dotenv
import os

path = load_dotenv()

USER_NAME = os.getenv("USER_NAME")
USER_PWD = os.getenv("USER_PWD")
NOT_REGISTERED_USER = "SomeOne"
LOGIN_ERROR_MSG = "There was a problem"
