import pandas as pd
import os

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
"""
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
