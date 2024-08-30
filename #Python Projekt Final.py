#Python Projekt Final
import random
import time
import sys

#function for printing out text slowly to simulate someone typing the text out
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

#region Playr values and gear
player = {"name": "Du", "lp": 10, "weapon": "", "damage": 0, "gear": "", "defense": 0},
#endregion

#region Opponent list
enemylist = [
{"name": "Warg", "lp": 3,"weapon": "Zähne", "damage": 1, "defense": 0},
{"name": "Ork", "lp": 5,"weapon": "", "damage": 0, "defense": 0},
{"name": "Troll", "lp": 10,"weapon": "", "damage": 0, "defense": 0},
]
#endregion

#region Weapon list
weaponlist = [
{"weapon": "Schwert", "damage": 1},
{"weapon": "Axt", "damage": 1},
{"weapon": "Hellebarde", "damage": 3},
]

itemlist = [
{"item": "Heiltrank", "heal": 10,},
]

gearlist = [
{"gear": "Schild", "defense": 5,},
]

# Ask the user a question expecting a numeric answer within the specified range
# defined by range(min, max + 1). If an invalid input is entered, prompt again.
#region
# Returns the number that the user entered.
def prompt(question: str, min: int, max: int):
    try:
        answer = int(input(question))

        if answer in range(min, max + 1):
            return answer
        else:
            print(f'Die eingegebene Nummer ist nicht gültig, bitte geben Sie eine Nummer zwischen {min} und {max} ein.')
            return prompt(question, min, max)
    
#handle exceptions raised if the user enters something that can't be parsed as an integer
    except ValueError:
        print(f'Bitte gebe eine Nummer zwischen {min} und {max} ein.')
        return prompt(question, min, max)

#region Difficulty setting
difficulty = prompt("\nWelchen Schwierigkeitsgrad möchtest du spielen? [0] Einfach [1] Normal [2] Schwer:\n", 0, 2)
if difficulty == 0:
    player[0]["weapon"], player[0]["damage"], player[0]["gear"], player[0]["defense"] = weaponlist[2]["weapon"], weaponlist[2]["damage"], gearlist[0]["gear"], gearlist[0]["defense"]
    enemylist[1]["weapon"], enemylist[1]["damage"] = weaponlist[1]["weapon"], weaponlist[1]["damage"]
    enemylist[2]["weapon"], enemylist[2]["damage"] = weaponlist[0]["weapon"], weaponlist[0]["damage"]
    enemylist[0]["lp"] = 3
    enemylist[1]["lp"] = 4 
    enemylist[2]["lp"] = 8
elif difficulty == 1:
    player[0]["weapon"], player[0]["damage"] = weaponlist[1]["weapon"], weaponlist[1]["damage"]
    enemylist[1]["weapon"], enemylist[1]["damage"] = weaponlist[1]["weapon"], weaponlist[1]["damage"]
    enemylist[2]["weapon"], enemylist[2]["damage"] = weaponlist[0]["weapon"], weaponlist[0]["damage"]
    enemylist[0]["lp"] = 3
    enemylist[1]["lp"] = 5
    enemylist[2]["lp"] = 9
else:
    player[0]["weapon"], player[0]["damage"] = weaponlist[0]["weapon"], weaponlist[0]["damage"]
    enemylist[1]["weapon"], enemylist[1]["damage"] = weaponlist[1]["weapon"], weaponlist[1]["damage"]
    enemylist[2]["weapon"], enemylist[2]["damage"] = weaponlist[2]["weapon"], weaponlist[2]["damage"]
    enemylist[0]["lp"] = 4
    enemylist[1]["lp"] = 5
    enemylist[2]["lp"] = 10
#endregion

#region fight mechanic
def fighting(enemyidx):
    # fight =  prompt("Do you want to fight? [0] Nein [1] Ja \n", 0, 1)
    
    print("\nDer Kampf beginnt\n")

    attacker = player[0]
    defender = enemylist[enemyidx]

