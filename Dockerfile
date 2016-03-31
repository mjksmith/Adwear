FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3-pip python-pip tmux

RUN pip install urwid
RUN pip3 install urwid

ADD adwear /adwear

ENTRYPOINT ./adwear/adwear.py
