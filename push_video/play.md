```conf
user root;
worker_processes 1;

load_module modules/ngx_http_flv_live_module.so;

events {
    worker_connections 1024;
}

http {
    include mime.types;
    default_type application/octet-stream;

    keepalive_timeout 65;

    sendfile on;
    server {
        listen 18080;
        location /live {
            flv_live on; #打开 HTTP 播放 FLV 直播流功能
            chunked_transfer_encoding on; #支持 'Transfer-Encoding: chunked' 方式回复

            add_header 'Access-Control-Allow-Origin' '*'; #添加额外的 HTTP 头
            add_header 'Access-Control-Allow-Credentials' 'true'; #添加额外的 HTTP 头
        }
    }
}

rtmp {
    server {
        listen 1935;
        chunk_size 4096;
        out_queue 4096;
        out_cork 8;
        max_streams 128;
        timeout 15s;
        drop_idle_publisher 15s;

        log_interval 5s; #log 模块在 access.log 中记录日志的间隔时间，对调试非常有用
        log_size 1m; #log 模块用来记录日志的缓冲区大小

        application myapp {
            live on;
            gop_cache on; #打开 GOP 缓存，减少首屏等待时间
        }
    }
}

```
ffplay rtmp://192.168.8.208:1935/myapp/test
http://example.com:8080/live?port=1985&app=myapp&stream=test
http://192.168.8.208:18080/live?port=1935&app=myapp&stream=test

ffplay -fflags nobuffer -flags low_delay \
  "http://example.com:8080/live/test.flv?port=1985&app=myapp"
http://127.0.0.1:18080/live/test.flv
ffplay -fflags nobuffer -flags low_delay \
  "http://192.168.8.208:18080/live/test.flv?port=1935&app=myapp"

ffplay http://192.168.8.208:18080/live/test.flv
ffplay http://192.168.8.208:18080/live/test.flv

http://192.168.8.14:18090/live?src=a&port=1935&app=myapp&stream=test