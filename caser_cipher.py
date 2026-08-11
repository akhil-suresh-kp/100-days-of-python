alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(alphabet,msg,shift_amount):
    msg = msg.replace(' ','')
    enc_msg = ''
    for x in msg:
        num = alphabet.index(x) + shift_amount
        num %= len(alphabet)
        enc_msg += alphabet[num]
    return enc_msg


def decrypt(alphabet,msg,shift_amount):
    msg = msg.replace(' ','')
    dec_msg = ''
    for x in msg:
        num = alphabet.index(x) - shift_amount
        num %= len(alphabet)
        dec_msg += alphabet[num]
    return dec_msg

def main():
    switch = True
    while switch:
        msg = input("Enter the message: ").lower()
        choice = input("Encrypt/Decrypt (E/D): ").lower()
        if choice == 'e':
            shift_amount = int(input("Enter the shift amount: "))
            res = encrypt(alphabet,msg,shift_amount)
            print(f'Encrypted Message: {res}')
        elif choice == 'd':
            shift_amount = int(input("Enter the shift amount: "))
            res = decrypt(alphabet,msg,shift_amount)
            print(f'Decrypted Message: {res}')
        else:
            print("Invalid Option")
        x = input("Do you want to restart? (Y/n): ")
        if x == 'y':
            continue
        else:
            switch = False

main()