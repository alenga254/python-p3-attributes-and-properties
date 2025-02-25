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
    def __init__(self, name="joe", job="ITC"):
        self.name = name
        self.job = job
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) != str:
            print("Name must be string between 1 and 25 characters.")
        elif len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
        
            self._name = name.title()

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, job):
        if type(job) != str:
            print("Job must be in list of approved jobs.")
        elif job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = job

    job = property(get_job, set_job)

    pass
