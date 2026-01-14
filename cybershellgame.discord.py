#!/usr/bin/env python3
from pypresence import Presence
import time

CLIENT_ID = "1459808522719072408"

rpc = Presence(CLIENT_ID)
rpc.connect()

rpc.update(
    state="Jakiando con JakiKaliOS",
    details="https://cybershellgame.net",
    large_image="logo",
    large_text="Runner Go +On +On",
    start=time.time()
)

while True:
    time.sleep(15)
