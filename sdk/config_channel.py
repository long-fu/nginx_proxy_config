import requests

BASE_URL = "http://22.10.57.100:8000"

proxies = {
    "http":  "http://192.168.8.188:11568"
}

def test_post_play(rtsp):
    payload = {
        "rtsp": rtsp,
    }
    r = requests.post(f"{BASE_URL}/configchannel", json=payload, proxies=proxies, timeout=3)
    print("item:", r.json())

if __name__ == "__main__":
    rtsp = "rtmp://22.10.57.187:1935/stream"
    test_post_play(rtsp)
