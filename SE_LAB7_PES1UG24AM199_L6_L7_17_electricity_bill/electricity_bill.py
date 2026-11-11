
RATES = {"DOM": 3, "COM": 6}
SLAB = {"A": 1, "B": 2}


def units_consumed(reading):
    if not isinstance(reading, str):
        raise ValueError("Meter reading must be a string")

    parts = reading.split(':')

    if len(parts) != 2:
        raise ValueError("Enter readings as previous:current")

    try:
        previous = int(parts[0].strip())
        current = int(parts[1].strip())
    except ValueError:
        raise ValueError("Meter readings must be integers")

    if previous < 0 or current < 0:
        raise ValueError("Meter readings cannot be negative")

    if current < previous:
        raise ValueError("Current reading cannot be less than previous reading")

    return current - previous


def daily_average(units_csv):
    if not isinstance(units_csv, str) or not units_csv.strip():
        raise ValueError("Daily units cannot be empty")

    try:
        units = [int(u.strip()) for u in units_csv.split(',')]
    except ValueError:
        raise ValueError("Daily units must contain valid integers")

    if any(u < 0 for u in units):
        raise ValueError("Daily units cannot be negative")

    return round(sum(units) / len(units), 2)


def tariff_rate(code):
    if not isinstance(code, str):
        raise ValueError("Tariff code must be a string")

    parts = code.strip().split('-')

    if len(parts) != 2:
        raise ValueError("Tariff code must be CATEGORY-SLAB")

    category, slab = parts[0].strip().upper(), parts[1].strip().upper()

    if category not in RATES:
        raise ValueError("Invalid tariff category")

    if slab not in SLAB:
        raise ValueError("Invalid tariff slab")

    return RATES[category] * SLAB[slab]


def main():
    print("==== Running units_consumed ====")
    user_input = input(
        "Enter meter readings as previous:current (e.g. 1200:1350): "
    )
    try:
        result = units_consumed(user_input)
        print("Units Consumed:", result)
    except ValueError as error:
        print("Invalid input:", error)

    print("\n==== Running daily_average ====")
    user_input = input("Enter daily units as CSV (e.g. 5,7,6): ")
    try:
        result = daily_average(user_input)
        print("Daily Average:", result)
    except ValueError as error:
        print("Invalid input:", error)

    print("\n==== Running tariff_rate ====")
    user_input = input("Enter a tariff code (e.g. DOM-A): ")
    try:
        result = tariff_rate(user_input)
        print("Rate per Unit:", result)
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
