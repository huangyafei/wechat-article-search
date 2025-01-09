from miku_ai import get_wexin_article
from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader, APIKey
from typing import List, Dict
import asyncio
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 从环境变量获取 API key
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("未设置 API_KEY 环境变量")

app = FastAPI(
    title="微信文章搜索 API",
    description="搜索微信公众号文章的 API 服务"
)

# 添加 API key 配置
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=True)

# 添加 API key 验证函数
async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    raise HTTPException(
        status_code=403,
        detail="无效的 API key"
    )

@app.get("/search/", response_model=List[Dict])
async def search_articles(
    query: str, 
    top_num: int = 10,
    api_key: APIKey = Depends(get_api_key)
):
    """
    搜索微信公众号文章
    
    - **query**: 搜索关键词
    - **top_num**: 返回结果数量，默认为10条（实际返回数量可能小于此值）
    """
    print(f"收到请求 - query: {query}, top_num: {top_num}, type(top_num): {type(top_num)}")
    try:
        articles = await get_wexin_article(query, top_num=top_num)
        actual_count = len(articles)
        print(f"获取到 {actual_count} 条结果")
        if actual_count < top_num:
            print(f"警告：实际获取到的结果数量（{actual_count}）小于请求数量（{top_num}）")
        return articles
    except Exception as e:
        print(f"搜索出错：{str(e)}")
        raise HTTPException(status_code=500, detail=f"搜索失败：{str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)