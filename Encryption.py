"""
Encrypt Decrypt


Encrypt is a function that takes a string, -message-, as an attribute and will return None.
Encrypt will:
    Ask the user to enter a file name. This file should contain pairs of characters and numbers.
    Match the characters from -message- to the numbers given in the file.
    Save the numbers to a text file.

Decrypt is a function that takes no arguments and will return a string.
    Ask the user for two inputs, the name of a file containing the cipher and the name
    of a file containing an encrypted message.
    Match the characters given by the cipher file to the numbers given in the message file.
    return the decyphered string.

Note:
A cypher.txt file is provided.
you can use the following string to test your code.
m = "The Kalevala is a 19th-century compilation of poetry written by Elias Lönnrot it contains Finnish oral folklore and mythology"
"""
# Function to Encrypt the code according to given Cypher file, the Function will read cypher file and replace the
# single number(containing 1 digit) by adding '0' on left side with digit, number with double digit will remain same
# and for characters not in cypher file, it adds '*' on right side with that character , so its easy to Decrypt
def Encrypt(str_msg):
    while True:                                                         # loop for correct file name and Extension
        File_name = input("Enter a Name of file containing Cypher code : ")
        if File_name.endswith(('.txt')):
            break
        print("Error!! Enter file Name with correct Extention: ")
    handler = open(File_name, 'r')                                      # Reads a file that is needed to Encryp
    Final_string = ""                                                   # Empty Final String
    Final_dict = {}
    for line in handler:                                                # loop for reading lines in file(file that is needed to Encrypt)
        if len(line[2:].rstrip("\n")) < 2:                              # if the number in cypher file is 1 digit then it adds string('0') in front of that digit
            num = "0" + line[2:].rstrip("\n")
        else:                                                           # if number is 2 digit then it will add to number
            num = line[2:].rstrip("\n")
        Final_dict[line[0]] = num
    for char in str_msg:                                                # loop for each characters in the string argument
        Status = 0
        for key, value in Final_dict.items():                           # loop for keys and values of dictionary made of cypher code
            if char == key:                                             # condition (if character matches the key (i.e letter in dictionary of cypher file)
                Final_string += value                                   # it add the value of dictionary (which is with key of dictionary) instead of character
                Status = 1
                break
        if char == " ":                                                 # condition for space in string message to encrypt
            Final_string += "  "                                        # it adds 2 spaces which helps id Decrypting code(even numbers)
            Status = 1
        if Status == 0:                                                 # condition for characters which are not included in cypher file
            #Final_string += char + "0"
            Final_string += char + "*"                                  # it adds * after a character which helps in Decrypting (makes even length(i.e. 2))
    handler.close()
    Encrypted_code = open('Encrypted_data.txt', 'w')                    # Makes new file for  the Encrypted data
    Encrypted_code.write(Final_string)                                  # Writes a Encrypted code in File
    Encrypted_code.close()
    print("\nA New File Named Encrypted_data.txt containing Encrypted code is created in your Device\n")
m = "The Kalevala is a 19th-century compilation of poetry written by Elias Lönnrot it contains Finnish oral folklore and mythology"
Encrypt(m)

# Function to Decrypt the Encrypted code
def Decrypt():
    while True:                                                             #loop for correct file name and Extension
        Cypher_file_name = input("Enter a Cypher File Name: ")
        if Cypher_file_name.endswith(('.txt')):
            break
        print("Error!! Enter file name with correct Extention: ")
    cypher_handler = open(Cypher_file_name, 'r')                            # reads file with cypher code

    while True:                                                             # loop for correct file name and Extension
        Encrypt_file_name = input("Enter a Name of File Containing Encrypted Message:  ")
        if Encrypt_file_name.endswith(('.txt')):
            break
        print("Error!! Enter file name with correct Extention: ")
    Encrypted_handler = open(Encrypt_file_name, 'r')                         # reads file that is needed to Decrypt
    string_list=[]
    n = 0
    for digits in Encrypted_handler:                                         # loop for digits in Encrypted
        for n in range(0, len(digits), 2):
            string_list.append(digits[n:n+2])
    Final_string = ""                                                        # Empty final string for Decrypted code
    Final_dict = {}
    for line in cypher_handler:                                              # loop for reading lines in Cypher file
        if len(line[2:].rstrip("\n")) < 2:                                     # if number has 1 digit, it adds string '0' before number easy Decryption and as done in encryption
            num = "0" + line[2:].rstrip("\n")
        else:                                                                # for 2 digits in number, it adds that number in number
            num = line[2:].rstrip("\n")
        Final_dict[line[0]] = num
    cypher_handler.close()
    for item in string_list:                                                 # loop for every items in the list( contains characters of the string argument)
        status = 0
        for key, value in Final_dict.items():                                # loop for key and values in Dinctionary ( made of cypher code)
            if item == value:                                                # condition for item(number(digits) of argument passed) and value in dictionary of cypher code
                Final_string += key                                          # it replaces with character again
                status = 1
                break
        if item == "  ":                                                     # if it contains 2 blank space, it makes 1
            Final_string += " "
            status = 1
        if status == 0:                                                      # condition that removes '*' character
            Final_string += item.rstrip("*")
            #Final_string += item.lstrip("0")
    print("The Decrypted (Readable)/ Decyphered code is :\n")
    return Final_string                                                      # prints the Decrypted code (Readable)
print(Decrypt())

"""
Hider

Hider is a function that takes a string, -sentence- and a list of letters, -hide- as arguments.
Hider will modify the words of -sentence- by changing the letters of the words by *
if they appear in -hide-. If a word has 2 or more letters that appear in -hide-,
the whole word should be replaced with *.

Hider should work for both the upper and lowercase letters.

example = "The brown fox jumps over the lazy dog."
letterList = ["b", "d","j", "m"]
Hider(example, letterList)
#ouptput: The *rown fox ***** over the lazy *og.

"""
# Function for hiding a letter that contains particular characters in list and word that has 2 or more characters in word
def Hider(str, letter_list):
    str = str.lower()                                               # converts string into lower case
    final = ""
    for character in str:                                           # loop for reading character in string and making new list
        if character in letter_list :
            final += '*'
        else:
            final += character
    final = final.split()                                           # splits word and makes list
    i = 0
    for word in final:                                              # loop for reading each word in list
        i += 1
        count = 0
        for letter in word:                                         # loop for counting number of letters contained in letter list(letters that are replaced)
            if letter == '*':
                count += 1
        if count >= 2:                                              # if word contains 2 or more letters from list, it replaces whole word with '*'
            final[i-1] = '*'*len(word)
    print("\nThe Hidden Sentence :\n")
    return " ".join(final)
example = "The brown fox Jumps over the lazy dog."
letterList = ["b", "d", "j", "m"]
print(Hider(example, letterList))