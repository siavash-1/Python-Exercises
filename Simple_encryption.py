import random
#change uncrypt to decrypt
message1=("baba")


def key_gen():
    key= {
        "a": str(random.randint(1,9)),
        "b": str(random.randint(1,9))
        }
        #if- check if the key for a and be are the same in that case repeat process
    return key

def encryption(key,message):
    encrypted1=[]
    for x in message:
        encrypted1.append(key[x])
    encrypted2= "".join(encrypted1)
    return encrypted2

def key_join(key):
    joined_key=''.join('{}{}'.format(key, value) for key, value in key.items())
    return joined_key

def key_unjoin(joined_key):
    unjoined_key={}
    keys1=[]
    keys2=[]

    for x in joined_key[ : :2]:
        keys1.append(x)

    for x in joined_key[1 : :2]:
        keys2.append(x)

    return dict(zip(keys2,keys1))   #byt till tvärtom

def uncrypt(encrypted,key):
    uncrypted=[]
    for x in encrypted:
        uncrypted.append(key[x])
    return "".join(uncrypted)

def test1():     #remove function
    a=key_gen()
    print(a)

    b=encryption(a,message1)
    print(b)

    c=key_join(a)
    print(c)

    d=key_unjoin(c)
    print(d)

    e=uncrypt(b,d)
    print(e)


def encrypt_file(file):
    f = open(file,"r")
    message2=f.read()
    encryption_key=key_gen()
    encryption2=encryption(encryption_key,message2)
    f = open(file,"w")
    f.write(encryption2)
    f.close()
    return key_join(encryption_key)


def uncrypt_file(file,key):
    f=open(file,"r")
    message=f.read()
    uncrypted_message=uncrypt(message,key)
    return uncrypted_message





#print(encrypt_file(file1))

#key5="a3b7"
#print(uncrypt_file(file1,key_unjoin(key5)))


# write in a function
input1=input("e=encrypt, d=decrypt")
if input1 == "e":
    file_name=input("file to encrypt")
    print("file is being encrypted,  your key is:")
    print(encrypt_file(file_name))

elif input1 == "d":
    key=input("key")
    file_name=input("file to decrypt")
    key= key_unjoin(key)
    print(uncrypt_file(file_name,key))
