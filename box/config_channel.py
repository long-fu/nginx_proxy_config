from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict
import time

app = FastAPI(title="FastAPI Demo Server")
import subprocess
import sys

# --------- 请求体定义 ----------
class Item(BaseModel):
    rtsp: str


def play_video(rtsp: str) -> Dict:
    """
    使用 ffplay 播放视频流
    """
    try:
        # 启动 ffplay 播放视频流
        cmd = [
            sys.executable,          # 当前 Python 解释器（强烈推荐）
            "play_video.py",
            "--rtsp", rtsp
        ]        
        
        subprocess.Popen(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT
        )
        return {"status": "playing", "rtsp": rtsp}
    except Exception as e:
        return {"status": "error", "error": str(e)}

# --------- POST JSON 示例 ----------
@app.post("/configchannel")
def play(item: Item):
    play_video(item.rtsp)
    return {
        "status": "ok",
        "data": item,
    }
