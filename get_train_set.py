global train_set

def get_train_set (a):

    train_set = []
    
    if a % 2 == 0:
        train_set.append ('Pull ups')
        train_set.append ('Pull_ups.gif')
        
    else:
        train_set.append ('Chin ups')
        train_set.append ('Chin_ups.gif')

    train_set.append ('Abs')
    train_set.append ('Abs.gif')

    if a % 3 == 0:
        train_set.append ('Legs')
        train_set.append ('Legs.gif')
        
    elif  (a-2)%3 == 0:
        train_set.append ('Push ups')
        train_set.append ('Push_ups.gif')
        
    else:
        train_set.append ('Wide pull')
        train_set.append ('Wide_pull_ups.gif')
        

    return (train_set)
        
