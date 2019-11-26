from typing import List

from pydantic import BaseModel


class Live(BaseModel):
    pk_live_id:int
    artists: str
    live_name: str
    livehouse: str
    live_url: str
    day: int
    month: int
    year: int
    artists_origin: str
    img_url: str


class GetResponse(BaseModel):
    live_list: List[Live]
