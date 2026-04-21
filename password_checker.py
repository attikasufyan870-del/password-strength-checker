# Password Strength Checker
# Cybersecurity Project by Attika Sufyan

def check_password(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters chahiye")
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("❌ Ek capital letter daalo")
    
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("❌ Ek small letter daalo")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("❌ Ek number daalo")
    
    symbols = "!@#$%^&*"
    if any(c in symbols for c in password):
        score += 1
    else:
        feedback.append("❌ Ek symbol daalo (!@#$%)")
    
    if score <= 2:
        strength = "🔴 WEAK"
    elif score <= 4:
        strength = "🟡 MEDIUM"
    else:
        strength = "🟢 STRONG"
    
    print(f"\nPassword Strength: {strength}")
    print(f"Score: {score}/5")
    
    if feedback:
        print("\nImprove karo:")
        for tip in feedback:
            print(tip)

password = input("Password enter karo: ")
check_password(password)
