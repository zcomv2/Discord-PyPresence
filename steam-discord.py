#!/usr/bin/env python3
from pypresence import Presence
import time

CLIENT_ID = "1460322186467344480"

rpc = Presence(CLIENT_ID)
rpc.connect()

rpc.update(
    state="Play The Game Right Now!!!.",
    details="Delante del Portal de la Vida Virtual",
    large_image="logo",
    large_text="TTY Power Shell",
    start=time.time()
)

while True:
    time.sleep(15)
