from pydantic import BaseModel


class AutoCompleteModel(BaseModel):
    phrase: str


class ChatModel(BaseModel):
    message: str


class ChatResponseModel(BaseModel):
    assistant: str


class TranslationModel(AutoCompleteModel):
    pass
