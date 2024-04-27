"""
class Subject:
    def __init__(self, stud_id) -> None:
        self.student_id = stud_id

    def generate_sub_id(self):
        pass
    def generate_marks(self):
        pass
    def assign_grade(self, marks):
        pass
"""
import random

class Subject:
    def __init__(self, current_sub) -> None: 
        self.subs = current_sub           
        self.sub = dict.fromkeys(["id", "marks", "grade"])
        
    def assign_sub(self):
        ids = [sub["id"] for sub in self.subs if self.subs]
        new_id = str(random.randint(1, 999)).zfill(3)
        while new_id in ids:
            new_id = str(random.randint(1, 999)).zfill(3)
        self.sub["id"] = new_id
        self.sub["marks"] = random.randint(25, 100)
        self.sub["grade"] = self.calculate_grade(self.sub["marks"])
        return self.sub

    
    def calculate_grade(self, mark):
        if mark < 50:
            return 'Z'
        elif mark < 65:
            return 'P'
        elif mark < 75:
            return 'C'
        elif mark < 85:
            return 'D'
        else:
            return 'HD'
