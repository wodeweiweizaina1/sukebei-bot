# sukebei-bot
## 实现功能
给tg机器人发送番号，机器人自动下载到aria中，并回复已下载。注意发送的消息之中有且只能有一个番号
## 启动方法
### 编译成docker
运行docker需要配置五个环境变量，bottoken为telegram的token，ALLOWED_USER_ID为你的对话id， host，port，secret为aria2下载器的地址
```python
docker run --network host \
  -e BOT_TOKEN=dasdqweqweqweqw \
  -e ALLOWED_USER_ID=121111111 \
  -e host=http://192.168.1.1 \
  -e port=6800 \
  -e secret=password \
  --restart unless-stopped \
  sukebei-bot:latest
```

### 直接运行python
对python代码从环境变量取值的几处填成值就可以了运行了
