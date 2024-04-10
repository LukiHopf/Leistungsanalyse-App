import json

if __name__ == "__main__":
    from my_functions import build_person, build_experiment

    # Build a Supervisor
    #supervisor1 = build_person("Lukas", "Höpflinger", "male", 21)
    print("Bitte geben Sie die Daten des Supervisors ein:")
    supervisor1 = build_person(input("Vorname:" ), input("Nachname:" ),  input("Geschlecht (englisch):"), int(input("Alter:")))
    
    #Build a Subject
    #subject1 = build_person("Max", "Mustermann", "male", 25)
    print("Bitte geben Sie die Daten des Subjects ein:")
    subject1 = build_person(input("Vorname:" ), input("Nachname:" ),  input("Geschlecht (englisch):"), int(input("Alter:")))

    # Build an experiment
    #experiment1 = build_experiment("First Experiment", "2024-04-05", supervisor1, subject1)
    print("Bitte geben Sie die Daten des Experiments ein:")
    experiment1 = build_experiment(input("Experimentname:" ), input("Datum:" ), supervisor1, subject1)

    #Print Experiment
    print(experiment1)

#Speichern der Datei
with open("test.json", "a") as outfile: 
    json.dump(experiment1, outfile)
