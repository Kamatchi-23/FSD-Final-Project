import re

class Student:
    def __init__(self) -> None:
        self.name = ""
        self.email = ""
        self.password = ""
        self.subjects = []
        self.student_accounts = []
        self.generate_stud_id()
    
    def generate_stud_id(self):
        pass
    def verify_credentials(self, email, password):
        email_regex = r"(^[a-zA-Z]+\.+[a-zA-Z]+@+university+\.+com+$)"
        email_match = re.match(email_regex, email)
        password_regex = r"()"
        password_match = re.match(password_regex, password)
        if not email_match or not password_match:
            return False
        else:
            return True

    def verify_account(self, email, password):
        if email == "john.smith@university.com":
            return True
        else:
            return False

    def register(self):
        self.email = input("Email: ")
        self.password = input("Password: ")
        #self.verify_credentials(self.email, self.password) to add
        print("email and password formats acceptable")
        self.name = input("Name: ")
        #self.generate_stud_id()
        print(f"Enrolling Student {self.name}")
        self.student_menu()

    def login(self):
        self.email = input("Email: ")
        self.password = input("Password: ")
        login_verify = self.verify_credentials(self.email, self.password)
        while not login_verify:
            print("Incorrect email or password format")
            self.email = input("Email: ")
            self.password = input("Password: ")
            login_verify = self.verify_credentials(self.email, self.password)
        print("email and password formats acceptable")
        account_verify = self.verify_account(self.email, self.password)
        if not account_verify:
            print("Student does not exist")
            self.student_menu()
        else:
            self.student_course_menu()

    def change_password(self):
        self.new_password = input("\t New Password: ")
        #verify_password()
        self.confirm_password = input("\t Confirm Password: ")
        while self.new_password != self.confirm_password:
            print("\t Password does not match. Try Again!")
            self.confirm_password = input("\t Confirm Password: ")
        self.password = self.new_password
        
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
        choice = input("\t Student Course Menu (c/e/r/s/x): ")
        while choice != "x":
            match choice:
                case 'c':
                    print("\t Updating Password")
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
            choice = input("\t Student Course Menu (c/e/r/s/x): ")
        print("\t Signed Out!! Back to Student Menu")
    
    
    def student_menu(self):
        choice = input("Student System (l/r/x): ")
        while choice != "x":
            match choice:
                case 'l':
                    print("Student Sign In")
                    self.login()
                case 'r':
                    print("Student Sign Up")
                    self.register()
                case _:
                    self.student_helpmenu()
            choice = input("Student System (l/r/x): ")
        print("Back to University Menu")

    def student_helpmenu(self):
        print("Student Menu Options: \n(l) Login and access the student course menu \n(r) Register for new students to gain system access \n(x) Go back to University Menu")
    
    def student_sub_helpmenu(self):
        print("\t Student Course Menu Options: \n\t (c) Change login password \n\t (e) Enrol in new subjects \n\t (r) Remove a subject \n\t (s) View currently enrolled subjects and respective results \n\t (x) Sign Out and Go back to Student Menu")

if __name__ == "__main__":
    student = Student()
    student.student_menu()