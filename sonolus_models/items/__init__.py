from pydantic import BaseModel
from typing import Optional, List
from ..base import SonolusResourceLocator
from ..common import Tag
from enum import Enum


SRL = SonolusResourceLocator

class LocalationText(BaseModel):
    ja: Optional[str] = None
    en: Optional[str] = None
    zh: Optional[str] = None

class BaseItem(BaseModel):
    """全てのアイテムの基底クラス"""
    name: str
    source: Optional[str] = None
    title: str
    author: str
    tags: List[Tag] = []

class PackBaseItem(BaseItem):
    """パック内の全てのアイテムの基底クラス"""
    name: str
    source: Optional[SRL] = None
    title: LocalationText
    author: LocalationText
    tags: List[Tag] = []

class ItemType(str, Enum):
    """ItemType定義
    type ItemType = 'post' | 'playlist' | 'level' | 'skin' | 'background' 
                  | 'effect' | 'particle' | 'engine' | 'replay' | 'room' | 'user'
    """
    post = "posts"
    playlist = "playlists"
    level = "levels"
    skin = "skins"
    background = "backgrounds"
    effect = "effects"
    particle = "particles"
    engine = "engines"
    replay = "replays"
    room = "rooms"
    user = "users"
    
__all__ = [
    "BaseItem",
    "PackBaseItem",
    "ItemType",
    "LevelItem",
    "SkinItem",
    "EngineItem",
    "BackgroundItem",
    "EffectItem",
    "ParticleItem",
    "PostItem",
    "ReplayItem",
    "PlaylistItem",
    "RoomItem",
    "UserItem",
]

from .background import BackgroundItem
from .effect import EffectItem
from .engine import EngineItem
from .level import LevelItem
from .particle import ParticleItem
from .post import PostItem
from .replay import ReplayItem
from .skin import SkinItem
from .playlist import PlaylistItem
from .room import RoomItem
from .user import UserItem