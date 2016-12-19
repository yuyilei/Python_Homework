
def change_to_minute_and_hour(n) :
    hour = n / 60 
    minute = n - hour * 60
    return hour , minute 

if __name__ == '__ main__' :
    n = raw_input('Enter a number of minute :')
    s = int(n)
    res = change_to_minute_and_hour(s)
    print res 
