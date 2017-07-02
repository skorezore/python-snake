import msvcrt

def input():
    if msvcrt.kbhit():
        return msvcrt.getch().decode("utf-8")

    return '\0'
