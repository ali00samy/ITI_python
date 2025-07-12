from person import Person


class Employee(Person):
    def __init__(
        self, name, money, mood, healthRate, id, car, email, salary, distanceToWork
    ):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = max(salary, 1000)
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours > 8:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def drive(self):
        self.car.run(60, self.distanceToWork)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = min(self.car.fuelRate + gasAmount, 100)

    def send_mail(self, to, subject, body):
        print(f"Sending email to: {to}\nSubject: {subject}\nBody: {body}")
