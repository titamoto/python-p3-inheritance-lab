#!/usr/bin/env python

from user import User

class Student(User):
    
    knowledge = []
    
    def learn(self, lesson):
        self.knowledge.append(lesson)