#fight mechanic in a function
    while True:
        if attacker["lp"] and defender["lp"] > 0:
            result_roll = roll()
            result_roll = result_roll - defender["defense"]
            if result_roll >= 9:
                print("Würfelergebnis: ", result_roll, "\nKritischer Treffer!\n",-attacker["damage"] + 1, "Lebenspunkte")
                defender["lp"] -= attacker["damage"] + 1
            elif result_roll > 2:
                print("\nWürfelergebnis: ", result_roll, "\nTreffer!\n",-attacker["damage"], "Lebenspunkt")
                defender["lp"] -= attacker["damage"]
            else: 
                print("Du würfelst: ", result_roll, "\nPariert!" )

            print("Lebenspunkte: ", defender["name"], defender["lp"], "\n")
            time.sleep(2)
        
            if enemylist[enemyidx]["lp"] <= 0:
                print(f"Der {defender["name"]} geht zu Boden.\nDu hast noch {player[0]["lp"]} Lebenspunkte.")
                return True
        
            attacker, defender = defender, attacker

        if player[0]["lp"] <= 0:
                return False
#endregion

user_is_playing = True

# Ask the user a question expecting a numeric answer within the specified range
# defined by range(min, max + 1). If an invalid input is entered, prompt again.
#region
# Returns the number that the user entered.
def prompt(question: str, min: int, max: int):
    try:
        answer = int(input(question))

        if answer in range(min, max + 1):
            return answer
        else:
            print(f'Die eingegebene Nummer ist nicht gültig, bitte geben Sie eine Nummer zwischen {min} und {max} ein.')
            return prompt(question, min, max)
    
#handle exceptions raised if the user enters something that can't be parsed as an integer
    except ValueError:
        print(f'Bitte gebe eine Nummer zwischen {min} und {max} ein.')
        return prompt(question, min, max)

#Prompt the user to either restart or exit the game.
def exit_check():
    global user_is_playing

    result = prompt("Du bist gestorben. Erneut versuchen [0] oder Spiel beenden [1]: ", 0, 1)
#if user entered 1, break out of the main loop (exit gracefully)
    if result == 1:
        user_is_playing = False
        exit(0)
#Defines function which rolls d9 
def roll():
    return random.randint(1, 9)

#Start of the game
print("\nHerzlich Wilkommen im Textadventure! Bitte benutze zum spielen die Tasten [0] , [1] oder [2] \n")
time.sleep(2)

#Introduction of the story
print_slow(f"""\nDu wachst in einem dunklen Raum auf und bemerkst sofort einen starken Schmerz im Kopf.
Als du mit deiner Hand deine Stirn abtastest, fühlst du eine große Beule und blut tropft dir ins Gesicht.
Dann wird dir klar, dass du bewusstlos gewesen sein musst und keine Erinnerungen mehr an deine Vergangenheit hast. 
Dir ist aber bewusst, dass etwas Schlimmes passiert ist, deswegen bündelst du deine letzten Kräfte und erhebst dich. 
Zu deinem großen Glück siehst du ein/e {player[0]["weapon"]} zu deiner linken liegen und hebst es auf.
Es fühlt sich vertraut an und liegt gut in der Hand.
Vor dir erstreckt sich ein langer Gang, der von Fackeln an den Wänden erleuchtet wird. Dann läufst du los…\n""")

