from dotenv import load_dotenv
import os

load_dotenv()

class Environment:
    def __init__(self):
        return
    
    def get_env(self, variable):
        return os.environ[f"{variable}"]