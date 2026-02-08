# ここでベースとなるモデルの定義

from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any, Union, Literal
from enum import Enum
from .ServerOption import ServerOption
from .text import SonolusText
from .icon import SonolusIcon

class SonolusResourceLocator(BaseModel):
    # https://wiki.sonolus.com/ja/custom-server-specs/misc/srl
    # type Srl = { hash?: string | null, url?: string | null }
    model_config = {"exclude_none": True}
    
    hash: Optional[str] = None
    url: Optional[str] = None

# エイリアス
Srl = SonolusResourceLocator


class SonolusItemButtonType(str, Enum):
    # ServerInfoItemButtonで使用可能なtype
    ROOM = "room"
    POST = "post"
    PLAYLIST = "playlist"
    LEVEL = "level"
    REPLAY = "replay"
    SKIN = "skin"
    BACKGROUND = "background"
    EFFECT = "effect"
    PARTICLE = "particle"
    ENGINE = "engine"
    USER = "user"
    CONFIGURATION = "configuration"


class ServerInfoAuthenticationButton(BaseModel):
    # 認証ボタン
    type: Literal["authentication"]


class ServerInfoItemButton(BaseModel):
    # アイテムボタン
    model_config = {"exclude_none": True}
    
    type: SonolusItemButtonType
    title: Optional[Union[SonolusText, str]] = None
    icon: Optional[Union[SonolusIcon, str]] = None
    badgeCount: Optional[int] = None
    infoType: Optional[str] = None
    itemName: Optional[str] = None


class ServerInfoConfigurationButton(BaseModel):
    # 設定ボタン
    type: Literal["configuration"]

    
# ボタンの定義（Union型）
SonolusButton = Union[
    ServerInfoAuthenticationButton,
    ServerInfoItemButton,
    ServerInfoConfigurationButton
]

    
class SonolusConfiguration(BaseModel):
    # サーバーの設定の情報
    options: List[ServerOption] = Field(default_factory=list)

    
class SonolusServerInfo(BaseModel):
    # サーバーの情報を定義
    # Sonolusのサーバーに入ったときの最初のメニュー
    model_config = {"exclude_none": True}
    
    title: str
    description: Optional[str] = None
    buttons: List[SonolusButton] = Field(default_factory=list)
    configuration: SonolusConfiguration = Field(default_factory=SonolusConfiguration)
    banner: Optional[SonolusResourceLocator] = None