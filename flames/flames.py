def flames(name1, name2):
    for i in range(len(name1)):
        for j in range(len(name2)):
            if(name1[i]==name2[j]):
                 name2=name2.replace(name2[j],"*")
                 break
    #print(name1)
    #print(name2)
    t=name2.count('*')*2
    print(t)
    results = ['friend','love','affection','marriage','enemy','sister']
    t=len(name1)+len(name2)-t-1
    #print(t)
    i=-1
    while(len(results)>1):       
        count=-1
        while(count<t):
            count=count+1
            i=(i+1)%len(results)            
        results.remove(results[i-1])      
    return results[0]
        
name1 = input('Enter name of first person: ').casefold()
name2 = input('Enter name of second person: ').casefold()
print('Relationship is', flames(name1, name2))
