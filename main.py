from common.custom_page import PageContents, CustomPage

page_contents = [
    PageContents(file_dir="pages/generate_menu_image_page.py", 
                 page_title_label="메뉴판 만들기 페이지", 
                 icon="🔥")
]

CustomPage.create_normal_page(page_contents)