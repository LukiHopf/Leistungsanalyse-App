import json

if __name__ == "__main__":
    from my_classes import Person, Experiment

    # Build a Supervisor
    #supervisor1 = build_person("Lukas", "Höpflinger", "male", 21)
    print("Bitte geben Sie die Daten des Supervisors ein:")
    supervisor1 = Person(
        input("Vorname:" ), 
        input("Nachname:" ), 
        input("Geschlecht (male or female):"), 
        int(input("Alter:")))
    
    #Build a Subject
    #subject1 = build_person("Max", "Mustermann", "male", 25)
    print("Bitte geben Sie die Daten des Subjects ein:")
    subject1 = Person(
        input("Vorname:" ), 
        input("Nachname:" ), 
        input("Geschlecht (male or female):"), 
        int(input("Alter:")))

    # Build an experiment
    #experiment1 = build_experiment("First Experiment", "2024-04-05", supervisor1, subject1)
    print("Bitte geben Sie die Daten des Experiments ein:")
    experiment1 = Experiment(
        input("Experimentname:" ), 
        input("Datum:" ), 
        supervisor1, 
        subject1)

    #Print Experiment
    print(experiment1)

#Speichern der Datei
with open("Aufgabe61.json", "a") as outfile: 
    json.dump(experiment1.__dict__, outfile)
