#!/usr/bin/python
# -*- coding: utf-8 -*-

import urwid

palette = [
    ("banner", "black", "light gray"),
    ("streak", "black", "dark gray"),
    ("bg", "black", "dark blue"),
]

txt = urwid.Text(("banner", """

YOU HAVE RUN THE 10 MILLIONTH COMMAND IN THIS TERMINAL!!!!!

CLICK TO CLAIM YOU'RE PRIZE!!!!!!!!!!!!!!!!!

"""), align="center")
map1 = urwid.AttrMap(txt, "streak")
fill = urwid.Filler(map1)
map2 = urwid.AttrMap(fill, "bg")

loop = urwid.MainLoop(map2, palette)
def exit(*args, **kwargs): raise urwid.ExitMainLoop()
loop.set_alarm_in(5, exit)
loop.run()
