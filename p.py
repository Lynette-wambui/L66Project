# Asking for input from a user
num = int(input("🤔 Enter a number to check if it is a power of 8: "))

# Checking if the number is a power of 8
is_power = False
for i in range(100):
    if 8 ** i == num:
        print(f" 🎉 🤗 Yes! The number is a power of 8: 8^{i} = {num}")
        is_power = True
        break

if not is_power:
    print("😔 😔Oops! The number is not a power of 8.")







import random

print("📖 Let's Learn If Numbers are Powers of 8!")
print("Here are the powers of 8 from 0 to 20:\n")

# Step 1: Show powers of 8
powers_of_8 = []
for i in range(21):
    value = 8 ** i
    powers_of_8.append(value)
    print(f"8^{i} = {value}")

# Step 2: Random Quiz
print("\n🧠 Time for a Quick Quiz!")
print("I'll show you a number. You tell me if it's a power of 8 by answering (yes/no).\n")

# Generate 4 random numbers
for _ in range(4):
    num = random.randint(1, 100000)
    user_input = input(f"Is {num} a power of 8? (yes/no): ").strip().lower()

    if (num in powers_of_8 and user_input == "yes") or (num not in powers_of_8 and user_input == "no"):
        print("✅ Correct!")
    else:
        print(f"❌ Oops! {'It is' if num in powers_of_8 else 'It is not'} a power of 8.")

print("\n🎈🎊 Great job! Keep practising powers of 8!")











import random

print("📖Let's Learn Powers of 2!")
print("Here are the powers of 2 from 0 to 20:\n")

# Step 1: Show powers of 2
for i in range(20):
    print(f"2^{i} = {2 ** i}")

# Step 2: Random Quiz
print("\n Time for a Quick Quiz.")

# Generate 3 random questions 
for _ in range(4):
    exp = random.randint(0, 10)
    answer = int(input(f"What is 2 to the power of {exp}?"))

    if answer == 2 ** exp:
        print(f"☺️ ☺️ Correct! 2^{exp} = {2 ** exp}")
    else:
        print(f"😔😢😞Oops! The correct answer is {2 ** exp}")

print("\n 🎈🎊🎊Great job! Keep practising powers of 2!")





import random

print("📖Let's Learn Powers of 4!")
print("Here are the powers of 4 from 0 to 25:\n")

# Step 1: Show powers of 4
for i in range(26):
    print(f"4^{i} = {4 ** i}")

# Step 2: Random Quiz
print("\n Time for a Quick Quiz.")

# Generate 3 random questions 
for _ in range(4):
    exp = random.randint(0, 10)
    answer = int(input(f"What is 4 to the power of {exp}?"))

    if answer == 4 ** exp:
        print(f"☺️ ☺️ Correct! 4^{exp} = {4 ** exp}")
    else:
        print(f"😔 😢 😞Oops! The correct answer is {4 ** exp}")

print("\n 🎈🎊🎊Great job! Keep practising powers of 4!")





base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Calculate the exponent
result = base ** exponent

# Display the result
print(f"{base} raised to the power of {exponent} is {result}")


base = int(input("Enter the base number: "))
power = int(input("Enter the power: "))

# Calculate the power
result = base ** power 

# Display the result
print(f"{base} raised to the power of {power} is {result}")



