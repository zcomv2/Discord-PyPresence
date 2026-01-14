#!/usr/bin/env python3
from pypresence import Presence
import time

CLIENT_ID = "1460313517738688676"

rpc = Presence(CLIENT_ID)
rpc.connect()

rpc.update(
    details="Levantando Minons en Red",
    state="Minion Control Panel CLI",
    large_image="logo",
    large_text="TTY Power Shell",
    start=time.time()
)

while True:
    time.sleep(15)
