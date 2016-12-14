'make a text python creat text file'

import os 
ls = os.linesep


# get filename

while True :
     
    if os.path.exits(fname) :
        print "ERROR : '%s' already exits"  % fname
    else:
        break 

# get file content (text) lines

add = []
print "\nEnter lines ('.'by itself to quit).\n"

#loop until user terminates input
while True :
    entry = raw_input('> ')
    if entry == '.' :
        break
    else :
        all.append(entry)

# write lines to file 

fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all ])
fobj.close()

print 'DONE'


