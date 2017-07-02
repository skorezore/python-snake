import msvcrt

while True:
    character = msvcrt.getch().decode("utf-8")
    if character == '\r':
        break
    else: print(character)
