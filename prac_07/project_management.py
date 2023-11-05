"""
Expected Time: 40 Minutes
Actual Time:
"""

import csv
from datetime import datetime


def main():
    filename = "projects.txt"
    projects = load_projects(filename)


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
