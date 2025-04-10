import time
from tkinter import *

def update_clock():
    # Lokale Uhrzeit
    current_time = time.strftime("%H:%M:%S")
    # Update das Label mit der aktuellen Zeit
    info_label.config(text=current_time)
    # Lokales Datum
    current_date = time.strftime("%d-%m-%Y")
    # Update das Label mit dem aktuellen Datum
    date_label.config(text=current_date)
    # Rufe diese Funktion nach 1000ms (1s) neu auf
    fenster.after(1000, update_clock)

fenster = Tk()
fenster.title("TTimer")
fenster.configure(bg="black")

# Erstelle ein Label für die Zeit
info_label = Label(fenster, font=("Helvetica", 48), fg="white", bg="black")
info_label.pack()

# Erstelle ein Label für das Datum
date_label = Label(fenster, font=("Halvetica", 24), fg="white", bg="black")
date_label.pack()

# Rufe die Funktion update_clock auf, um die Uhr zu starten
update_clock()

fenster.mainloop()
  