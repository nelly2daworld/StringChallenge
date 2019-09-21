input_string = input()
count = 0

new_word = ""
i = 1
for i in range(len(input_string) ):
    first_letter = input_string[i - 1] 
    second_letter = input_string[i]
    if(first_letter == second_letter):
        new_word += first_letter
        count += 1
        i += 1
    else:
        if(i != 0):
            new_word += str(count)
        count = 1
        new_word += second_letter
        i += 1
if range(len(input_string)):
    new_word += str(count)
print(new_word)
