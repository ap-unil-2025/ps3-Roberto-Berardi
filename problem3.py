"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers (floats).
    """
    numbers = []
    while True:
        s = input("Enter a number: ").strip().lower()
        if s == "done":
            break
        try:
            numbers.append(float(s))
        except ValueError:
            print("Invalid input, please enter a number or 'done'.")
    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count, sum, average, minimum, maximum
    - even_count (only integers), odd_count (only integers)
    """
    if not numbers:
        return None

    count = len(numbers)
    total = sum(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)

    even_count = 0
    odd_count = 0
    for x in numbers:
        if float(x).is_integer():
            if int(x) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return {
        "count": count,
        "sum": total,
        "average": average,
        "minimum": minimum,
        "maximum": maximum,
        "even_count": even_count,
        "odd_count": odd_count,
    }


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.
    """
    if not analysis:
        return

    def fmt(x):
        return str(int(x)) if float(x).is_integer() else f"{x}"

    print("\nAnalysis Results:")
    print("-----------------")
    print(f"Count: {analysis['count']}")
    print(f"Sum: {fmt(analysis['sum'])}")
    print(f"Average: {analysis['average']:.2f}")
    print(f"Minimum: {fmt(analysis['minimum'])}")
    print(f"Maximum: {fmt(analysis['maximum'])}")
    print(f"Even numbers: {analysis['even_count']}")
    print(f"Odd numbers: {analysis['odd_count']}")


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    analysis = analyze_numbers(numbers)
    display_analysis(analysis)


if __name__ == "__main__":
    main()

# ci-touch
