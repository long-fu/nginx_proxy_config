# 网络拓扑代理

A <-> PROXY <-> B
      PROXY <-> C

A -> B 正向代理 
A -> C

B -> A 反向代理
C -> A

# 正向代理CURL 测试


```sh

curl -x http://127.0.0.1:3128 http://httpbin.org/ip

```