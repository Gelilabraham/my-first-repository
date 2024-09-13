def encrypt():
    msg=input("mesage: ")
    key=input("key: ")
    encrypt_hex = ""
    key_itr=0
    for i in range(len(msg)):
        deciTEXT=ord(msg[i]) ^ ord(key[key_itr])
        key_itr+=1
        if key_itr >= len(key):
            key_it=0

        encrypt_hex += hex(deciTEXT)[2:]


    print(f"messgage encrypted successfully!\n messgage: {encrypt_hex}")

