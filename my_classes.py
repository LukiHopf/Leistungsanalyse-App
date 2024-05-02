import json
from datetime import date
import requests

class Person():
    """Creates an object person"""

    #Konstruktor
    def __init__(self, first_name, last_name, sex, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = str(sex)
        self.__date_of_birth = str(date_of_birth)
        self.age = self.calc_age()
        
    def calc_age(self):
        """Calculates the age of an Subject with the date of birth"""
        today = date.today()
        date_list = self.__date_of_birth.split(".")
        birth_date_day = int(date_list[0])
        birth_date_month = int(date_list[1])
        birth_date_year = int(date_list[2])
        return today.year - birth_date_year - ((today.month, today.day) < (birth_date_month, birth_date_day))
    
    def put(self):
        #URL für den Webserver
        url = "http://127.0.0.1:5000/person/"
        #Erstellen der Daten:
        data = {"name" : self.first_name}
        #Daten in eine json-Datei konvertieren:
        data_json = json.dumps(data)
        #Senden der Daten an den Webserver --> Post request / Ausgabe der Antwort des Webservers
        response = requests.post(url, data = data_json ) 
        print(response.text )

    def delete(self):
        url = "http://127.0.0.1:5000/person/" + self.first_name
        response = requests.delete(url)  
        print(response.text)
    
    def get(self):
        url = "http://127.0.0.1:5000/person/" + self.first_name
        response = requests.get(url)
        print(response.text)


class Supervisor(Person):
    """Creates an Object Supervisor"""        
    def __init__(self, first_name, last_name, sex, date_of_birth):
        super().__init__(first_name, last_name, sex, date_of_birth)

    #Funktion welche die Daten als Dict in einer json-Datei speichert!
    def save(self):
        with open("Supervisor_{}_{}.json".format(self.first_name, self.last_name), "a") as outfile: 
            json.dump(self.__dict__, outfile)


class Subject(Person):
    def __init__(self, first_name, last_name, sex, date_of_birth):
        super().__init__(first_name, last_name, sex, date_of_birth)
        self.max_heart_rate = self.estimate_max_hr()
        self.email = "{}.{}@oida.at".format(self.first_name, self.last_name)

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
        with open("Subject_{}_{}.json".format(self.first_name, self.last_name), "a") as outfile: 
            json.dump(self.__dict__, outfile)

    def update_email(self):
        #URL für den Webserver inkluse Verweis auf die jeweilige Person
        url = "http://127.0.0.1:5000/person/"+ self.first_name
        #Erstellen der Daten:
        data = {"email" : self.email,
                "age" : self.age}
        #Daten in eine json-Datei konvertieren:
        data_json = json.dumps(data)
        #Senden der Daten an den Webserver --> Put request / Ausgabe der Antwort des Webservers
        response = requests.put(url, data = data_json) 
        print(response.text)
    

class Experiment():
    """Creates an object experiment"""

    #Konstruktor
    def __init__(self, experiment_name, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = "{}.{}.{}".format(str(date.today().day), str(date.today().month), str(date.today().year))
        self.supervisor = supervisor
        self.subject = subject

    #Funktion welche die Daten als Dict in einer json-Datei speichert!
    def save(self):
        with open("Experiment_{}.json".format(self.experiment_name), "a") as outfile:
            json.dump(self.__dict__, outfile)

##Testen der Programme
