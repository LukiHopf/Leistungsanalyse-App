import json
from my_functions import estimate_max_hr
# die Klassen Person und Experiment erstellen

class Person(): # Klasse Person wird erstellt
    
    def __init__(self, first_name, last_name, sex, age):
            self.first_name = first_name,
            self.last_name = last_name,
            self.sex = sex,
            self.age = age,
            self.max_hr = estimate_max_hr(age, sex)
    
    def save(self):
        with open("Person_{}_{}.json".format(self.last_name, self.first_name),  "w") as outfile: # Vorname und Nachname werden als Dateiname verwendet
            json.dump(self.__dict__, outfile) # speichert die Daten als DICT in einer JSON Datei

class Experiment(): # Klasse Experiment wird erstellt

    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name,
        self.date = date,
        self.supervisor = supervisor,
        self.subject = subject
    
    def save(self):
        with open("Experiment_{}.json".format(self.experiment_name), "w") as outfile: # Experimentname wird als Dateiname verwendet
            json.dump(self.__dict__, outfile) # speichert die Daten als DICT in einer JSON Datei

