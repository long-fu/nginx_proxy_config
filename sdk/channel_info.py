from fastapi import FastAPI, Request
from pydantic import BaseModel


app = FastAPI(title="FastAPI Demo Server")

# --------- 请求体定义 ----------
class Item(BaseModel):
    info: str

    
# --------- POST JSON 示例 ----------
@app.post("/mc/channelinfo")
def channelinfo(item: Item):
    print("play info received:", item.info)
    return {
        "status": "ok",
        "data": item,
    }