#Player´s first decision
while user_is_playing:
        time.sleep(1)
        print_slow("""\nAm Ende des Ganges erblickst du eine schwere und große Eisentür auf welche du dich zubewegst. 
Aus dem Augenwinkel fällt auf der Hälfte des Ganges zu deiner rechten eine weitere
aber kleinere und unauffälligere Holztür auf.
Entscheidest du dich, es durch die kleine Holztür zu deiner rechten zu versuchen 
oder gehst du bist zum Ende des Ganges und wählst die schwere Eisentür?\n""")
#Asks user which door they want to choose
        floor1room1 = prompt("\nSchwere Eisentür [0] oder unauffällige Holztür [1] ?:\n", 0, 1)
        if floor1room1 == 0:
            print_slow("""\nDu bewegst dich schnell und entschlossen auf die schwere Eisentür zu.
Als du vor Ihr stehst entdeckst du ein Rätsel an der Tür:\n""")
            
#Asks user riddle and validates answer
            riddle = prompt("""\nWas hat ein Gesicht und zeigt die Zeit an, hat aber weder Mund noch Augen. 
Der Fluss [0] Die Zeit: [1]\n""", 0, 1)
            if riddle == 0:
                print_slow("""\nDeine Antwort ist falsch! Der Boden gibt plötzlich nach und bricht ein. 
Vor dir klafft jetzt ein großes Loch im Boden, wo grade noch die Tür war.\n""")
            elif riddle == 1:
                print_slow("""\nDeine Antwort ist richtig! Du drehst die Scheibe an der Tür in die Richtige Position und Sie öffnet sich. 
Du gehst durch die Eisentür betrittst den nächste Raum in welchem sich eine Falltür befindet. 
Du öffnest die Falltür und kletterst eine lange Leiter hinab in die Tiefe.\n""")
                break  
#Conditional if user answers riddle incorrectly     
            hole = prompt("\nMöchtest du versuchen hinüber zu balancieren [0] oder versuchen zu Springen? [1]\n", 0, 1)
            if hole == 0:
                print_slow("""\nSehr gut! Du balancierst erfolgreich über die Holzstrebe und entdeckst eine Falltür im Boden. 
Du öffnest die Falltür und kletterst eine lange Leiter hinab in die Tiefe.\n""")
                break
            elif hole == 1:
                print_slow("""\nDu hast hast versucht über das Loch zu Springen.
Beim Anlauf bis du gestolpert und in das Loch gefallen.\n""")
                exit_check()
                continue
                

#Asks user if they wants to return to starting point or choose slide
        elif floor1room1 == 1:
            print_slow("""\nDu öffnest die unauffällige Holztür und betrittst einen kleinen Raum dahinter. 
Es ist sehr dunkel aber du kannst vor dir am Ende des Raums deutlich eine kleine Rutsche erkennen.?\n""")
            slide = prompt("\nMöchtest du das Risiko eingehen und rutscht in die Dunkelheit [0] oder gehst du durch die kleine Holztür zurück [1]\n", 0, 1)

            if slide == 0:
                print_slow(f"""\nEs ist sehr dunkel aber du kannst vor dir am Ende des Raums deutlich eine kleine Rutsche erkennen.
Du nimmst deinen ganzen Mut zusammen und rutscht in die Dunkelheit. 
Als du wieder etwas sehen kannst stehst du in einem weiteren Raum. Auf einmal hörst du ein Geräusch aus einer Ecke des Raums. 
Ein riesiger Warg tritt aus dem dunklen hervor und macht sich bereit zum Angriff. 
Du greifst nach deinem/r {player[0]["weapon"]} und machst dich ebenfalls bereit für den Kampf\n""")

#First fight of the game (Warg)
                warg = prompt("\nDu wirst jetzt von dem Warg angegriffen, möchtest du dich verteidigen, Ja [0] Nein [1] \n", 0, 1)
                if warg == 0:
                    player_won = fighting(0)
                    if player_won:
                        print_slow("""\nPerfekt! Mit einem schnellen Stich ins Herz erledigst du deinen Gegner. 
Du hast den Warg besiegt! Hinter dem toten Körper kannst du eine weitere Tür ausmachen,
welche sich perfekt in die Steinwand einfügt und schwer zu erkennen ist.
Du kletterst über den Warg und drückst die steinerne Klinke der Tür herunter.
Mit einem lautem Geräusch öffnet Sie sich.
Dahinter ist eine Falltür.
Da dies der einzige Weg zu sein scheint, stemmst du die auch die Falltür auf und kletterst eine lange Leiter hinab in die Tiefe.\n""")
                        break
                    exit_check()
                    continue
                elif warg == 1:
                    exit_check()
                    continue

            elif slide == 1:
                print_slow("\nDu hast dich entschieden zurückzugehen, wo du herkamst.\n")
                continue


