if __name__ == "__main__":
    from my_functions import build_person, build_experiment

    # Build a Supervisor
    supervisor1 = build_person("Lukas", "Höpflinger", "male", 21)
    
    #Build a Subject
    subject1 = build_person("Max", "Mustermann", "male", 25)

    # Build an experiment
    experiment1 = build_experiment("First Experiment", "2024-04-05", supervisor1, subject1)

    #Print Experiment
    print(experiment1)
