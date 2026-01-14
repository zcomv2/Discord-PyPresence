#!/usr/bin/env python3
from pypresence import Presence
import time

CLIENT_ID = "1460321110615920680"

rpc = Presence(CLIENT_ID)
rpc.connect()

rpc.update(
    state="Esa Chica tranquila escribiendo...",
    details="Escuhando LoFi y haciendo Tareas",
    large_image="logo",
    large_text="TTY Power Shell",
    start=time.time()
)

while True:
    time.sleep(15)
