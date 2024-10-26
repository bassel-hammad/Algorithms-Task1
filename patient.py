# patient.py
class Patient:
    def __init__(self, id, name, arrival_time, departure_time, severity):
        self.id = id
        self.name = name
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.severity = severity
