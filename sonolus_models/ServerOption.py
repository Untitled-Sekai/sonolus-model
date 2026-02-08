from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Union, Literal
from enum import Enum
from .common import Text, Sil, Icon

class SelectValue(BaseModel):
    """セレクト/マルチオプションの値"""
    name: str
    title: Text

class ServerOptionBase(BaseModel):
    """全てのServerOptionの基底クラス"""
    query: str
    name: Text
    description: Optional[str] = None
    required: bool

class ServerTextOption(ServerOptionBase):
    """テキスト入力オプション"""
    type: Literal["text"] = "text"
    def_: str = Field(alias="def")  # Pythonの予約語を回避
    placeholder: Text
    limit: int
    shortcuts: List[str]
    class Config:
        populate_by_name = True

class ServerTextAreaOption(ServerOptionBase):
    """テキストエリア入力オプション"""
    type: Literal["textArea"] = "textArea"
    def_: str = Field(alias="def")
    placeholder: Text
    limit: int
    shortcuts: List[str]
    class Config:
        populate_by_name = True

class ServerSliderOption(ServerOptionBase):
    """スライダー入力オプション"""
    type: Literal["slider"] = "slider"
    def_: float = Field(alias="def")
    min: float
    max: float
    step: float
    unit: Optional[Text] = None
    class Config:
        populate_by_name = True

class ServerToggleOption(ServerOptionBase):
    """トグル（ON/OFF）オプション"""
    type: Literal["toggle"] = "toggle"
    def_: bool = Field(alias="def")
    class Config:
        populate_by_name = True

class ServerSelectOption(ServerOptionBase):
    """セレクト（単一選択）オプション"""
    type: Literal["select"] = "select"
    def_: str = Field(alias="def")
    values: List[SelectValue]
    class Config:
        populate_by_name = True

class ServerMultiOption(ServerOptionBase):
    """マルチ（複数選択）オプション"""
    type: Literal["multi"] = "multi"
    def_: List[bool] = Field(alias="def")
    values: List[SelectValue]
    class Config:
        populate_by_name = True

class ServerServerItemOption(ServerOptionBase):
    """サーバーアイテム（単一）オプション"""
    type: Literal["serverItem"] = "serverItem"
    item_type: str = Field(alias="itemType")  # ItemType
    info_type: Optional[str] = Field(default=None, alias="infoType")
    def_: Optional[Sil] = Field(alias="def")
    allow_other_servers: bool = Field(alias="allowOtherServers")
    class Config:
        populate_by_name = True

class ServerServerItemsOption(ServerOptionBase):
    """サーバーアイテム（複数）オプション"""
    type: Literal["serverItems"] = "serverItems"
    item_type: str = Field(alias="itemType")  # ItemType
    info_type: Optional[str] = Field(default=None, alias="infoType")
    def_: List[Sil] = Field(alias="def")
    allow_other_servers: bool = Field(alias="allowOtherServers")
    limit: int
    class Config:
        populate_by_name = True

class ServerCollectionItemOption(ServerOptionBase):
    """コレクションアイテムオプション"""
    type: Literal["collectionItem"] = "collectionItem"
    item_type: str = Field(alias="itemType")  # ItemType
    class Config:
        populate_by_name = True

# ServerFileOptionのValidation型定義
class ServerFileOptionValidationBase(BaseModel):
    """ファイルバリデーションの基底クラス"""
    minSize: Optional[int] = None
    maxSize: Optional[int] = None

class ServerFileOptionValidationFile(ServerFileOptionValidationBase):
    type: Literal['file', 'engineRom']

class ServerFileOptionValidationImage(ServerFileOptionValidationBase):
    type: Literal[
        'image', 'serverBanner', 'postThumbnail', 'playlistThumbnail',
        'levelCover', 'skinThumbnail', 'skinTexture', 'backgroundThumbnail',
        'backgroundImage', 'effectThumbnail', 'particleThumbnail',
        'particleTexture', 'engineThumbnail', 'roomCover'
    ]
    minWidth: Optional[int] = None
    maxWidth: Optional[int] = None
    minHeight: Optional[int] = None
    maxHeight: Optional[int] = None

class ServerFileOptionValidationAudio(ServerFileOptionValidationBase):
    type: Literal['audio', 'levelBgm', 'levelPreview', 'roomBgm', 'roomPreview']
    minLength: Optional[float] = None
    maxLength: Optional[float] = None

class ServerFileOptionValidationZip(ServerFileOptionValidationBase):
    type: Literal['zip', 'effectAudio']

class ServerFileOptionValidationJson(ServerFileOptionValidationBase):
    type: Literal[
        'levelData', 'skinData', 'backgroundData', 'backgroundConfiguration',
        'effectData', 'particleData', 'enginePlayData', 'engineWatchData',
        'enginePreviewData', 'engineTutorialData', 'engineConfiguration',
        'replayData', 'replayConfiguration'
    ]

ServerFileOptionValidation = Union[
    ServerFileOptionValidationFile,
    ServerFileOptionValidationImage,
    ServerFileOptionValidationAudio,
    ServerFileOptionValidationZip,
    ServerFileOptionValidationJson
]

class ServerFileOption(ServerOptionBase):
    """ファイルオプション"""
    type: Literal["file"] = "file"
    def_: str = Field(alias="def")
    validation: Optional[ServerFileOptionValidation] = None
    class Config:
        populate_by_name = True
        
# Union型でServerOptionを定義
ServerOption = Union[
    ServerTextOption,
    ServerTextAreaOption,
    ServerSliderOption,
    ServerToggleOption,
    ServerSelectOption,
    ServerMultiOption,
    ServerServerItemOption,
    ServerServerItemsOption,
    ServerCollectionItemOption,
    ServerFileOption
]

class ServerForm(BaseModel):
    """サーバーフォームの定義"""
    type: str
    title: Text
    icon: Optional[Icon] = None
    description: Optional[str] = None
    help: Optional[str] = None
    require_confirmation: bool = Field(alias="requireConfirmation")
    options: List[ServerOption]
    
    class Config:
        populate_by_name = True
