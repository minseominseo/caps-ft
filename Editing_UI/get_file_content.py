import re

lines_t=[]
L=[]

def read_result_string():
    f=open('./recover_list.tmp','r')
    lines = f.readlines()


    for i in lines:
        lines_t.append(i[:-1])

    f.close()

    str_line =""
    for i in lines:
        str_line+=i

    return str_line

def read_result_num():
    
    for i in range(len(lines_t)):
        L.append(lines_t[i].split('-'))
    

    num_recover= sum(int(j) for i, j in L)
    
    number_re = str(num_recover)
    print(number_re)
    return  number_re

