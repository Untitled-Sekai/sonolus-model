from pydantic import BaseModel
from typing import Optional, List
from ..base import SonolusResourceLocator
from ..common import Tag
from ..items import BaseItem, PackBaseItem
from ..items import LocalationText
from .user import UserItem

SRL = SonolusResourceLocator

class ParticleItem(BaseItem):
    """ParticleItemはパーティクルの情報を提供"""
    version: int = 3
    subtitle: str
    authorUser: Optional[UserItem] = None
    thumbnail: SRL
    data: SRL
    texture: SRL

class ParticlePackItem(PackBaseItem):
    """ParticlePackItemはパック内のパーティクルの情報を提供"""
    version: int = 3
    subtitle: LocalationText
    thumbnail: SRL
    data: SRL
    texture: SRL