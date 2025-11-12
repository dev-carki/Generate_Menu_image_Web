from datetime import datetime

class MenuImage:
    def __init__(self, menu_id: str, image_url: str, created_date: datetime):
        self.menu_id = menu_id
        self.image_url = image_url
        self.created_date = created_date

    def __repr__(self):
        return f"<MenuImage {self.menu_id} | {self.image_url}>"
