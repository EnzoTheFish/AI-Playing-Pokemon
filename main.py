import time
from launcher import iniciar_jogo
import json

iniciar_jogo();

while True:

    with open("ipc/state.json") as f:
        state = json.load(f)

    print(state)

    time.sleep(1)