#构建用户--项目的二模矩阵
import numpy as np

def main():
    fcon = open('ContributorsInfo.txt','rb')
    fmatrix = open("matrixFull.txt",'wb')
    flist = open("list.txt",'rb')
    fpro = open("project.txt",'a')

    fcon.readline()
    lines1 = fcon.readlines()
    lines2 = flist.readlines()

    list_name = []
    list_star = []
    list_lang = []
    list_member = []
    member = []

    for line in lines1:
        elements = line.split()
        #注意用二进制读取，清除空格
        list_name.append(str(elements[0].decode('UTF-8')))
        list_star.append(str(elements[1].decode('UTF-8')))
        list_lang.append(str(elements[2].decode('UTF-8')))
        list_member.append(str(elements[3].decode('UTF-8')))

    for line in lines2:
        elements = line.split()
        member.append(str(elements[0].decode('utf-8')))

    name = sorted(set(list_name),key=list_name.index)
    for i in range(len(name)):
        temp = []
        temp = [x for x in range(len(list_name)) if list_name[x] == name[i]]
        fpro.write(name[i]+"\t"+list_star[temp[0]]+"\n")

    width = len(name)
    height = len(member)
    print(width,height)
    matrix = np.zeros((height,width))

    for i in range(len(member)):
        temp = []
        #找出每个成员在哪几个项目中出现了，
        temp = [x for x in range(len(list_member)) if list_member[x] == member[i]]
        for j in range(len(temp)):
            index = name.index(list_name[temp[j]])
            matrix[i,index] = 1
                

    np.savetxt(fmatrix, matrix, fmt='%d',delimiter='\t')

    fmatrix.close()
    fcon.close()
    flist.close()
    fpro.close()
    print("The two mode matrix is created!")

if __name__ == '__main__':
    main()
