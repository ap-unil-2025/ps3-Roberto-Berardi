"""
Bonus Challenge: Password Generator
Generate secure passwords with customizable options.
"""

import random
import string


def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                      use_digits=True, use_special=True):
    """
    Generate a random password based on criteria.

    Returns:
        str: Generated password

    Raises:
        ValueError: if no character types are selected or length < selected types
    """
    pools = []
    if use_lowercase:
        pools.append(string.ascii_lowercase)
    if use_uppercase:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_special:
        pools.append(string.punctuation)

    if not pools:
        raise ValueError("No character types selected.")

    if length < len(pools):
        raise ValueError(f"Length must be at least {len(pools)} to include all selected types.")

    # 1) Guarantee at least one from each selected type
    password_chars = [random.choice(pool) for pool in pools]

    # 2) Fill remaining with combined pool
    combined = "".join(pools)
    password_chars.extend(random.choice(combined) for _ in range(length - len(password_chars)))

    # 3) Shuffle
    random.shuffle(password_chars)
    return "".join(password_chars)


def password_strength(password):
    """
    Rate password strength from 1-5:
      +1 length >= 8
      +1 length >= 12
      +1 has lowercase
      +1 has uppercase
      +1 has digits
    """
    score = 0
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1

    labels = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    return labels[min(score, 5)]


def main():
    print("Password Generator")
    print("-" * 30)

    length_input = input("Password length (default 12): ").strip()
    try:
        length = int(length_input) if length_input else 12
        if length <= 0:
            raise ValueError
        if length > 128:
            print("Length too large; capping to 128 for safety.")
            length = 128
    except ValueError:
        print("Invalid length. Using default 12.")
        length = 12

    try:
        password = generate_password(length, True, True, True, True)
        print(f"\nGenerated Password: {password}")
        print(f"Strength: {password_strength(password)}")

        print("\nAlternative passwords:")
        for i in range(3):
            alt = generate_password(length, True, True, True, True)
            print(f"{i+1}. {alt} ({password_strength(alt)})")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
