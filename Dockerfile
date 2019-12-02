FROM python:3.8.0-alpine3.10
RUN apk add git
RUN git clone https://github.com/Bacon-Legend/discordbot
RUN pip3 install -r discordbot/requirements.txt
CMD ["python3","discordbot/app.py"]