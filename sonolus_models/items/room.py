from pydantic import BaseModel
from typing import Optional, List
from ..base import SonolusResourceLocator
from ..common import Tag
from .user import UserItem

SRL = SonolusResourceLocator


class RoomItem(BaseModel):
    """RoomItemはルーム情報を提供
    type RoomItem = {
        name: string
        title: string
        subtitle: string
        master: string
        masterUser?: UserItem
        tags: Tag[]
        cover?: Srl
        bgm?: Srl
        preview?: Srl
    }
    """
    name: str
    title: str
    subtitle: str
    master: str
    masterUser: Optional[UserItem] = None
    tags: List[Tag] = []
    cover: Optional[SRL] = None
    bgm: Optional[SRL] = None
    preview: Optional[SRL] = None
