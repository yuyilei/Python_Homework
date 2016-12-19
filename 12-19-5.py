def findchr(string,char) :
    liststr = [ i for i in string ]
    index = []
    for each in string :
        if each == char :
            index.append(liststr.index(char)) 
    if len(index) == 0 :
        return -1 
    else :
        return index


def rfindchr(string,char) :
    liststr = [i for i in string] 
    liststr_reverse = liststr[::-1]
    index = -1 
    for each in liststr_reverse :
        if each == char :
            index = liststr.index(each)
            break 

    return index 


def subchr(string,origchar,newchar) :
    liststr = [ i for i in string ] 
    for each in liststr :
        if each == origchar :
            index = liststr.index(each)
            liststr.remove(origchar)
            liststr.insert(index,newchar) 
    res = ''.join(liststr)
    return res 

if __name__ == '__main__' :
    string = raw_input('Enter a string')
    char = raw_input('Enter a char') 
    origchar = raw_input('Enter an origchar')
    newchar = raw_input('Enter a newchar')
    print  findchr(string,char) 
    print rfindchr(string,char)
    print subchr(string,origchar,newchar)

    
