queue = []

def enQ() :
    queue.append(raw_input('Enter New string : '),strip())

def deQ() :
    if len(queue) == 0 :
        print 'Cannot pop from an empty queue !'
    else :
        print 'Remove [',`queueu.pop(0)`,']'

def viewQ() :
    print queue 

CDMs = { 'e' : enQ ,'d' : deQ ,'v' :viewQ } 

def showmenu() :
        pr = """
    (E)nqueue
    (D)equeue
    (V)iew
    (Q)uit

    Enter choice : """

    while True:
        while True:
            try :
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError , KeyboardInterrupt,IndexError) :
                choice = 'q'


            print '\n You picked : [%s]' % choice
            if choice not in 'devq' :
                print 'Invaild option ,try again!'
            else :
                break

        if choice == 'q' :
            break 
        CDMs[choice]()

if __name__ == '__main__' :
    showmenu()
        
        
    
