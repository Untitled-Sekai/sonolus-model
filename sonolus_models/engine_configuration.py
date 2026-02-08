"""エンジン設定関連のモデル定義"""
from pydantic import BaseModel
from typing import Optional, List, Literal, Union
from .common import Text


class EngineConfigurationSliderOption(BaseModel):
    """スライダーオプション"""
    name: Text
    description: Optional[str] = None
    standard: Optional[bool] = None
    advanced: Optional[bool] = None
    scope: Optional[str] = None
    type: Literal['slider'] = 'slider'
    def_: float
    min: float
    max: float
    step: float
    unit: Optional[Text] = None


class EngineConfigurationToggleOption(BaseModel):
    """トグルオプション"""
    name: Text
    description: Optional[str] = None
    standard: Optional[bool] = None
    advanced: Optional[bool] = None
    scope: Optional[str] = None
    type: Literal['toggle'] = 'toggle'
    def_: Literal[0, 1]


class EngineConfigurationSelectOption(BaseModel):
    """セレクトオプション"""
    name: Text
    description: Optional[str] = None
    standard: Optional[bool] = None
    advanced: Optional[bool] = None
    scope: Optional[str] = None
    type: Literal['select'] = 'select'
    def_: int
    values: List[Text]


# Union型定義
from typing import Union
EngineConfigurationOption = Union[
    EngineConfigurationSliderOption,
    EngineConfigurationToggleOption,
    EngineConfigurationSelectOption
]


class EngineConfigurationUI(BaseModel):
    """エンジン設定UI"""
    scope: str
    primaryMetric: str
    secondaryMetric: str
    menuVisibility: dict  # より詳細な型定義が必要な場合は追加
    judgmentErrorStyle: str
    judgmentErrorPlacement: str
    judgmentErrorMin: float


class EngineConfiguration(BaseModel):
    """エンジン設定
    type EngineConfiguration = {
        options: EngineConfigurationOption[]
        ui: EngineConfigurationUI
        replayFallbackOptionNames?: (Text | (string & {}))[]
    }
    """
    options: List[EngineConfigurationOption]
    ui: EngineConfigurationUI
    replayFallbackOptionNames: Optional[List[Text]] = None
