import inspect
from pydantic import TypeAdapter

from network.endpoints.menu_board_endpoint import MenuBoardEndpoint
from network.services.base_network_service import base_network_service
from network.dto.response_wrapper import BaseResponseWrapper
from network.dto.response_dto.menu_board.generate_menu_board_response_dto import GenerateMenuBoardResponseDTO

from network.mapper.menu_board.generate_menu_board_request_mapper import MenuBoardMapper

from domain.output.menu_image import MenuImage
from domain.input.menu_board_input import MenuBoardInput

class MenuBoardNetworkService():
    @staticmethod
    async def generate_menu_board(request_body: MenuBoardInput, method="POST") -> MenuImage:
        request_url = MenuBoardEndpoint.generate_menu_board_endpoint()
        
        print(f"🟢 [DEV - Streamlit] {inspect.currentframe().f_code.co_name} 요청 url: {method}: {request_url}")
        dto = MenuBoardMapper.to_request_dto(request_body)
        
        response = await base_network_service(url=request_url, method=method, body=dto.model_dump())
        
        wrapper_adapter = TypeAdapter(BaseResponseWrapper[GenerateMenuBoardResponseDTO])
        parsed = wrapper_adapter.validate_python(response)
        
        print(f"🟢 [DEV - Streamlit] Parsed Response Data: {parsed}")
        print(f"🟢 [DEV - Streamlit] Parsed Response Data Type: {type(parsed)}")
        
        result = parsed.data.to_domain()
        
        print(f"🟢 [DEV - Streamlit] Return Data: {result}")
        print(f"🟢 [DEV - Streamlit] Return Data Type: {type(result)}")
        
        return result