#Prints out lore
print_slow("""\nWährend du die Leiter hinabsteigst erinnerst du dich plötzlich an Bruchstücke deiner Vergangenheit. 
Du wurdest in deinem Haus angegriffen und hast einen schweren Schlag auf den Kopf bekommen. 
Danach ist die Erinnerung nur noch sehr schwach.
Du erinnerst dich auch daran das du entführt und einige Zeit durch die Dunkelheit geschleift wurdest.\n""")

#informs user they've reached a checkpoint
print_slow("\nDu hast jetzt ein Checkpoint erreicht. Falls du Sterben solltest fängst du von diesem Punkt erneut an.\n")

print_slow("""\nDu hast jetzt einen neuen Raum betreten. Vor dir sind zwei Abzweigungen zu sehen.
Entweder kannst du durch den rechten oder den linken Gang gehen.\n""")

        
while user_is_playing:
#Choose which path to proceed with
    Path = prompt("\nWelchen Gang möchten Sie nehmen? links [0] oder rechts [1]:\n", 0, 1)

    if Path == 0:
#Left Path: Room 1
        print_slow("""\nDu hast dich für den linken Gang entschieden.
Du stehst jetzt in einem Zimmer mit Steinwänden und einer ganzen Halle.
Du siehst am Ende des Zimmers eine kleine Falltür.
Der Boden von dem Raum ist uneben und es liegen Leichen in dem Zimmer. 
Von der Decke hängen Spikes, die aus Stein gemacht sind.
Du betrittst das Zimmer und läufst über eine Druckplatte, welche in den Boden eingelassen ist.
Ein großes Eisentor fällt hinter dir herrunter und blockiert den Gang aus dem du gekommen bist.
Aufeinmal fallen die Spikes ein ganzes stück herrunter. Du musst jetzt schnell aus dem Zimmer kommen, 
vor die Decke ganz herrunterkommt. Rolle einen Würfel, um festzustellen, ob du es schaffst.\n""")
#Rolls D9 to determine if you pass the condition
        ergebnis = roll()
        print("\nDu hast", ergebnis, "gewürfelt\n")
#Result of previous D9 
        if ergebnis >= 5:
            print_slow("""\nDu bist losgerannt und den Leichen ausgewichen.
Dann hast du es über den unebenenden Boden bis zur Falltür geschafft.\n""")
        elif ergebnis <= 4:
            print_slow("""\nDu bist Richtung Falltür losgelaufen.
Während du gerannt bist, bist du über den unebenen Boden gestolpert und auf eine Leiche gefallen.
Leider hast du es zeitlich nicht zur Falltür geschafft.
Du wurdest von den Spikes auf der Decke aufgespießt.\n""")
#Asks user if they want to keep playing or exit the game
            exit_check()
            continue
        
        leftpathroom2 = ergebnis >=5
        
        #Left path room 2
        if leftpathroom2: 
            print_slow("""\nDu befindest dich jetzt in einem neuen Raum. Du siehst, in der Mitte des Zimmers ist eine gravierte Drehschreibe.
Auf der linken Seite des Zimmers sind Gefängniszellen, dort siehst du einen älteren Mann.\n""")
            leftpathroom2choice1 = prompt("\nMöchtest du ihn Angreifen [0] oder mit ihm Reden? [1]:\n", 0, 1)
            
