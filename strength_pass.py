import re

def password_strength(password):
    
    length_score = min(1, len(password) / 8)  

    
    uppercase_score = 1 if re.search(r"[A-Z]", password) else 0

    
    lowercase_score = 1 if re.search(r"[a-z]", password) else 0

    
    number_score = 1 if re.search(r"\d", password) else 0

    
    special_char_score = 1 if re.search(r"[!@#$%^&*()-_+=]", password) else 0

   
    total_score = length_score + uppercase_score + lowercase_score + number_score + special_char_score

    
    if total_score < 2:
        strength = "Weak"
    elif total_score < 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength

# Example usage
password = input("Enter your password: ")
strength = password_strength(password)
print("Password strength:", strength)
