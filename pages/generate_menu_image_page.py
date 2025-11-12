import asyncio

import streamlit as st

from widgets.custom_title import show_normal_title
from widgets.custom_text_input import show_normal_text_input
from widgets.custom_text_area import show_normal_text_area
from widgets.custom_button import show_normal_button

from network.services.menu_board.menu_board_network_service import MenuBoardNetworkService

from domain.input.menu_board_input import MenuBoardInput

show_normal_title("메뉴판 이미지 생성 페이지")

prompt = show_normal_text_area(title_label="프롬프트 작성", placeholder_label="중식 뭐시기...")

style = show_normal_text_input(title_label="스타일 작성", placeholder_label="화사한 분위기")

if show_normal_button(label="API 요청 버튼"):
    response = asyncio.run(MenuBoardNetworkService.generate_menu_board(MenuBoardInput(prompt=prompt, style=style)))

    show_normal_title(f"이미지 ID: {response.menu_id}")
    st.image(response.image_url)
    show_normal_title(f"이미지 생성 날짜: {response.created_date}")
