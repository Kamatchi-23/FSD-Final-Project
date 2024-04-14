import re

class Student:
    def __init__(self) -> None:
        self.name = "John Smith"
        self.email = ""
        self.password = ""
        self.email_regex = r"(^[a-zA-Z]+\.+[a-zA-Z]+@+university+\.+com+$)"
        self.password_regex = r"(^[A-Z]+[a-z]{5,}+[0-9]{3,})"
        self.subjects = []
        self.student_accounts = []
        self.generate_stud_id()
    
    def generate_stud_id(self):
        pass

    def verify_credentials(self, email, password):
        verify_cred_result = True
        email_match = re.match(self.email_regex, email)
        password_match = re.match(self.password_regex, password)
        if not email_match or not password_match:
            verify_cred_result = False
        return verify_cred_result

    def verify_account(self, email, password):
        if email == "john.smith@university.com":
            return True, self.name
        else:
            return False, self.name

    def register(self):
        self.email = input("\033[1;37m Email: ")
        self.password = input("\033[1;37m Password: ")
        register_verify = self.verify_credentials(self.email, self.password)
        while not register_verify:
            print("\033[1;31m Incorrect email or password format")
            self.email = input("\033[1;37m Email: ")
            self.password = input("\033[1;37m Password: ")
            register_verify = self.verify_credentials(self.email, self.password)
        print("\033[1;33m email and password formats acceptable")
        self.account_verify, self.name = self.verify_account(self.email, self.password)
        if self.account_verify:
            print(f"\033[1;31m Student {self.name} already exists")
        else:
            self.name = input("\033[1;37m Name: ")
            #self.generate_stud_id()
            print(f"\033[1;33m Enrolling Student {self.name}")
        self.student_menu()

    def login(self):
        self.email = input("\033[1;37m Email: ")
        self.password = input("\033[1;37m Password: ")
        login_verify = self.verify_credentials(self.email, self.password)
        while not login_verify:
            print("\033[1;31m Incorrect email or password format")
            self.email = input("\033[1;37m Email: ")
            self.password = input("\033[1;37m Password: ")
            login_verify = self.verify_credentials(self.email, self.password)
        print("\033[1;33m email and password formats acceptable")
        self.account_verify, self.name = self.verify_account(self.email, self.password)
        if not self.account_verify:
            print("\033[1;31m Student does not exist")
            self.student_menu()
        else:
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