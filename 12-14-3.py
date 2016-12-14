
def displayNumType(num):
    print num "is"
    if isintance(num,(int,long,float,complex)):
        print ' s number of type :' ,type(num)._name_
    else :
        print 'not a  number at all! '


from types import IntType

def displayNumTypez(num):
    if type(num) == IntType :
        print num 'is an integer'
