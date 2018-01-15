#构建完整的一模矩阵
import numpy as np

def main():
    fcon = open('ContributorsInfo.txt','rb')
    fmatrix = open("matrixFull.txt",'wb')
    #a模式不能覆盖原文件,a+可以覆盖，a模式用于字符串的写入
    flist = open("list.txt",'rb')

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

    member1 = sorted(set(list_member),key=list_member.index)

    for line in lines2:
        elements = line.split()
        member.append(str(elements[0].decode('utf-8')))

    size = len(member)
    matrix = np.eye(size)

    for i in range(size):
        temp = []
        #找出每个成员在哪几个项目中出现了
        temp = [x for x in range(len(list_member)) if list_member[x] == member[i]]
        for j in range(len(temp)):
            #找出这几个项目有哪些成员
            project = [x for x in range(len(list_name)) if list_name[x] == list_name[temp[j]]]
            for k in range(len(project)):
                index = member.index(list_member[project[k]])
                if index != i:
                    matrix[i,index] += 1
                else:
                    pass

    np.savetxt(fmatrix, matrix, fmt='%d',delimiter='\t')
    
    fmatrix.close()
    fcon.close()
    flist.close()
    print("The full matrix is created!")

if __name__ == '__main__':
    main()

