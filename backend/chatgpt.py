from typing import List
import json
from dotenv import load_dotenv
from openai import OpenAI
from request import MessageRequestBody
import re
load_dotenv()
client = OpenAI()


def recomend_response(Requests: List[MessageRequestBody]):
    """
    おすすめジャルジャル動画を提案するアシスタント機能
    """
    
    with open('description.txt', 'r', encoding='utf-8') as f:
        prompt_txt = f.read()
    
        
    messages = [
        {"role": request.role, "content": request.message} for request in Requests
    ]
    
    messages.insert(
        0,
        {
            "role": "system",
            "content": prompt_txt,
        },
    )
    Description_response = client.chat.completions.create(
        model="gpt-4o", messages=messages
    )
    
    return Description_response.choices[0].message.content


def clean_description(description_jaljal):
    """
    不要な文字を削除する
    """

    # \nの文字削除
    description_jaljal1 = description_jaljal.replace("\n", "")
    
    description_jaljal2 = description_jaljal1.replace("*", "")
    
    description_jaljal3 = description_jaljal2.replace("-", "")
    
    description_jaljal4 = description_jaljal3.replace("#", "")
    
    return description_jaljal4
    
def get_url(cleaned_description):
    """
    cleaned_descriptionから動画のURLだけを取得する
    """
    with open('url.txt', 'r', encoding = 'utf-8') as f1:
        url_txt = f1.read()
        
    url_response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": url_txt
            },
            {"role": "system", "content": cleaned_description},
        ],
    )
    return url_response.choices[0].message.content

def true_get_url(got_url):
    """
    辞書型に変換して返す
    """
    change_url = got_url
    
    if isinstance(change_url, str): 
        true_url = json.loads(change_url)
        
    return true_url

def description_change(cleaned_description):
    """
    説明文のURLを削除する
    """
    description_url = re.sub(r"https?://[^\s]+", "", cleaned_description)
    #https?://[^\s]+
    #https?: httpまたはhttpsにマッチ
    #://: コロンとスラッシュ（://）にマッチ
    #[^\s]+: 空白文字以外が1つ以上続く部分（URLの残り）にマッチ
    
    #re.sub関数:
    #第1引数: URLパターン
    #第2引数: 削除後に置き換える内容（今回は空文字列""）
    #第3引数: 処理対象のテキスト
    
    return description_url