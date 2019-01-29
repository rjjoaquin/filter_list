l = ['a', 'b', 'c', 1, 2, 3, '1','2','3',0]

def filter_list(l):
    list = []
    for i in l:
        try:
            if i >= 0:
                list.append(i)
        except:
            pass
    return list

print (filter_list(l))
