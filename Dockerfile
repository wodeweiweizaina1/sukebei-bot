FROM python:3.11.4
ADD . /code
COPY sukebei-bot.py /code
WORKDIR /code
RUN pip install -r requirements.txt
ENV BOT_TOKEN="None"
ENV ALLOWED_USER_ID="None"
ENV host="None"
ENV port="None"
ENV secret="None"
COPY start.sh /start.sh
RUN chmod +x /start.sh
ENTRYPOINT /bin/bash /start.sh
