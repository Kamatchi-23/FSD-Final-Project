import re
from DataFile import Data
import pandas as pd
import random

class Student:
    def __init__(self) -> None:
        self.name = ""
        self.email = ""
        self.password = ""
        self.email_regex = r"(^[a-zA-Z]+\.+[a-zA-Z]+@+university+\.+com+$)"
        self.password_regex = r"(^[A-Z]+[a-z]{5,}+[0-9]{3,})"
        self.subjects = []
        self.file = Data("CLI App\\student.data")
        self.student_df = self.read_accounts()

    def verify_credentials(self, email, password):
        verify_cred_result = True
        email_match = re.match(self.email_regex, email)
        password_match = re.match(self.password_regex, password)
        if not email_match or not password_match:
            verify_cred_result = False
        return verify_cred_result

    def read_accounts(self):
        student_data = Data.read_data(self.file)
        student_data = student_data.astype(str, errors="ignore")
        return student_data

    def verify_email(self, email):
        emails = [x.lower() for x in list(self.student_df["Email"])]
        if email.lower() in emails:
            stud_rec = self.student_df[self.student_df["Email"].str.contains(email, case=False)]
            self.name = stud_rec.Name.values[0]
            return True, self.name
        else:
            return False, self.name

    def prefix_zero(self, id):
        len_id = len(id)
        id = id.zfill(6) if len_id < 6 else id
        return id

    def generate_stud_id(self):
        ids = list(self.student_df["student_id"])
        stud_id = str(random.randint(1,999999))
        stud_id = self.prefix_zero(stud_id)
        while stud_id in ids:
            stud_id = str(random.randint(1,999999))
            stud_id = self.prefix_zero(stud_id)
        return stud_id

    def register(self):
        """
        Student details registration includes the below steps:
        1. Obtaining the user credentials - email and password
        2. Verifying if the credentials match the given pattern requirements
        3. Ask for credentials until the pattern specifications match
        4. Check if the given email has been already registered
        5. Only if the email is not registered, the student id is generated and provided details are stored in student.data file
        6. Student menu is displayed for the user to navigate to other options (l/r/x)
        """
        #Getting the credentials from user as input
        self.email = input("\033[1;37m Email: ")
        self.password = input("\033[1;37m Password: ")
        #Verify if the credentials satisfy the given pattern conditions
        register_verify = self.verify_credentials(self.email, self.password)
        while not register_verify:
            print("\033[1;31m Incorrect email or password format")
            self.email = input("\033[1;37m Email: ")
            self.password = input("\033[1;37m Password: ")
            register_verify = self.verify_credentials(self.email, self.password)
        print("\033[1;33m email and password formats acceptable")
        #Check if student email has already been registered
        email_verify, self.name = self.verify_email(self.email)
        if email_verify:
            print(f"\033[1;31m Student {self.name} already exists")
        #If not registered, generate the unique student id and store the student details to the data file
        else:
            self.name = input("\033[1;37m Name: ")
            self.id = self.generate_stud_id()
            self.new_student_df = pd.DataFrame([[self.id, self.name, self.email, self.password, []]], columns=list(self.student_df.columns))
            self.student_df = self.student_df._append(self.new_student_df, ignore_index=True)
            Data.write_data(self.file, self.student_df)
            print(f"\033[1;33m Enrolling Student {self.name}")
        #Display the student menu after registration
        self.student_menu()

    def login(self):
        self.email = input("\033[1;37m Email: ")
        self.password = input("\033[1;37m Password: ")
        login_verify = self.verify_credentials(self.email, self.password)
        self.stored_password = self.student_df.loc[self.student_df["Email"].str.contains(self.email, case=False), "Password"]

        while not login_verify:
            print("\033[1;31m Incorrect email or password format")
            self.email = input("\033[1;37m Email: ")
            self.password = input("\033[1;37m Password: ")
            login_verify = self.verify_credentials(self.email, self.password)
        print("\033[1;33m email and password formats acceptable")
        email_verify, self.name = self.verify_email(self.email)
        if not email_verify:
            print("\033[1;31m Student does not exist")
            self.student_menu()
        else:
            while self.stored_password.values[0] != self.password:
                print("\033[1;31m Password mismatch. Please enter correct password")
                self.password = input("\033[1;37m Password: ")
            self.student_course_menu()

    def change_password(self):
        self.new_password = input("\t \033[1;37m New Password: ")
        password_match = re.match(self.password_regex, self.new_password)
        while not password_match:
            print("\t \033[1;31m Incorrect password format.")
            self.new_password = input("\t \033[1;37m New Password: ")
            password_match = re.match(self.password_regex, self.new_password)
        self.confirm_password = input("\t \033[1;37m Confirm Password: ")
        while self.new_password != self.confirm_password:
            print("\t \033[1;31m Password does not match. Try Again!")
            self.confirm_password = input("\t \033[1;37m Confirm Password: ")
        self.stored_password = self.new_password
        stu_id = self.student_df.loc[self.student_df["Email"].str.contains(self.email, case=False), "student_id"].values[0]
        self.student_df.loc[self.student_df["Email"].str.contains(self.email, case=False), "student_id"] = self.prefix_zero(stu_id)
        Data.write_data(self.file, self.student_df)
        
    def remove_subject(self, sub_id):
        pass

#####Jay's part##############
    def enrol_subjects(self):
        pass
    def assign_results(self):
        pass
    def view_enrolment(self):
        pass
##############################

    def student_course_menu(self):
        choice = input("\t \033[1;36m Student Course Menu (c/e/r/s/x): \033[1;37m")
        while choice != "x":
            match choice:
                case 'c':
                    print("\t \033[1;33m Updating Password")
                    self.change_password()
                case 'e':
                    self.enrol_subjects()
                case 'r':
                    subject_id = int(input("\t Remove Subject by ID: "))
                    self.remove_subject(subject_id)
                case 's':
                    self.view_enrolment()
                case _:
                    self.student_sub_helpmenu()
            choice = input("\t \033[1;36m Student Course Menu (c/e/r/s/x): \033[1;37m")
        print("\t \033[1;37m Signed Out!! Back to Student Menu")
    
    
    def student_menu(self):
        choice = input("\033[1;36m Student System (l/r/x): \033[1;37m")
        while choice != "x":
            match choice:
                case 'l':
                    print("\033[1;32m Student Sign In")
                    self.login()
                case 'r':
                    print("\033[1;32m Student Sign Up")
                    self.register()
                case _:
                    self.student_helpmenu()
            choice = input("\033[1;36m Student System (l/r/x): \033[1;37m")
        print("\033[1;37m Back to University Menu")

    def student_helpmenu(self):
        print("Student Menu Options: \n(l) Login and access the student course menu \n(r) Register for new students to gain system access \n(x) Go back to University Menu")
    
    def student_sub_helpmenu(self):
        print("\t Student Course Menu Options: \n\t (c) Change login password \n\t (e) Enrol in new subjects \n\t (r) Remove a subject \n\t (s) View currently enrolled subjects and respective results \n\t (x) Sign Out and Go back to Student Menu")

if __name__ == "__main__":
    student = Student()
    student.student_menu()