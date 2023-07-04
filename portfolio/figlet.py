import sys
from random import randrange
from pyfiglet import Figlet

if len(sys.argv) != 1 and len(sys.argv) != 3:
    print("Invalid usage")
    sys.exit(1)

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 3:
    if (sys.argv[1] != "-f" and sys.argv[1] != "--font") or sys.argv[2] not in font_list:
        print("Invalid usage")
        sys.exit(1)
    else:
        fnt = sys.argv[2]
else:
    fnt = font_list[randrange(len(font_list))]

figlet.setFont(font=fnt)
text = input("Input: ")
print("Output:")
print(figlet.renderText(text))
