class Company:
    def __init__(self, name, business_type, employees=None):
        self.__name =name
        self.__business_type = business_type
        if employees == None:
            self.__employees = []
        else:
            self.__employees = employees

    def get_name(self):
        return self.__name

    def add_employee(self,employee):
        self.__employees.append(employee)

    def remove_employee(self,employee):
        self.__employees.remove(employee)
    def __str__(self):
        return (f"Company: {self.__name}, \nBusiness Type: {self.__business_type}\
                \nEmployees:{[emp.get_name() for emp in self.__employees]}")


class Person:
    def __init__(self, name, age, residence, employer):
        self.__name = name
        self.__age = age
        self.__residence = residence
        self.__employer = employer

    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name

    def get_residence(self):
        return self.__residence

    def get_employer(self):
        return self.__employer

    def set_employer(self,new_employer):
        self.__employer= new_employer

    def move(self,new_residence):
        self.__residence = new_residence

    def __str__(self):
        if self.__employer == None:
            employer_str = "Not employed"

        else:
            employer_str = self.__employer.get_name()
        return (f"Person: {self.__name}, Age: {self.__age}, Residence:{self.__residence}, Employer: {employer_str}")


company1 = Company("TechCorp", "Tech")
person1 = Person("John Doe", 30, "Paris",company1)
person2 = Person("Mac joe",23,"Nice",company1)
print(person1)
print(person2)
company1.add_employee(person1)
company1.add_employee(person2)
print(company1)
company1.remove_employee(person2)
print(company1)
print(person2)