# Leistungsanalyse-App
## Clonen Sie das Github-Repository auf ihren PC.
- Öffnen Sie dazu Git Bash und navigieren Sie zu dem gewünschten Ordner: `cd "<gewünschter Ordner>"`
- Geben Sie den folgenden Befehl ein um das Repository in den Ordner zu clonen: `git clone <Link des Repositorys>`

## Öffnen Sie den Ordner in VS Code

### Virtuellen Bereich erstellen: 

- Öffnen Sie ein neies Terminal --> windows Powershell
- Geben sie folgenden Befehl ein um einen Virtuellen Bereich zu erstellen: `python -m venv .venv`
- Geben sie folgenden Befehl ein um einen Virtuellen Bereich zu aktivieren: `.\.venv\Scripts\Activate`
- Falls dieser nicht funktioniert gib vorher folgenden Befehl ein um den Zugriff zu erlauben: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`.
- Der Virtuelle Bereich ist nun erstellt und activiert.

## Nötigen Pakete installieren:
<<<<<<< HEAD

- Die nötigen Pakete sind in der Text-Datei requirements.txt angeführt.
=======
- Die nötigen Pakete sind in der Text-Datei `requirements.txt` angeführt.
>>>>>>> b8221e2ca5d2f08fa710ef6a8255d40f8acdfe76
- Für die nächten Schritt müssen sie sich schon in der Umgebung befinden und diese muss aktiviert sein.
- Sie können sie einzeln installieren indem sie folgenden Befehl in die Komandozeile von Windows Powershell eingeben: `pip install <gewünschtes Paket>`
- Sie können auch alle Pakete gleichszeitig installieren indem sie folgenden Befehl in die Komandozeile von Windows Powershell eingeben: `pip install -r requirements.txt`

- #### Der Code kann nun Ausgeführt werden.

- Code ausführen und die geforderten Daten eingeben !!bei Geschlecht nur: male oder female schreiben!! (Falls nicht muss der Benutzer die max. Heartrate manuell eingeben)
- Experiment wird in json-Datei gespeichert und abgelegt

### Den Branch in VS-Code wechseln

- ein neues PowershellTerminal erstellen 
- Mit dem Befehl `git checkout <Name of Branch>` den Branch wechseln

## venv erstellen und Server starten

- mit `git clone <link des repositories>` das repository clonen
- `.\venve\Scripts\activate` das virtuell Environment starten und die `requirements.txt` installieren
    - mit `ls` kann man die Ordnerstruktur ansehen
- `python .\main.py` die main Datei des geklonten repositories ausführen und Server starten
    - STRG+C um den Server zu stoppen

