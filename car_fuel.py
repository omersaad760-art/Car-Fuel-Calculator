class fuelCalculator:

    def calculate_fuel(self,distance_in_KM,consumption_per_100KM):
        if distance_in_KM <= 0 or consumption_per_100KM <= 0:
            raise ValueError("distance and consumption must be greater than zero")
        return (distance_in_KM * consumption_per_100KM) / 100

    def calculate_cost(self,fuel_litres,price_per_litre):
            if fuel_litres < 0 or price_per_litre < 0:
                raise ValueError("fuel litres and its price can not be negative")
            return (fuel_litres * price_per_litre ) 

    def calculate_consumption(self,distance_in_KM,used_fuel):
            if distance_in_KM <= 0 or used_fuel <= 0:
                raise ValueError("distance and fuel must be positive")
            return (used_fuel / distance_in_KM) * 100


def get_positive_number(message):
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print("enter a number greater than 0")
                continue
            return value
        except ValueError:
            print("invalid error enter a correct number")  
            
                  
def main():
    calculator = fuelCalculator()
    print("=" * 30)
    print("     fuel calculator")
    print("=" * 30)

    while True:
        print("\n choose an option:")
        print("1. calculate fuel needed and trip cost")
        print("2. calculate car consumption")
        print("3. exit")
        choice = input("enter 1,2 or 3: ").strip()

        if choice == "1":
            distance = get_positive_number("enter trip distance in KM: ")
            consumption = get_positive_number("car consumption: ")
            price = get_positive_number("price per litre: ")
            fuel = calculator.calculate_fuel(distance,consumption)
            cost = calculator.calculate_cost(fuel,price)
            print(f"\nfuel needed: {fuel:.1f} litres")
            print(f"trip cost: {cost:.1f}")

        elif choice == "2":
            distance = get_positive_number("driven distance in KM: ")
            used_fuel = get_positive_number("fuel used: ")
            consumption = calculator.calculate_consumption(distance,used_fuel)
            print(f"consuption is {consumption:.1f} L/100KM")

        elif choice == "3":
            print("exiting")
            break

        else:
            print("invalid choice ,enter 1,2 or 3")
             

if __name__ == "__main__":
    main()

             


    



        