#Results of left path room 2
            if leftpathroom2choice1 == 0:
                print_slow(f"""\nDu hebst dein/e {player[0]["weapon"]} und schlägst es dem Mann in den Kopf. Er kippt sofort um und sein Kopf fängt an stark zu bluten.
Sein Blut fängt an in die Gravierung der Drehscheibe zu fließen. Nach wenigen Sekunden dreht sich die Drehscheibe im Uhrzeigersinn.
Die geschlossene Tür hinter der Drehscheibe hat sich jetzt geöffnet.\n""")
                print_slow("""\nDu bist jetzt durch die Tür. Hinter der Tür ist eine große Treppe die du hoch läufst.
Als du oben ankommst, siehst du vor dir eine große Holztür. Du schlagst die Tür auf und vor dir ist eine Riesenhalle.\n""")
                break
            elif leftpathroom2choice1 == 1:
                print_slow("""\nDu läufst zu dem älterem Mann. Er stöhnt und sagt: Um weiterzukommen, wird das Leben als Opfer verlangt.
Ich bin nicht mehr stark genug um hier herrauszukommen, aber du könntest es noch schaffen.
Finde einen Ausweg und nimm mich bitte als Opfer.
Ich bin hier schon viel zu lange, meine Zeit ist gekommen.\n""")

#Left path room 2 2nd choice
                leftpathroom2choice2 = prompt("\nMöchtest du den Herrn opfern [0] oder dich selber opfern? [1]:\n", 0, 1)

#Results of left path room 2 2nd choice
                if leftpathroom2choice2 == 0: 
                    print_slow(f"""\nDu hebst dein/e {player[0]["weapon"]} und köpfst den älteren Mann.
Sein Blut fliest über die Drehscheibe hinaus und die Tür öffnet sich.
Du bist jetzt durch die Tür gegangen. Hinter der Tür ist große Treppe, welche du erklimmst.
Als du oben ankommst, siehst du vor dir eine große Holztür. Du schlägst die Tür auf und vor dir ist eine Riesenhalle.\n""")
                    break
                elif leftpathroom2choice2 == 1:
                    print_slow(f"""\nDu nimmst dein/e {player[0]["weapon"]} und stößt es in dein eigenes Herz.
Dein Blut fließt über die Drehscheibe und eine Tür öffnet sich.
Du fällst auf den Boden und wirst ohnmächtig. Du bist gestorben. \n""")
                    exit_check()
                    continue
#Right Path Room 1 
    elif Path == 1:
        print_slow("""\nDu hast dich für den rechten Gang entschieden.
Du stehst jetzt in einem runden Zimmer. Der Boden und die Wände bestehen aus Sandstein. 
Inmitten des Zimmers ist ein Sockel aus Obsidian.
Auf dem Sockel steht eine Keramikschale mit einer schwarzen Flüssigkeit.
Du hast die Möglichkeit, die Flüssigkeit auszutrinken oder auszuschütten oder zurück ins erste Zimmer zu gehen.\n""" )

#Right path room 1 choice 1
        rightpathroom1 = prompt("\nWas möchtest du jetzt machen, Flüssigkeit Trinken [0], Ausschüten [1]? oder zurück zur Abzweigung? [2] \n", 0, 2)

        if rightpathroom1 == 0:

#Result of right path room 1 option 0
            print_slow("""\nAuf einmal ist dir sehr übel und schwindelig.
Du hast das Gefühl, dass du jeden Moment bewusstlos werden kannst. Du ignorierst das Schwächegefühl und trinkst einfach weiter.
Nachdem du alles ausgetrunken hast, fühlst du dich schwächer als ob dir jemand Kraft genommen hat.
Am anderen Ende des Zimmers öffnet sich plötzlich eine geheime Tür, die in der Wand versteckt ist.\n""")
        elif rightpathroom1 == 1:

