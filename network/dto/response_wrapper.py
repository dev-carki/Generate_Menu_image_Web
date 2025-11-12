from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from datetime import datetime

T = TypeVar("T")

class BaseResponseWrapper(BaseModel, Generic[T]):
    code: int
    message: str
    data: Optional[T]
