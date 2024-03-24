num_times = int(input("How many numbers will you add -> "))
total = 0.0

for i in range(num_times):
    user_input = input("Enter a number -> ")
    if user_input == '':
        user_input = '0'
    total += float(user_input)

print(f"Your total is -> {total}")
