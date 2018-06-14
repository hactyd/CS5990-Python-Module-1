
class Employee:
    numberofE = 0
    totSal = 0
    def __init__(self, n, f, s, d):

        self.family = f
        self.salary = s
        self.department = d
        Employee.numberofE += 1
        Employee.totSal += self.salary

    def avg_sal(self):
        print("Average salary: " + str(Employee.totSal/Employee.numberofE))


class FullTimeEmployee(Employee):
    def __init__(self, n, f, s, d):
        Employee.__init__(self, n, f, s, d)





employ1 = Employee("Jack", "Lastly", 10.0, "Computer")
employ2 = FullTimeEmployee("Johnny", "Kuzko", 10.0, "Electrical")
employ3 = FullTimeEmployee('JJ', "Chad", 50.0, 'Math')
employ4 = Employee('Hope', "Destiny", 60.0, "Art")


