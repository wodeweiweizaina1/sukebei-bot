import telebot
import requests
import sys
from bs4 import BeautifulSoup
import aria2p




# 从命令行参数获取配置
BOT_TOKEN = sys.argv[1]
ALLOWED_USER_ID = int(sys.argv[2])
ARIA2_HOST = sys.argv[3]
ARIA2_PORT = int(sys.argv[4])
ARIA2_SECRET = sys.argv[5]

# 初始化 aria2 客户端
aria2 = aria2p.API(
    aria2p.Client(
        host=ARIA2_HOST,
        port=ARIA2_PORT,
        secret=ARIA2_SECRET
    )
)

# 初始化 Telegram bot
bot = telebot.TeleBot(BOT_TOKEN)

def fetch_data(code):
    url = f"https://sukebei.nyaa.si/user/offkab?q={code}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('tr', class_='success')
    
    return max(
        (
            (int(row.find('td', class_='text-center', string=lambda x: x and x.strip().isdigit()).text),
             row.find('a', href=lambda x: x and x.startswith('magnet:'))['href'])
            for row in rows
            if row.find('td', class_='text-center', string=lambda x: x and x.strip().isdigit()) and
               row.find('a', href=lambda x: x and x.startswith('magnet:'))
        ),
        key=lambda x: x[0],
        default=(0, None)
    )[1]

@bot.message_handler(func=lambda message: message.from_user.id == ALLOWED_USER_ID)
def process_message(message):
    print(f"收到的消息: {message.text}")
    magnet_link = fetch_data(message.text)
    if magnet_link:
        aria2.add_magnet(magnet_link)
        bot.reply_to(message, "下载任务已添加")
    else:
        bot.reply_to(message, "未找到匹配的磁力链接")

@bot.message_handler(func=lambda message: message.from_user.id != ALLOWED_USER_ID)
def unauthorized_access(message):
    bot.reply_to(message, "对不起，您没有使用此机器人的权限。")

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling()

