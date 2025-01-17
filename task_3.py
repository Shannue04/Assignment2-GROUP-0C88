# -*- coding: utf-8 -*-
"""TASK 3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16HW4cUJjihOsdqTJ7Mr81UZ00KdMET8k
"""

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                elif shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Given encrypted code (assuming it's given as 'encrypted_text')
encrypted_text = "tybony_inenvoyr = 100\nzl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}\n\nqrs cebprff_ahzoref():\n    tybony tybony_inenvoyr\n    ybpny_inenvoyr = 5\n    ahzoref = [1, 2, 3, 4, 5]\n\n    juvyr ybpny_inenvoyr > 0:\n        vs ybpny_inenvoyr % 2 == 0:\n            ahzoref.erzbir(ybpny_inenvoyr)\n        ybpny_inenvoyr -= 1\n\n    erghea ahzoref\n\nzl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}\nerfhyg = cebprff_ahzoref(ahzoref=zl_frg)\n\nqrs zbqvsl_qvpg():\n    ybpny_inenvoyr = 10\n    zl_qvpg['xrl4'] = ybpny_inenvoyr\n\nzbqvsl_qvpg(5)\n\nqrs hcgngr_tybony():\n    tybony tybony_inenvoyr\n    tybony_inenvoyr += 10\n\nsbe v va enatr(5):\n    cevag(v)\n    v += 1\n\nvs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:\n    cevag('Pbapgvba zrg!')\n\nvs 5 abg va zl_qvpg:\n    cevag('5 abg sbhaq va gur qvpgvbanerl!')\n\ncevag(tybony_inenvoyr)\ncevag(zl_qvpg)\ncevag(zl_frg)"

# Trying a possible key value to decrypt (example: key = 13, a common Caesar cipher shift)
key = 13
decrypted_code = decrypt(encrypted_text, key)

# Display the decrypted code to identify errors and fixes
print(decrypted_code)

global_varaible = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_varaible
    local_varaible = 5
    numbers = [1, 2, 3, 4, 5]

    while local_varaible > 0:
        if local_varaible % 2 == 0:
            numbers.remove(local_varaible)
        local_varaible -= 1

    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers(numbers=my_set)

def modify_dict():
    local_varaible = 10
    my_dict['key4'] = local_varaible

modify_dict(5)

def uptate_global():
    global global_varaible
    global_varaible += 10

for i in range(5):
    print(i)
    i += 1

if my_set is not None and my_dict['key4'] == 10:
    print('Conction met!')

if 5 not in my_dict:
    print('5 not found in the dictionarey!')

print(global_varaible)
print(my_dict)
print(my_set)

# Corrected code with explanations

# Corrected global variable name spelling
global_variable = 100

# Corrected dictionary key names
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Corrected function for processing numbers
def process_numbers():
    global global_variable  # Corrected spelling
    local_variable = 5  # Corrected spelling
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:  # Fixed indentation error
        if local_variable % 2 == 0:
            numbers.remove(local_variable)  # Correct method call
        local_variable -= 1

    return numbers

# Sets cannot have duplicate values; removed redundant values
my_set = {1, 2, 3, 4, 5}
result = process_numbers()  # Corrected the call without passing arguments

# Corrected function to modify the dictionary
def modify_dict():
    local_variable = 10  # Corrected spelling
    my_dict['key4'] = local_variable  # Corrected the dictionary update

modify_dict()  # Corrected the call without passing arguments

# Corrected function name to update the global variable
def update_global():
    global global_variable  # Corrected spelling
    global_variable += 10

update_global()  # Added a call to update the global variable

# Corrected the for-loop logic
for i in range(5):
    print(i)

# Fixed logical condition and string typo in the if statement
if my_set is not None and my_dict['key4'] == 10:
    print('Condition met!')

# Corrected the logic and string typo in the second if statement
if 5 not in my_dict:
    print('5 not found in the dictionary!')

# Corrected print statements to show output
print(global_variable)
print(my_dict)
print(my_set)