#Result of right path room 1 option 1
            print_slow("""\nDu hast die Schüssel ausgeschüttet. 
Du spürst eine starke Vibrationen im Raum, als ob es ein großes Erdbeben gibt.
Wasser fängt an, von den Wänden zu tropfen. Das Wasser steigt und der Druck erhöht sich, bis es aus den Wänden geschossen kommt.
Jetzt fühlt sich das Zimmer sehr schnell mit Wasser. Du versucht herauszukommen, aber es ist zu spät: Alle Türen sind verschlossen.
Es gibt keinen Weg mehr raus. Du bist ertrunken.\n""")

#Loops back to the start of floor 2 if user chose choice 2
            exit_check()
            continue
        
#Orc fight
        if rightpathroom1 == 0:
            print_slow(f"""\nDu bist jetzt durch die Tür gekommen. In dem neuen Raum sind Stahlstühle und Tische zu sehen.
An einem der Tische sitzt ein Ork in einem Mantel. Er brüllt dich an, dass du ihn gestört hast. 
Er steht wütend auf, nimmt sein/e {enemylist[1]["weapon"]} in die Hand und stürmt auf dich zu.\n""")
            ork = prompt("\nDu wirst jetzt von dem Ork angegriffen, möchtest du dich verteidigen Ja [0] Nein [1] \n", 0, 1)
            if ork == 0:
                player_won = fighting(1)
                if player_won:
                    print_slow(f"""\nDu hast den Ork besiegt. Dein/e {player[0]["weapon"]} berührt zufällig das Blut des toten Orks.
Der Kopf deine/r {player[0]["weapon"]} leuchtet jetzt dunkel Rot und pulsiert. Diese/s {player[0]["weapon"]} sieht wirklich mächtig aus.\n""")
                    player[0]["damage"] += 2
                    break
                exit_check()
                continue
            elif ork == 1:
                exit_check()
                continue

#End of last floor. Boss fight ahead
print_slow("\nNach dem du eine lange und steile Treppe hochgelaufen bist, stehst du jetzt vor einer großen Holztür.\n")
print_slow("""\nDu trittst in eine große Halle.
Am anderen Ende des Raums siehst du einen schlafenden Troll. Auf der linken Seite des Zimmers sind 
große Fenster mit Eisenstangen. Durch die offenen Fenster strömt kalter Wind und durch das öffnen der Tür 
entsteht ein Durchzug, welcher die Tür schlagartig hinter dir zu schlägt. Durch den Lärm
der Tür wacht der Troll auf. Er steht auf, guckt sich um und sieht dich im Zimmer stehen. Er schreit
dir zu: Du hast hier nichts zu suchen.Er hebt seine große Holzkeule vom Boden auf und brüllt:
Ich mach dich jetzt platt.\n""")

print_slow("\nDu hast jetzt ein Checkpoint erreicht. Falls du Sterben solltest fängst du von diesem Punkt erneut an.\n")


while user_is_playing:
    end_boss = prompt("\nDu wirst jetzt von dem Troll angegriffen, möchtest du dich verteidigen Ja [0] Nein [1] \n", 0, 1)
    if end_boss == 0:
        player_won = fighting(2)
        if player_won:
            break
        exit_check()
        continue
    else:
        exit_check()
        continue

print_slow("""\nNach einem intensiven Kampf nimmst du Anlauf,
springst auf den Rücken des Trolls und erschlägst ihn mit einem schweren Hieb in den Nacken.
Der Troll stürzt donnernd auf den Mamorboden der Halle und bleibt Tod liegen.\n""")

