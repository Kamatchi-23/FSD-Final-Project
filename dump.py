#import pandas as pd
import pickle
import os

file_path = "./students_copy.data"
class Data:

    @staticmethod
    def check_file():
        if not os.path.exists(file_path):
            file = open(file_path, "wb")
            pickle.dump("Student_id;Name;Email;Password;Subjects", file)
            file.close()
        return True
    
    @staticmethod
    def read_data():
        with open(file_path, 'rb') as file:
            student_data = pickle.load(file)
        return student_data
    
    @staticmethod
    def write_data(data):
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)

if __name__ == "__main__":
    stud_data = Data()
    file_check = stud_data.check_file()
    print(file_check)
    if file_check:
        data = stud_data.read_data()
        print(data)
        stud_data.write_data("349102;John Smith;john.smith@university.com;Qwerty1234;[{'id': '001', 'marks': 75, 'grade': 'D'}, {'id': '030', 'marks': 90, 'grade': 'HD'}, {'id': '035', 'marks': 70, 'grade': 'C'}]")
        stud_data.read_data()



            
"""
class Data:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
    
    def check_file(self):
        if not os.path.exists(self.file_path):
            file = open(self.file_path, "a")
            file.write("Student_id;Name;Email;Password;Subjects")
        return True

    def read_data(self):
        student_data = pd.read_csv(self.file_path, sep=";")
        return student_data

    def write_data(self, data):
        data.to_csv(self.file_path, index=False, sep=";")

if __name__ == "__main__":
    stud_data = Data("CLI App\\student.data")
    file_check = stud_data.check_file()
    print(file_check)
    if file_check:
        data = stud_data.read_data()
        print(data)
        #stud_data.write_data("This is john")
        #stud_data.read_data()
"""
