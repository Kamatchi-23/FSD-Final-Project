import pandas as pd

class Data:
    def __init__(self) -> None:
        self.file_path = "CLI App\student.data"

    def read_data(self):
        student_data = pd.read_csv(self.file_path, sep=",")
        student_data.head()
    def write_data(self, data):
        data.to_csv(self.file_path)

if __name__ == "__main__":
    data = Data()
    data.read_data()
    
"""
# Open the file
file = open(, 'r')

# Read the file
content = file.read()
print(content)
# Close the file
file.close()
"""
