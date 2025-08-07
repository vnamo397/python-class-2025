name =input("Enter your name: ")
surname =input("Enter your surname: ")
age = int(input("Enter your age: "))
print(f"Hello, my name is {name} {surname}. I am Gender of {age} years old.")

str ="perfect#perfected#perfect#perfection"
print(str.split("#")) 

dna = "CACGCCTAGTTTCAGACATAACCCTGGACATAGCCATAACGGAGTCAG"

print(len(dna))  # Using the len function to get the length of the DNA string
print(dna.find('TGGA'))
print(dna.find('TCAG',dna.find('TGGA') + 1,len(dna)))
print(dna.find('GACG'))

print('GACG'in dna)  # Check if 'GACG' is in the DNA string
if 'GACG' in dna:
    print("We found  in the DNA .")
else:
    print("We not found in the DNA .")

    # Slice the dna string into substrings of 3 characters and print them all in one line
triplets = [dna[i:i+3] for i in range(0, len(dna), 3)]
print(' '.join(triplets))