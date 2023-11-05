"""
Expected Time: 40 Minutes
Actual Time:
"""

import csv
from datetime import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name} (Start Date: {self.start_date.strftime('%d/%m/%Y')}, Priority: {self.priority}, " \
               f"Cost Estimate: {self.cost_estimate}, Completion Percentage: {self.completion_percentage}%)"
