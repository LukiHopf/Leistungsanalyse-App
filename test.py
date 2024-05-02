from my_classes import Person, Experiment, Supervisor, Subject
import json

person_1 = Subject("Markus", "Mitteregger", "male", "27.12.2000")

person_1.put()

person_1.update_email()