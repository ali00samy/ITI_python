class Car:
    def __init__(self, name, fuelRate, velocity=0):
        self.name = name
        self.fuelRate = min(max(fuelRate, 0), 100)
        self.velocity = min(max(velocity, 0), 200)

    def run(self, velocity, distance):
        self.velocity = min(max(velocity, 0), 200)
        consumed_fuel = distance * 0.1
        if self.fuelRate <= 0:
            self.stop(distance)
            return
        if consumed_fuel >= self.fuelRate:
            distance_driven = self.fuelRate / 0.1
            remaining_distance = distance - distance_driven
            self.fuelRate = 0
            self.stop(remaining_distance)
        else:
            self.fuelRate -= consumed_fuel
            self.stop(0)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            print(
                f"The car stopped before reaching the destination. {remaining_distance:.2f} km left."
            )
        else:
            print("You have arrived at your destination.")
