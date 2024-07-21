# sukebei-bot
## 启动方法
### 编译成docker
运行docker需要配置五个环境变量，bottoken为telegram的token，ALLOWED_USER_ID为你的对话id， host，port，secret为aria2下载器的地址
'''docker
docker run --network host \
  -e BOT_TOKEN=dasdqweqweqweqw \
  -e ALLOWED_USER_ID=121111111 \
  -e host=http://192.168.1.1 \
  -e port=6800 \
  -e secret=password \
  --restart unless-stopped \
  sukebei-bot:latest
'''


