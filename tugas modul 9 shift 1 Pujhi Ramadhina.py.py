import os
import time
from termcolor import cprint

def clear_screen():
    os.system("cls")

def loading_screen():
    clear_screen()
    cprint("=" * 16, "yellow")
    cprint(" TIX ID LOADING", "cyan", attrs=["bold"])
    cprint("=" * 16, "yellow")
    logo_lines = [
            "    _______    ",
            "  /         \\  ",
            " |   T I X   | ",
            "  \\ _______ /  "
    ]
    for line in logo_lines:
        cprint(line, "yellow", "on_black", attrs=["bold"])
    cprint("\nMemuat aplikasi", "green", attrs=["bold"])
    for i in range(6):
        print("Loading" + "." * (i % 4) + "   ", end="\r")
        time.sleep(0.5)
    cprint("\n\nAplikasi siap digunakan!", "green", attrs=["bold"])
    input("\nTekan Enter untuk keluar...\n")

if __name__ == "__main__":
    loading_screen()