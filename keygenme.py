import random
import string


j = int(input("How many keys you want to generate?\n\n> "))




for i in range(j):


    final_key = ""

    key_len = random.randint(1,63)

    key = ''.join(random.choices(string.digits + string.ascii_letters, k=2))

    for x in range(key_len):
        final_key += key
        final_key += key[::-1]



    print(final_key) 
