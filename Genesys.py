def nth_most_rate_signature(list,n):
    res = ''
    count = []
    for element in list:
        count.append(list.count(element))
    for i in count:
        if count.count(i) > 1:
            count.remove(i)
    count.sort()
    for i in list:
        if list.count(i) == count[(n-1)]:
            res += str(i)+', '
    print('The '+str(n)+'th'+' rarest number in '+str(list)+' is '+res)