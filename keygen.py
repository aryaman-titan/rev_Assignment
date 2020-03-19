from pwn import *

# Declare a list containing all alphabets and '@' key

alpha = 'a'
alphabets = []

for i in range(0,26):
    alphabets.append(alpha)
    alpha = chr(ord(alpha) + 1)

alphabets.append('@')

# Generating the key

key = random.choice(alphabets)
key += chr(0x40) # chr(0x40) = '@'
key += random.choice(alphabets)
key += random.choice(alphabets)
key += chr(300 - (ord(key[2])+ord(key[3])))

io = process(['glowwine',key])
print("Using key : ", key)
output = io.recvline()
print(output)
print("Congrats..binary cracked!! :-)")