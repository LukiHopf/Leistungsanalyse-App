import json
from my_functions import estimate_max_hr # zur Berechnung der max_hr


class Person(): # Klasse Person wird erstellt
    """Creating Class Person"""
    def __init__(self, first_name, last_name, sex, age):
            self.first_name = first_name
            self.last_name = last_name
            self.sex = sex
            self.__age = age
            # self.max_hr = estimate_max_hr(age, sex)

class Subject(Person): 
    """Subclass Subject wird erstellt --> benötigt max_hr"""
    def __init__(self, firstname, lastname, sex, age):
        super().__init__(firstname, lastname,sex, age)
        self.max_hr = estimate_max_hr(age, sex)
    
    def estimate_max_hr(age_years : int , sex : str) -> int:
  
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age_years
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age_years
        else:
        # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
    """Test
    def __init__(self, firstname, lastname, sex, age, max_hr):
        super().__init__(firstname, lastname,sex, age, max_hr)
       

    """

    def save(self):
        """Function to save Subject as DICT in JSON file"""
        with open("Subject_{}_{}.json".format(self.last_name, self.first_name),  "w") as outfile: # Vorname und Nachname werden als Dateiname verwendet
            json.dump(self.__dict__, outfile) # speichert die Daten als DICT in einer JSON Datei
 

class Supervisor(Person): # SUbclass Subject wird erstellt --> benötigt max_hr
    def __init__(self, firstname, lastname, sex, age):
        super().__init__(firstname, lastname,sex, age)

    def save(self):
        with open("Supervisor_{}_{}.json".format(self.last_name, self.first_name),  "w") as outfile: # Vorname und Nachname werden als Dateiname verwendet
            json.dump(self.__dict__, outfile) # speichert die Daten als DICT in einer JSON Datei
           

class Experiment(): # Klasse Experiment wird erstellt

    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
    
    def save(self):
        with open("Experiment_{}.json".format(self.experiment_name), "w") as outfile: # Experimentname wird als Dateiname verwendet
            json.dump(self.__dict__, outfile) # speichert die Daten als DICT in einer JSON Datei

