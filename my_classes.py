import json
class Person():
    """Creates an object person"""

    #Konstruktor
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = str(sex)
        self.age = age
        self.max_hr = self.estimate_max_hr()

    #Funktion zur berechnung der maximalen Heartrate
    def estimate_max_hr(self):
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  self.age
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
    
    #Funktion welche die Daten als Dict in einer json-Datei speichert!
    def save(self):
        with open("Person_{}_{}".format(self.first_name, self.last_name), "a") as outfile: 
            json.dump(self.__dict__, outfile)
        


class Experiment():
    """Creates an object experiment"""

    #Konstruktor
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = str(date)
        self.supervisor = supervisor
        self.subject = subject

    #Funktion welche die Daten als Dict in einer json-Datei speichert!
    def save(self):
        with open("Experiment_{}".format(self.experiment_name), "a") as outfile:
            json.dump(self.__dict__, outfile)

