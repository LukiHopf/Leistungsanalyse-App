import json
from my_classes import Person, Subject

if __name__ == "__main__":

    # Build a Supervisor
    #supervisor1 = build_person("Lukas", "Höpflinger", "male", 21)
    print("Bitte geben Sie die Daten des Supervisors ein:")
    person = Person(
        input("Vorname:" ), 
        input("Nachname:" ))
        
    #Build a Subject
    #subject1 = build_person("Max", "Mustermann", "male", 25)
    print("Bitte geben Sie die Daten des Subjects ein:")
    subject1 = Subject(
        input("Vorname:" ), 
        input("Nachname:" ), 
        input("Geschlecht (male or female):"), 
        input("Geburtsdatum (Tag.Monat.Jahr):"),
        input("E-Mail:"))
    
    Subject.update_email(subject1)
    
    Person.put(person)


