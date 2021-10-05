FROM ubuntu:20.04
RUN apt update && apt -y upgrade
RUN apt install -y python3-pip
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8501
