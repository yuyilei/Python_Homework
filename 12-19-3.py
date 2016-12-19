

num_str = raw_input('Enter a number: ')

num_num = int(num_str) 

fac_list = range(1,num_num+1)
res_list = range(1,num_num+1)

print 'BEFORE::',fac_list 

for each in fac_list :
    if num_num % each == 0 :
        res_list.remove(each) 


print 'AFTER :' ,res_list
