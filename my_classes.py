import json
from my_functions import estimate_max_hr # zur Berechnung der max_hr
import requests
import datetime

class Person(): # Klasse Person wird erstellt
    """Creating Class Person"""
    def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name
            # self.max_hr = estimate_max_hr(age, sex)
    #mit put wird die bestehende Person geändert    
    def put(self):
        url = "http://127.0.0.1:5000/person/{}".format(self.first_name)
        # Define the data you want to send
        data = {
            "name": self.last_name
        }
        data_json = json.dumps(data)
        response = requests.put(url, data=data_json)
        print(response.text)

class Subject(Person): 
    """Subclass Subject wird erstellt --> benötigt max_hr"""
    def __init__(self, firstname, lastname, sex, birthdate, email):
        super().__init__(firstname, lastname)
        self.sex = sex
        self.age = self.calculate_age(birthdate)
        self.__birthdate = birthdate
        self.max_hr = estimate_max_hr(self.age, sex)
        self.email = email

    def calculate_age(self, birthdate):
        today = datetime.date.today()
        birthdate = datetime.datetime.strptime(birthdate, "%d.%m.%Y").date()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age 

    def estimate_max_hr(age_years : int , sex : str) -> int:
  
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age_years
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age_years
        else:
        # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
    #mit post wird eine neue person erstellt
    def update_email(self):
        url = "http://127.0.0.1:5000/person/"
        data = {
            "name": self.first_name,
            "email": self.email
            }
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json)
        print(response.text)

    def save(self):
        """Function to save Subject as DICT in JSON file"""
        with open("Subject_{}_{}.json".format(self.last_name, self.first_name),  "w") as outfile: # Vorname und Nachname werden als Dateiname verwendet
            json.dump(self.__dict__, outfile) # speichert die Daten als DICT in einer JSON Datei
 

class Supervisor(Person): # Subclass Subject wird erstellt --> benötigt max_hr
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)


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

