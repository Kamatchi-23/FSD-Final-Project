import pandas as pd
class Data:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def read_data(self):
        student_data = pd.read_csv(self.file_path, sep=",")
        return student_data

    def write_data(self, data):
        data.to_csv(self.file_path, index=False, encoding='utf-8')
"""
if __name__ == "__main__":
    stud_data = Data()
    stud_data.read_data()
    stud_data.write_data("This is john")
    stud_data.read_data()

"""
