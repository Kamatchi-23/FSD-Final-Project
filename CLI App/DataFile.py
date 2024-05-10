import csv
import os

file_path = "CLI App/Students.csv"
headers = ["Student_id", "Name", "Email", "Password", "Subjects"]

class Data:
    @staticmethod
    def check_file():
        try:
            if not os.path.exists(file_path):
                with open(file_path, mode='w', newline='') as file:
                    writerfile = csv.DictWriter(file, fieldnames=headers)
                    writerfile.writeheader()
            return True
        except FileExistsError:
            print("\033[1;31m Issue in creating student data file")
            return False
    @staticmethod
    def read_data():
        students_lst = []
        with open(file_path, mode='r') as file:
            student_data = csv.DictReader(file)
            for data in student_data:
                students_lst.append(data)
        return students_lst
    @staticmethod
    def write_data(data):
        with open(file_path, mode='w', newline='') as file:
            writerfile = csv.DictWriter(file, fieldnames=headers)
            writerfile.writeheader()
            writerfile.writerows(data)

"""
if __name__ == "__main__":
    stud_data = Data()
    file_check = stud_data.check_file()
    print(file_check)
    if file_check:
        data = stud_data.read_data()
        print(data)
        stud_data.write_data([{"Student_id": "349102", "Name": "John Smith", "Email": "john.smith@university.com", "Password":"Qwerty1234", "Subjects": [{'id': '001', 'marks': 75, 'grade': 'D'}, {'id': '030', 'marks': 90, 'grade': 'HD'}, {'id': '035', 'marks': 70, 'grade': 'C'}]}, 
                              {"Student_id": "349102", "Name": "John Smith", "Email": "john.smith@university.com", "Password":"Qwerty1234", "Subjects": [{'id': '001', 'marks': 75, 'grade': 'D'}, {'id': '030', 'marks': 90, 'grade': 'HD'}, {'id': '035', 'marks': 70, 'grade': 'C'}]}])
        stud_data.read_data()
"""