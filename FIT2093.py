import gmpy2

def gcd(b,a):
    b,a=a,b%a
    if a==0:
        return b
    else:
        return gcd(b,a)

def read_in():
    n = []
    c = []
    with open('Joe_Public_Key_Samples.txt') as f:
        for line in f:
            if (line[0] == 'n'):
                n.append(int(line[2:]))
            if (line[0] == 'c'):
                c.append(int(line[2:]))

def get_read():
    alist = []
    blist = []
    opener = open('Joe_Public_Key_Samples.txt')
    for line in opener:
        if (line[0] == 'n'):
            alist.append(int(line[2:]))
        if (line[0] == 'c'):
            blist.append(int(line[2:]))
    return alist,blist

def get_number(alist,c):
    new_list = []
    for i in range(20):
        for j in range(i+1,20):
                com = gcd(alist[i],alist[j])
                if com != 1:
                    new_list.append((i+1,j+1,alist[i],alist[j],com,c[i],c[j]))
    return new_list

def get_d(new_list):
    e = 65537
    fi = []
    d = []
    for i in new_list:
        fi.append(((i[2] // i[4]) - 1) * (i[4] - 1))
        fi.append(((i[3] // i[4]) - 1) * (i[4] - 1))
    for i in fi:
        d.append(gmpy2.invert(e, i))
    return d

def decrypt(new_list,d):
    plain_text = []
    n = 0
    for i in range(len(new_list)):
        for m in range(2):
            plain_text.append((new_list[i][m],pow(new_list[i][m+5],d[n],new_list[i][2+m])))
            n+=1
    return plain_text

def main():
    n,c = get_read()
    new_list = get_number(n,c)
    d = get_d(new_list)
    plain_text = cryce(new_list,d)
    for i in plain_text:
        print(i)

if __name__ == '__main__':
    main()