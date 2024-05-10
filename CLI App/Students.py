import re
from DataFile import Data
from Subjects import Subject
import random

class Student:
    def __init__(self) -> None:
        self.name = ""
        self.email = ""
        self.password = ""
        self.email_regex = r"(^[a-zA-Z]+\.+[a-zA-Z]+@+university+\.+com+$)"
        self.password_regex = r"(^[A-Z]+[a-z]{5,}+[0-9]{3,})"
        self.current_subjects = []
        self.data_initialise()

    def data_initialise(self):
        file_check = Data.check_file()
        if file_check:
            self.student_list = Data.read_data()

    def verify_credentials(self, email, password):
        verify_cred_result = True
        email_match = re.match(self.email_regex, email)
        password_match = re.match(self.password_regex, password)
        if not email_match or not password_match:
            verify_cred_result = False
        return verify_cred_result

    def verify_email(self, email):
        stu_found = False
        for student in self.student_list:
            if email.lower() == student["Email"].lower():
                self.name = student["Name"]
                stu_found = True
        return stu_found, self.name

    def generate_stud_id(self):
        ids = [student["Student_id"] for student in self.student_list]
        stud_id = str(random.randint(1,999999)).zfill(6)
        while stud_id in ids:
            stud_id = str(random.randint(1,999999)).zfill(6)
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
            self.name = input("\033[1;37m Name: ").title()
            self.id = self.generate_stud_id()
            self.new_student = {"Student_id":self.id, "Name": self.name, "Email": self.email, "Password":self.password, "Subjects":str([])}
            self.student_list.append(self.new_student)
            Data.write_data(self.student_list)
            print(f"\033[1;33m Enrolling Student {self.name}")
        #Display the student menu after registration
        self.student_menu()

    def login(self):
        self.email = input("\033[1;37m Email: ")
        self.password = input("\033[1;37m Password: ")
        login_verify = self.verify_credentials(self.email, self.password)
        stored_password = [student["Password"] for student in self.student_list if self.email.lower() == student["Email"].lower()]

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
            while stored_password[0] != self.password:
                print("\033[1;31m Password mismatch. Please enter correct password")
                self.password = input("\033[1;37m Password: ")
            self.current_subjects = [student["Subjects"] for student in self.student_list if self.email.lower() == student["Email"].lower()]
            if self.current_subjects[0]:
                self.current_subjects = eval(self.current_subjects[0])
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
        for student in self.student_list:
            if self.email.lower() == student["Email"].lower():
                student["Password"] = self.new_password
        Data.write_data(self.student_list)
        
    def remove_subject(self, sub_id):
        sub_found = False
        if len(self.current_subjects) >= 1:
            for subject in self.current_subjects:
                if sub_id == subject["id"]:
                    sub_found = True
                    idx = self.current_subjects.index(subject)
                    self.current_subjects.pop(idx)
                    for student in self.student_list:
                        if self.email.lower() == student["Email"].lower():
                            student["Subjects"] = str(self.current_subjects)
                    Data.write_data(self.student_list)
                    print(f"\t \033[1;33m Dropping Subject-{sub_id}\n\t  You are now enrolled in {len(self.current_subjects)} out of 4 subjects")
            if not sub_found:
                print(f"\t \033[1;31m Subject-{sub_id} not found in currently enrolled list of subjects")
        else:
            print("\t \033[1;31m There are no subjects currently enrolled")

#####Jay's part##############
    def enrol_subjects(self):
        if len(self.current_subjects) == 4:
            print("\t \033[1;31m You have already enrolled in the maximum number of subjects.\033[0m")
        else:
            # Add new Subject
            new_sub = Subject(self.current_subjects)
            new_subject = new_sub.assign_sub()
            # Add the subject to the student's enrolled subjects
            self.current_subjects.append(new_subject)
            for student in self.student_list:
                if self.email.lower() == student["Email"].lower():
                    student["Subjects"] = str(self.current_subjects)
            # Save the updated student data
            Data.write_data(self.student_list)
            # Print the enrolled subject details
            print(f"\t \033[1;33m Enrolling in Subject-{new_subject["id"]}", f"\n\t \033[1;33m You are now enrolled in {len(self.current_subjects)} out of 4 subjects")

    def view_enrolment(self):
        if self.current_subjects:
            print(f"\t \033[1;33m Showing {len(self.current_subjects)} subjects")
            for subj in self.current_subjects:
                print(f"\t \033[1;37m [ Subject:: {subj["id"]} -- mark = {subj["marks"]} -- grade =  {subj["grade"]} ]")
        else:
            print("\t \033[1;33m Showing 0 subjects")
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
                    subject_id = input("\t  Remove Subject by ID: ")
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
        exit(0)

    def student_helpmenu(self):
        print("Student Menu Options: \n(l) Login and access the student course menu \n(r) Register for new students to gain system access \n(x) Go back to University Menu")
    
    def student_sub_helpmenu(self):
        print("\t Student Course Menu Options: \n\t (c) Change login password \n\t (e) Enrol in new subjects \n\t (r) Remove a subject \n\t (s) View currently enrolled subjects and respective results \n\t (x) Sign Out and Go back to Student Menu")

if __name__ == "__main__":
    student = Student()
    student.student_menu()