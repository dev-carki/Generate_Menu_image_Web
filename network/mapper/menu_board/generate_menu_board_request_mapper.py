# mappers/menu_board_mapper.py
from domain.input.menu_board_input import MenuBoardInput
from network.dto.request_dto.menu_board.generate_menu_board_request_dto import GenerateMenuBoardRequestDTO

class MenuBoardMapper:
    @staticmethod
    def to_request_dto(domain_model: MenuBoardInput) -> GenerateMenuBoardRequestDTO:
        return GenerateMenuBoardRequestDTO(
            prompt=domain_model.prompt,
            style=domain_model.style
        )
