from pydantic import BaseModel

from typing import List


class ReadersResponse(BaseModel):
    identifier: str
    language: str
    name: str
    arabic_name: str
    english_name: str
    format: str
    type: str
    surahs_sounds: List[str] = []

    class Config:
        from_attributes = True
