import subprocess;
import time;

EMULADOR = r"C:\Users\Tralhoto\Desktop\Projeto pokemon\Emulador\mGBA-0.10.5-win64\mGBA.exe";
ROM = r"C:\Users\Tralhoto\Desktop\Projeto pokemon\Roms\Pokemon fireRed.gba";

def iniciar_jogo():
    subprocess.Popen([EMULADOR, ROM])

    time.sleep(5)
