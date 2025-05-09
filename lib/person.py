#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name: str = "Unknown", job: str = "Admin"):
        self.name = name
        self.job = job

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        if not isinstance(new_name, str) or not (1 <= len(new_name.strip()) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = new_name.strip().title()

    @property
    def job(self) -> str:
        return self._job
    
    @job.setter
    def job(self, new_job: str):
        if new_job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = new_job
