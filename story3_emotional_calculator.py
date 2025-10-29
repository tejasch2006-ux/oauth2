# story3_emotional_calculator.py
mood = input("How are you feeling today? (happy/sad/angry): ")

if mood == "happy":
    print("😊 Let’s do some math magic!")
elif mood == "sad":
    print("💙 Don’t worry, math will cheer you up!")
else:
    print("🔥 Let’s channel that energy into solving problems!")

a, b = map(int, input("Enter two numbers: ").split())
print("Sum =", a + b)
