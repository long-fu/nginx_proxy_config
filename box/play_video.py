import argparse
import cv2
import requests

BASE_URL = "http://192.168.8.19:24902"
def post_play_info(rtsp_url: str):
    payload = {
        "info": "running",
    }
    r = requests.post(f"{BASE_URL}/mc/channelinfo", json=payload, timeout=3)
    print("item:", r.json())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rtsp", type=str, required=True)
    args = parser.parse_args()
    print("rtsp:", args.rtsp)
    # rtsp_url = "rtsp://user:password@192.168.1.100:554/stream1"
    cap = cv2.VideoCapture(args.rtsp)

    # 建议：降低延迟
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("读取失败，重试中...")
            continue

        cv2.imshow("RTSP", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()    

if __name__ == "__main__":
    main()
