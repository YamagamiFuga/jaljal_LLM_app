from pydantic import BaseModel

class MessageResponseBody(BaseModel):
    """
    対話内容からジャルジャル動画を返却するデータモデル
    """
    
    data:dict
    description:str
    