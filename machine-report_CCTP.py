"""
Made by Noga Levy in 2025. Will come back to finish this later.
"""

total_info = {0: ["Sarah", 1, "Login", "Dec 27, 2024"], 1: ["Sarah", 1, "Logout", "Dec 27, 2024"]}


class Event:
    def __init__(self, user: str, machine: int, event: str, date: str) -> None:
        self.user = user  # Person who used the machine
        self.machine_num = machine  # Machine used
        self.event_type = event  # The types are "login" and "log out"
        self.date = date  # Date machine was used by person

    def report(self):
        return f"Person: {self.user}\nMachine number: {self.machine_num}\nAction: {self.event_type}\nDate: {self.date}"


for i in range(0, len(total_info)):
    ev = Event(total_info[i][0], total_info[i][1], total_info[i][2], total_info[i][3])
    print(ev.report() + "\n")
