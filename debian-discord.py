#!/usr/bin/env python3
from pypresence import Presence
import time

CLIENT_ID = "1460548214766960674"

rpc = Presence(CLIENT_ID)
rpc.connect()

rpc.update(
    state="Configurando Systemas Y Redes",
    details="Con Debian 13 Trixie Stable",
    large_image="logo",
    large_text="TTY Power Shell",
    start=time.time()
)

while True:
    time.sleep(15)
