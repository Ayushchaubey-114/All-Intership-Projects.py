while True:
    print("\n--- Conversion Menu ---")
    print("1. Distance (Km to Mile / Mile to Km)")
    print("2. Speed (Km/h to m/s / m/s to Km/h)")
    print("3. Currency (INR to USD / USD to INR)")
    print("4. Fahrenheit to Celsius")
    print("5. Exit")

    option = int(input("Select an option: "))

    if option == 1:
        print("\n1. Kilometer to Mile")
        print("2. Mile to Kilometer")
        choice = int(input("Enter choice: "))
        if choice == 1:
            km = float(input("Enter Km: "))
            print(f"{km} Km = {km * 0.621371:} Miles")
        else:
            miles = float(input("Enter Miles: "))
            print(f"{miles} Miles = {miles / 0.621371:} Km")

    elif option == 2:
        print("\n1. Km/h to m/s")
        print("2. m/s to Km/h")
        choice = int(input("Enter choice: "))
        if choice == 1:
            kmh = float(input("Enter Km/h: "))
            print(f"{kmh} Km/h = {kmh / 3.6:.2f} m/s")
        else:
            ms = float(input("Enter m/s: "))
            print(f"{ms} m/s = {ms * 3.6:.2f} Km/h")

    elif option == 3:
        print("\n1. INR to USD")
        print("2. USD to INR")
        choice = int(input("Enter choice: "))
        rate = 0.012
        if choice == 1:
            inr = float(input("Enter ₹: "))
            print(f"₹{inr} = ${inr * rate:.2f}")
        else:
            usd = float(input("Enter $: "))
            print(f"${usd} = ₹{usd / rate:.2f}")

    elif option == 4:
        f = float(input("Enter Fahrenheit: "))
        print(f"{f}°F = {(f - 32) * 5/9:.2f}°C")

    elif option == 5:
        print("Exiting...")
        break

    else:
        print("Invaild option. Please try again.")
