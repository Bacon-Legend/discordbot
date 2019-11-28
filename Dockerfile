FROM ubuntu:latest
RUN apt update -y && apt upgrade -y
RUN apt install git python3-pip python3
RUN git clone https://github.com/Bacon-Legend/discordbot
RUN pip3 install -r discordbot/requirements.txt
CMD ["python3","discordbot/app.py"]