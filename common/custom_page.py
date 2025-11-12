import streamlit as st
from typing import List
from pathlib import Path

class PageContents():
    def __init__(self, file_dir: str | Path, page_title_label, icon):
        self.file_dir = file_dir
        self.page_title_label = page_title_label
        self.icon = icon


class CustomPage:
    @staticmethod
    def create_normal_page(page_contents: List[PageContents]):
        pages = [st.Page(pc.file_dir, title=pc.page_title_label, icon=pc.icon) for pc in page_contents]
        page = st.navigation(pages)
        page.run()