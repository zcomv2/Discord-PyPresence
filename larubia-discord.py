#!/usr/bin/env python3
from pypresence import Presence
import time

CLIENT_ID = "1459836603609649213"

rpc = Presence(CLIENT_ID)
rpc.connect()

rpc.update(
    state="Dandole Duro a la Rubia",
    details="Con mi Poyuco a SuXumino",
    large_image="logo",
    large_text="Tres veces al dia en el Hotel del Amor",
    start=time.time()
)

while True:
    time.sleep(15)
