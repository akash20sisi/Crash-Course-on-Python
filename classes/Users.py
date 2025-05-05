class Users:


    def __init__(self,first_name,last_name, middle_name = '',profession = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name  = middle_name
        self.profession = profession
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user name is {self.first_name} {self.middle_name} {self.last_name}")

        if self.profession:
            print(f"The user profession is {self.profession}") 

        else:
            print("The user profession is not available")    

    def increment_login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0    

        
class Admin(Users):

    def __init__(self, first_name, last_name, middle_name='', profession=''):
        super().__init__(first_name, last_name, middle_name, profession)
        self.privileges = Privileges()

      

    
class Privileges:

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"The admin privileges are {self.privileges}")
    


user  = Users('Akash','Kumar',profession = 'Teacher')
user.describe_user()
user.increment_login_attempt()
user.increment_login_attempt()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

admin = Admin('Akash','kumar')
print(admin.privileges.show_privileges())


