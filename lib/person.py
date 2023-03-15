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
    
    def __init__(self,name = "Louis",job = "Sales"):
        self.name = name
        self.job = job

    def name_getter(self):
        return self._name

    def name_setter(self,name):
        if(type(name) == str) and (1 <= len(name) <= 25):
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def job_getter(self):
        return self._job

    def job_setter(self,job):
        if (job in APPROVED_JOBS):
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    name = property(name_getter,name_setter,)
    job = property(job_getter,job_setter,)
