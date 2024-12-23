from pydantic import BaseModel

class MessageRequestBody(BaseModel):
    """
    おすすめジャルジャル動画をリクエストするデータモデル
    """
    
    role:str
    message:str
    description:str