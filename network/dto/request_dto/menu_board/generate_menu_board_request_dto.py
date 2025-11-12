# dto/request/menu_board_request.py
from pydantic import BaseModel

class GenerateMenuBoardRequestDTO(BaseModel):
    prompt: str
    style: str
