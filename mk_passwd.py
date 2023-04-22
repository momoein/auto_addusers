from os.path import exists

def get_users():
    if exists('users.txt'):
        #print('hast')
        with open('users.txt', 'r') as f:
            luser = f.readlines()
        new_luser = []    
        for i in luser:
            new_luser.append(i[0:-1])
        #print(new_luser)
        return new_luser
    else: 
        print('Error: users.txt not exist')

def add_pass():
    latin = ('_', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix')
    alpha = ('_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r')
    binery = ('0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001')
    passwords = []
    for i in range(10,100):
        i10 = i // 10
        i1 = i % 10
        isum = i10 + i1
        passwords.append(latin[i10] + alpha[isum] + binery[i1])
    #print(passwords)
    return passwords

def main():
    users = get_users()
    #print(users)
    passwd = add_pass()
    with open('passwords.txt', 'w')as f:
        for i in range(len(users)):
            f.write(users[i] + ':' + passwd[i] + '\n')
    print('The program was successfully executed')

if __name__ == '__main__':
    main()
