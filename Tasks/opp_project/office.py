class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        return next((e for e in self.employees if e.id == empId), None)

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        self.employees = [e for e in self.employees if e.id != empId]
        Office.employeesNum -= 1

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp:
            is_late = Office.calculate_lateness(
                9, moveHour, emp.distanceToWork, emp.car.velocity
            )
        if is_late:
            self.deduct(empId, 10)
        else:
            self.reward(empId, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            return True
        arrival_hour = moveHour + (distance / velocity)
        return arrival_hour > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num
