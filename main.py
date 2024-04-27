import json

if __name__ == "__main__":
    from my_classes import Person, Subject, Supervisor, Experiment

    # Build a Supervisor
    #supervisor1 = build_person("Lukas", "Höpflinger", "male", 21)
    print("Bitte geben Sie die Daten des Supervisors ein:")
    supervisor1 = Supervisor(
        input("Vorname:" ), 
        input("Nachname:" ), 
        input("Geschlecht (male or female):"), 
        int(input("Alter:")))
    
    #Build a Subject
    #subject1 = build_person("Max", "Mustermann", "male", 25)
    print("Bitte geben Sie die Daten des Subjects ein:")
    subject1 = Subject(
        input("Vorname:" ), 
        input("Nachname:" ), 
        input("Geschlecht (male or female):"), 
        int(input("Alter:")))

    # Build an experiment
    #experiment1 = build_experiment("First Experiment", "2024-04-05", supervisor1, subject1)
    print("Bitte geben Sie die Daten des Experiments ein:")
    experiment1 = Experiment(
        input("Experimentname:" ), 
        input("Datum (Tag.Monat.Jahr):" ), 
        supervisor1.__dict__, 
        subject1.__dict__)

    #Print Experiment
    print(experiment1)


    if input("Soll das Experiment gespeichert werden? (ja/Nein):") == "ja":
        experiment1.save()
        print("Experiment wurde gespeichert.")
    if input("Soll der Supervisor gespeichert werden? (ja/Nein):") == "ja":
        supervisor1.save()
        print("Supervisor wurde gespeichert.")
    if input("Soll das Subject gespeichert werden? (ja/Nein):") == "ja":
        subject1.save()
        print("Subject wurde gespeichert.")
    else:
        print("Die gewünschten Daten wurden gespeichert.")





#Speichern der Datei
# with open("Aufgabe61.json", "a") as outfile: 
  #  json.dump(experiment1.__dict__, outfile)
