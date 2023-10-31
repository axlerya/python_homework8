number_string = int(input('Input the line number to copy'))

with open("file.txt", 'r') as f1, open("new_file.txt", 'a+') as f2:
    strings = f1.readlines()
    count_string = len(strings)
    if (count_string+1 < number_string) or number_string == 0:
        print('Error: Input the correct line number in file')
    else:
        if number_string == 1:
            f2.write(strings[0][:-2] + '\n')
        else:
            f2.write(strings[number_string-1][:-2] + '\n')
        print('Line copied successfully')
