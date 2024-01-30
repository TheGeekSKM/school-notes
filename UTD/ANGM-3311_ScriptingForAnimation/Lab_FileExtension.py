user_input = input("Enter a file name -> ")
print(f"The extension -> {user_input[(user_input.find('.') + 1):]}")
