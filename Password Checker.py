import re

def password_strength_checker(password):
    """
    Evaluate the strength of a password based on length, complexity, and patterns.
    """
    strength = 0
    recommendations = []

    # Check password length
    if len(password) < 8:
        recommendations.append("Increase the password length to at least 8 characters.")
    else:
        strength += 1

    # Check for uppercase characters
    if not re.search(r"[A-Z]", password):
        recommendations.append("Add at least one uppercase letter.")
    else:
        strength += 1

    # Check for lowercase characters
    if not re.search(r"[a-z]", password):
        recommendations.append("Add at least one lowercase letter.")
    else:
        strength += 1

    # Check for digits
    if not re.search(r"\d", password):
        recommendations.append("Include at least one numeric digit.")
    else:
        strength += 1

    # Check for special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        recommendations.append("Include at least one special character (!@#$%^&*(), etc.).")
    else:
        strength += 1

    # Check for common patterns
    common_patterns = ["password", "1234", "qwerty", "abc123"]
    if any(pattern in password.lower() for pattern in common_patterns):
        recommendations.append("Avoid common patterns like 'password', '1234', etc.")

    # Output strength level
    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Very Strong"
    }

    print(f"Password Strength: {strength_levels[strength]}")
    if recommendations:
        print("\nRecommendations to improve your password:")
        for rec in recommendations:
            print(f"- {rec}")
    else:
        print("Your password is strong!")

# Input from the user
user_password = input("Enter your password: ")
password_strength_checker(user_password)
