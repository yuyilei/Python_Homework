import string
alphas = string.letters + '-'
nums = string.digits

import keyword
keywords = keyword.kelist

print ' Welcome to the Idenifier Checker v1.0'
print ' Testees must be at least 2 chars long '

myInput = raw_input('Identifier to test ?')

if len(myInput) ==1 :
    if myInput not in alphas :
        print ''' invalid :first symbol must be 
        alphabetic '''
    else :
        print 'okay as an identifier'

else :
    if myInput in keywords :
        print ''' invaild : the input can not be 
        keyword'''
    else :
        if myInput[0] not in alphas :
            print ''' invaild : first symbol must be 
            alphabetic '''

        else : 
            for otherchar in myInput[1:] :
                if otherchar not in nums :
                    print ''' invaild : remaining symbols must be 
                    alphabetic '''
                    break 

        


