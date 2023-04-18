
"""
În primul rând, vom defini o clasă numită Calendar, care va reprezenta calendarul nostru.
Clasa va avea metode pentru a adăuga un eveniment, a actualiza un eveniment, a șterge un eveniment și a afișa calendarul.
Vom utiliza modulele time și datetime pentru a afișa data și ora actuală.

Modulul pickle din Python este folosit pentru serializarea și deserializarea obiectelor Python.
Serializarea se referă la procesul de a transforma un obiect Python într-un format serializabil
(de exemplu, un șir de caractere sau un flux de octeți) astfel încât să poată fi stocat sau transmis prin rețea.
Deserializarea se referă la procesul de a transforma un format serializabil înapoi într-un obiect Python.
Modulul pickle oferă două funcții principale: dump() și load(). Funcția dump() serializează un obiect Python și îl
scrie într-un fișier deschis în mod binar. Funcția load() citește datele seriale dintr-un
fișier deschis în mod binar și le deserializează într-un obiect Python.
"""

import datetime
import os
import pickle

class Calendar:
    def __init__(self):
        self.events = {}

    def add_event(self, date, event):
        if date not in self.events:
            self.events[date] = [event]
        else:
            self.events[date].append(event)

    def update_event(self, date, old_event, new_event):
        if date in self.events:
            if old_event in self.events[date]:
                index = self.events[date].index(old_event)
                self.events[date][index] = new_event

    def delete_event(self, date, event):
        if date in self.events:
            if event in self.events[date]:
                self.events[date].remove(event)

    def print_calendar(self):
        print()
        for date in sorted(self.events.keys()):
            print(date)
            for event in self.events[date]:
                print("\t" + event)

    def save_calendar(self, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(self.events, f)

    def load_calendar(self, file_name):
        if os.path.exists(file_name):
            with open(file_name, 'rb') as f:
                self.events = pickle.load(f)

def get_date():
    while True:
        try:
            date_str = input("Enter date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return date
        except ValueError:
            print("Invalid date format. Please enter date in format YYYY-MM-DD.")

def get_event():
    return input("Enter event: ")

def main():
    calendar = Calendar()
    calendar.load_calendar("calendar.pickle")

    while True:
        print()
        print("Select an option:")
        print("1. View calendar")
        print("2. Add event")
        print("3. Update event")
        print("4. Delete event")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            calendar.print_calendar()

        elif choice == '2':
            date = get_date()
            event = get_event()
            calendar.add_event(date, event)
            calendar.save_calendar("calendar.pickle")

        elif choice == '3':
            date = get_date()
            old_event = get_event()
            new_event = get_event()
            calendar.update_event(date, old_event, new_event)
            calendar.save_calendar("calendar.pickle")

        elif choice == '4':
            date = get_date()
            event = get_event()
            calendar.delete_event(date, event)
            calendar.save_calendar("calendar.pickle")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == '__main__':
    main()
