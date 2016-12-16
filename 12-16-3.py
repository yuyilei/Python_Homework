import string 

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long'
myInput = raw_input('Identifier to test ? ')

strlen = len(myInput)
if strlen > 1 :
    if myInput[0] not in alphas :
         print ''' invalid : first must be 
         alphabetic '''
    else :
         for otherChar in myInput[1:] :
             alphnums = alphas + nums 
             if otherChar not in alphnums :
                 print  ''' invalid : remaining symbols must be 
                 alphabetic !! '''
                 break
         else :
             print 'okay as an identifier !!'
