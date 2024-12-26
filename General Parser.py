#Created by Dennis Ulichney, CSC-210, Section 2.
import sys
import os

#Everything involving the job file goes here:
job_name = input('Please enter the name of the job file.')
if os.path.exists(job_name):
    job_file = open(job_name,'r',encoding='UTF-8')
    file_names = job_file.readlines()
    job_file.close()
else:
    sys.exit('Please make sure that the name of the job file exactly matches a file that already exists in the same folder as the program.')
    
if len(file_names) == 4:
    input_name = file_names[0][0:len(file_names[0])-1]
    control_name = file_names[1][0:len(file_names[1])-1]
    frequency_name = file_names[2][0:len(file_names[2])-1]
    stat_name = file_names[3]
else:
    sys.exit('You must have four file names in the job file:\n1. The Input File\n2. The Control File\n3. The Frequency Table File\n4. The Statistics File')


#Everything involving the control file goes here:
if os.path.exists(control_name):
    control_file = open(control_name,'r',encoding='UTF-8')
    control_data = control_file.readlines()
    control_file.close()
else:
    sys.exit('Please make sure that the name of the control file exactly matches a file that already exists in the same folder as the program.')
    

if len(control_data) == 5:
    case_sensitive = control_data[0][0].lower()
    if case_sensitive == 'y':
        alphabet = control_data[1][0:len(control_data[1])-1]
    elif case_sensitive == 'n':
        alphabet = control_data[1][0:len(control_data[1])-1].lower() + control_data[1][0:len(control_data[1])-1].upper()
    else:
        sys.exit('The first line of the control file must consist of either a y or an n (y if case matters, n if not).')

    prefixes = control_data[2][0:len(control_data[2])-1]
    infixes = control_data[3][0:len(control_data[3])-1]
    suffixes = control_data[4][0:len(control_data[4])-1]
else:
    sys.exit('You must have five lines in the control file:\n1. Case Sensitivity (y for yes or n for no)\n2. A set of regular characters\n3. A Set of Prefix Characters\n4. A Set of Infix Characters\n5. A Set of Suffix Characters')


#Everything involving the input file goes here:
if os.path.exists(input_name):
    input_file = open(input_name,'r',encoding='UTF-8')
else:
    sys.exit('Please make sure that the name of the input file exactly matches a file that already exists in the same folder as the program.')
input_lines = input_file.readlines()
input_file.close()

word = ''
characters = []
word_list = []

for aline in range(0,len(input_lines)):
    for achar in range(0,len(input_lines[aline])):
        characters.append(input_lines[aline][achar])

        
        #Finds and adds regular characters:
        if (input_lines[aline][achar] in alphabet):
            word += input_lines[aline][achar]
            

        #Protects the following parts from index errors when a line has a length of 1:
        elif len(input_lines[aline]) == 1:
            continue

        
        #Looks for prefixes, adding a space before if the last character was a suffix:
        elif (achar < len(input_lines[aline])-1) and (len(word) > 0) and (input_lines[aline][achar] in prefixes) and (word[len(word)-1] in suffixes) and (input_lines[aline][achar+1] in alphabet):
            word_list.append(word)
            word = input_lines[aline][achar]
        
        elif (0 < achar < len(input_lines[aline])-1) and (input_lines[aline][achar] in prefixes) and (input_lines[aline][achar-1] not in alphabet) and (input_lines[aline][achar+1] in alphabet):
            word += input_lines[aline][achar]

        elif (achar == 0) and (input_lines[aline][achar] in prefixes) and (input_lines[aline][achar+1] in alphabet):
            word += input_lines[aline][achar]

            
        #Looks for infixes:
        elif (0 < achar < len(input_lines[aline])-1) and (input_lines[aline][achar] in infixes) and (input_lines[aline][achar-1] in alphabet) and (input_lines[aline][achar+1] in alphabet):
            word += input_lines[aline][achar]
            

        #Looks for suffixes:
        elif (0 < achar < len(input_lines[aline])-1) and (input_lines[aline][achar] in suffixes) and (input_lines[aline][achar-1] in alphabet) and (input_lines[aline][achar+1] not in alphabet):
            word += input_lines[aline][achar]

        elif (achar == len(input_lines[aline])-1) and (input_lines[aline][achar] in suffixes) and (input_lines[aline][achar-1] in alphabet):
            word += input_lines[aline][achar]

        #Assembles a list off all words:
        elif (len(word) > 0):
            word_list.append(word)
            word = ''

#Word:Frequency dictionary is created here:
word_count = dict.fromkeys(word_list)

word_total = 0
for word in word_list:
    word_count[word] = word_list.count(word)
    word_total += len(word)


#Write frequency table into a chosen file:
frequency_file = open(frequency_name,'w',encoding='UTF-8')

unique_total = 0
for key in word_count:
    frequency_file.write('{:<10}{}'.format(word_count[key],key)+'\n')
    unique_total += len(key)

frequency_file.close()


#Write stats table into a chosen file:
stat_file = open(stat_name,'w',encoding='UTF-8')


#Print the token count:
stat_file.write('{:>47}{:<}'.format('Number of tokens: ',len(word_list))+'\n')


#Print the unique token count:
stat_file.write('{:>47}{:<}'.format('Number of unique tokens: ',len(word_count))+'\n')


#Calculate and print the average length of the unique tokens:
if (len(word_count) > 0):
    stat_file.write('{:>47}{:<}'.format('Average length of unique tokens: ','{:.2f}'.format(unique_total/len(word_count)))+'\n')
else:
    stat_file.write('{:>47}{:<}'.format('Average length of unique tokens: ','There are no tokens to calculate an average with!\n'))
    

#Calculate and print the average token length:
if (len(word_list) > 0):
    stat_file.write('{:>47}{:<}'.format('Average token length: ','{:.2f}'.format(word_total/len(word_list)))+'\n')
else:
    stat_file.write('{:>47}{:<}'.format('Average token length: ','There are no tokens to calculate an average with!\n'))
    

#Character dictionary is created here to count unique characters:
char_dict = dict.fromkeys(characters)


#The total uses of each unique character are totalled here:
char_total = 0
for achar in char_dict:
    char_total += characters.count(achar)


#Calculate and write the number of characters:
stat_file.write('{:>47}{:<}'.format('Number of characters: ',len(characters))+'\n')


#Calculate and write the number of unique characters:
stat_file.write('{:>47}{:<}'.format('Number of unique characters: ',len(char_dict))+'\n')


#Calculate and write the average number of times that each unique character was used:
if (len(char_dict) > 0):
    stat_file.write('{:>47}{:<}'.format('Average number of uses for a unique character: ','{:.2f}'.format(char_total/len(char_dict))))
else:
    stat_file.write('{:>47}{:<}'.format('Average number of uses for a unique character: ','There are no characters to calculate an average with!'))
    
stat_file.close()

print('Done!')

