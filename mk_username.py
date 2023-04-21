from os.path import exists

def usermake(prompt):
    count = 10
    list = []
    for i in range(90):
        list.append(prompt + str(count))
        count += 1
    return list


def main():
    perfix = input('Enter optimal perfix: ')
    usernames = usermake(perfix)
    #if not exists('clients_username.txt'):
     #   with open('clients_username.txt', 'w') as ff:
      #      ff.close()
    with open('users.txt', 'w') as f:
        for i in usernames:
            f.write(i + '\n')
    

#if main == '__main__':
main()
