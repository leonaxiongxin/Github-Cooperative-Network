import numpy as np

def main():
    fcon = open('ContributorsInfo.txt','rb')

    fcon.readline()
    lines = fcon.readlines()

    list_name = []
    list_star = []
    list_lang = []
    list_member = []
    list_con = []

    for line in lines:
        elements = line.split()
        #注意用二进制读取，清除空格
        list_name.append(str(elements[0].decode('UTF-8')))
        list_star.append(str(elements[1].decode('UTF-8')))
        list_lang.append(str(elements[2].decode('UTF-8')))
        list_member.append(str(elements[3].decode('UTF-8')))
        list_con.append(int(elements[4].decode('UTF-8')))

    con = np.array(list_con)
    #print(con.shape)
    member = sorted(set(list_member),key=list_member.index)
    print(len(member))
    count = np.zeros((len(member),))
    #注意shape的表示

    f1 = open('1.txt','w')
    f10 = open('10.txt','w')
    f100 = open('100.txt','w')
    f1000 = open('1000.txt','w')
    f10000 = open('10000.txt','w')

    for i in range(len(member)):
        temp = []
        temp = [x for x in range(len(list_member)) if list_member[x] == member[i]]
        for j in range(len(temp)):
            k = temp[j]
            count[i] += con[k]
            
        if count[i] <= 10:
            for j in range(len(temp)):
                f1.write(list_name[temp[j]]+'\t'+list_star[temp[j]]+'\t'+list_lang[temp[j]]+'\t'+list_member[temp[j]]+'\n')
        elif count[i] <= 100:
            for j in range(len(temp)):
                f10.write(list_name[temp[j]]+'\t'+list_star[temp[j]]+'\t'+list_lang[temp[j]]+'\t'+list_member[temp[j]]+'\n')
        elif count[i] <= 1000:
            for j in range(len(temp)):
                f100.write(list_name[temp[j]]+'\t'+list_star[temp[j]]+'\t'+list_lang[temp[j]]+'\t'+list_member[temp[j]]+'\n')
        elif count[i] <= 10000:
            for j in range(len(temp)):
                f1000.write(list_name[temp[j]]+'\t'+list_star[temp[j]]+'\t'+list_lang[temp[j]]+'\t'+list_member[temp[j]]+'\n')
        else:
            for j in range(len(temp)):
                f10000.write(list_name[temp[j]]+'\t'+list_star[temp[j]]+'\t'+list_lang[temp[j]]+'\t'+list_member[temp[j]]+'\n')

    f1.close()
    f10.close()
    f100.close()
    f1000.close()
    f10000.close()
    fcon.close()
    print("Stratify successfully!")
    

if __name__ == '__main__':
    main()




        