#End of all floors, final dialogue and last decision
print_slow("""\nDu schaust dich um und entdeckst eine lange Strickleiter.
Blutüberströmt und mit letzter Kraft kletterst du dem Licht entgegen.
Als du das Ende der Strickleiter erreichst stehst du in einem Haus in dem es aussieht wie in einer Schmiede.
Plötzlich strömt die Erinnerung in dein Gedächtnis zurück.
Du bist Schmied, deswegen fiel es dir leicht mit Waffen umzugehen. 
Du wurdest von Orks angegriffen und entführt.
Als du die Küche deines Hauses betrittst, indem sich auch deine Schmiede befindet,
schaut dich deine Frau aus großen Augen an.
Neben Ihr steht ein mysteriöser Mann in einem langen schwarzen Mantel welcher sein Gesicht bedeckt.\n""")

end_choice = prompt("\nWas möchtest du tun? Den unbekannten blitzschnell angreifen und versuchen ihn zu enthaupten [0] oder mit ihm sprechen? [1]\n", 0, 1)

#Good ending
if end_choice == 0:
    print_slow("""\nNach einem kurzen Gerangel steckt ein Messer in der Brust des Unbekannten.
Deine Frau schreit aber Ihr seid in Sicherheit. Deine Frau fängt an zu sprechen: 'Da bist du ja,
ich dachte du wärest tot. Danke das du mich geretet hast.
Deine Frau erzählt dir das der Unbekannte dich entfürt hat das du für ihn Waffen schmieden solltest.
Die Waffen wollte er in einem Krieg gegen dein Volk verwenden.
Nach einem gespräch und fröhlichen wiedersehen, bist du so müde das du vor erschöpfung einschläfst.\n""")

#Secret Ending
elif end_choice == 1 and enemylist[0]["lp"] <=0 and enemylist[1]["lp"] <= 0 and enemylist[2]["lp"] <= 0:
    print_slow("""\nDer unbekannte fängt an zu sprechen. 
Es kommt dir wie eine Ewigkeit vor, dass du zuletzt einen Menschen hast reden hören.
Der Unbekannte erklärt das er dein verschollener Bruder ist und dich überall gesucht hat. 
Er möchte das du für ihn Waffen herstellst und mit ihm gegen das aktuell bestehende Königreich kämpfst.
Er möchte den König stürzen und selbst den Thron besteigen umd das Volk zu retten.
Er sagt dir das der könig böse ist weil er Kriegsverbrechen begangen hat.
Vor einiger Zeit wurden mehrere Dörfer in Schutt und Asche gelegt und die Bewohner ermordet.
Das hat der König zu alleine zu verantworten.
Du entscheidest mit deinem Bruder zu gehen und Ihr schafft letztendlich alles was Ihr euch vorgenommen habt.
Ihr errichtet zusammen ein neues und sicheres Königreich.
Du un deine Familie lebt zusammen glück bis ans Ende aller Tage.\n""")

elif end_choice == 1:   
    print_slow("""\nDer Unbekannter macht dir ein Angebot. Wenn du mit ihm in die Schwarzlande gehst,
wirst du ein reicher Mann sein. Das einzige was du dafür machen musst ist für ihn Waffen von hohe Qualität herzustellen.
Die Waffen werden dringend für einen Krieg gebraucht.\n""")
    end_choice2 = prompt("Möchtest du sein angebot wahr nehemen ? Ja [0] oder nein [1]", 0, 1)

#Bad Ending 
    if end_choice2 == 0:
        print_slow("""\n Du nimmst das Angebot an und reist mit ihm in die Schwarzlande.
Leider stellt sich heraus das er gelogen hat. 
Du wirst in Ketten gelegt und wirst für des Rest deines Lebens in Sklaverei Waffen herstellen.
Deine Familie siehst du nie wieder.\n""")

#Good Ending 2
    elif end_choice2 == 1:
        print_slow("""\n Du nimmst das Angebot von dem Unbekannten nicht an. 
Du spuckst ihm vor die Füße. Du würdest nie Waffen für den Krieg herstellen. 
Der Unbekannter wird wütend und nimmt sein Schwert in die Hand. Ein wilder zweikampf bricht aus.
Doch am ende liegt der Unbekannte blutend tot auf dem Boden.\n""")
