from car import Car
from employee import Employee
from office import Office


def main():
    office = Office("AI Hub")

    employees = [
        Employee(
            "Ali", 100, "neutral", 80, 1, Car("Toyota", 70), "ali@hub.com", 5000, 10
        ),
        Employee(
            "Sara", 150, "neutral", 90, 2, Car("BMW", 50), "sara@hub.com", 6000, 15
        ),
    ]

    for emp in employees:
        office.hire(emp)

    print(f"Total Employees: {Office.employeesNum}")

    for emp in employees:
        print(f"\nSimulating {emp.name}")
        emp.sleep(7)
        emp.eat(2)
        emp.buy(1)
        emp.drive()
        office.check_lateness(emp.id, moveHour=8)
        print(f"{emp.name}'s salary after lateness check: {emp.salary} L.E")


main()
