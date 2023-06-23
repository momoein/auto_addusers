def write_in_file(listuser):
    with open('expiry_users.txt', 'w')as file: 
        for i in listuser:   
            file.write(i)

if __name__ == '__main__':
    pre = input("enter prefixe: ")
    pas = input("enter the new password: ")
    temp = []
    while True:
        try:
            suffix = int(input('Who should we block? '))
            temp.append(str(suffix))
            keep = input('to continue just press "Enter" ')
            if keep == "":
                pass
            else: 
                break
        except ValueError:
            print('Error: gusaale adad vaared kon!!')
    suffixes = []
    [suffixes.append(x) for x in temp if x not in suffixes]
    # print(suffixes)
    banuser = []
    for i in range(len(suffixes)):
        temp = pre + suffixes[i] + ':' + pas + '\n'
        banuser.append(temp)
    # print(banuser)
    write_in_file(banuser)
