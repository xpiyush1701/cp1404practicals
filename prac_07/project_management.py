"""
Expected Time: 40 Minutes
Actual Time: 60 Minutes
"""

import csv
from datetime import datetime

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n" \
       "U)pdate project\n(Q)uit"


def main():
    filename = "projects.txt"
    projects = load_projects(filename)

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects(filename)
            pass
        elif choice == "S":
            save_projects(projects, filename)
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name} (Start Date: {self.start_date.strftime('%d/%m/%Y')}, Priority: {self.priority}, " \
               f"Cost Estimate: {self.cost_estimate}, Completion Percentage: {self.completion_percentage}%)"


def load_projects(filename):
    projects = []
    with open(filename, "r") as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            project = Project(row['Name'], row['Start Date'], row['Priority'], row['Cost Estimate'],
                              row['Completion Percentage'])
            projects.append(project)
        return projects


def save_projects(filename, projects):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file,
                                fieldnames=['Name', 'Start Date', 'Priority', 'Cost Estimate', 'Completion Percentage'])
        writer.writeheader()
        for project in projects:
            writer.writerow({'Name': project.name, 'Start Date': project.start_date.strftime('%d/%m/%Y'),
                             'Priority': project.priority, 'Cost Estimate': project.cost_estimate,
                             'Completion Percentage': project.completion_percentage})


main()
