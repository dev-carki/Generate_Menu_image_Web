from pydantic import BaseModel
from datetime import datetime

from domain.output.menu_image import MenuImage

class GenerateMenuBoardResponseDTO(BaseModel):
    id: str
    image_url: str
    created_at: datetime

    def to_domain(self):
        return MenuImage(
            menu_id=self.id,
            image_url=self.image_url,
            created_date=self.created_at
        )
