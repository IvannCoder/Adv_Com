from rental import ElectricCar, Motorbike, Renter, Vehicle


def main():
    print("--- 1. Creating Vehicles and Renter ---")

    car = Vehicle("Toyota", "LEXUS", "YGN467758")
    ev = ElectricCar("Tesla", "Model Y", "MDY456721", 75)
    bike = Motorbike("Yamaha", "R15", "NPW456789", 155)
    renter = Renter("Siam Student", 1001)

    print(car)
    print(ev)
    print(bike)

    print("\n--- 2. Renting and Returning a Vehicle ---")

    car.rent()
    print("After rent():", car)

    car.return_vehicle()
    print("After return_vehicle():", car)

    print("\n--- 3. Testing Encapsulation & ValueError Validation ---")

    try:
        Renter("", 1002)
    except ValueError as e:
        print(f"Caught expected ValueError for empty name: {e}")

    try:
        Renter("John Doe", -15)
    except ValueError as e:
        print(f"Caught expected ValueError for negative license: {e}")

    print("\n--- 4. Polymorphism via Mixed List Loop ---")

    fleet = [car, ev, bike]

    for vehicle in fleet:
        print(vehicle)


if __name__ == "__main__":
    main()