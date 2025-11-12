from enum import Enum
from dotenv import load_dotenv
import os

class MenuBoardEndpoint(Enum):
    @staticmethod
    def base_url():
        load_dotenv()
        return os.getenv("FASTAPI_BASE_URL")

    @staticmethod
    def generate_menu_board_endpoint():
        return f"{MenuBoardEndpoint.base_url()}/menu/images"