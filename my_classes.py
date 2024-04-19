import json
# die Klassen Person und Experiment erstellen

class Person(): # Klasse Person wird erstellt
    
    def __init__(self, first_name, last_name, sex, age):
            self.first_name = first_name,
            self.last_name = last_name,
            self.sex = sex,
            self.age = age,
            self.max_hr = self.estimate_max_hr()

    # aus my_functions.py kopiert und bei sex und age .self hinzugefügt da es nun in einer Klasse arbeitet
    def estimate_max_hr(self) -> int:
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  self.age
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)

    def save(self):
        with open("Person_{}{}_.json".format(self.last_name, self.first_name),  "a") as outfile: # Vorname und Nachname werden als Dateiname verwendet
            json.dump(self.__dict__, outfile) # speichert die Daten als DICT in einer JSON Datei

class Experiment(): # Klasse Experiment wird erstellt

    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name,
        self.date = date,
        self.supervisor = supervisor,
        self.subject = subject
    
    def save(self):
        with open("Experiment_{}.json".format(self.experiment_name), "a") as outfile: # Experimentname wird als Dateiname verwendet
            json.dump(self.__dict__, outfile) # speichert die Daten als DICT in einer JSON Datei

