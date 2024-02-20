max_cols = 5

final_string = ""
num_of_elements = 1
increasing = True
num_of_repetitions = 1
    
while num_of_elements > 0:
    line_string = ""
        
    for i in range(num_of_elements):
        line_string += "🐟"
        
    if num_of_repetitions > max_cols:
        increasing = False    
    num_of_repetitions += 1
        
    if increasing:
        num_of_elements += 1
    else:
        num_of_elements -= 1
            
    final_string += line_string + "\n"
        
print(final_string)