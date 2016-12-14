'read a file '

# get a filename 

fname = raw_input("Enter a filename")
print 

# attempt to open file for reading 

try :
    fobj = open(fname,'r')
except IOError , e :
    print "**** file open error:" ,e
else :
    # display contents to the screen 
    for eachLine in fobj:
        print eachLine,
fobj.close()
