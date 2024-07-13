# there are two MAIN types of sorting algorithms:
# bubble sorting and insertion sorting 
# bubble sorting takes a list, takes two neighbours, compares them (based on ascending or descending), and if the condition
# for the sorting is incorrect, they are just swapped. then, it moves on to the next set and repeats until sorted. 
# it keeps going until it hits the last index number, then one pass is completed. 
# it goes back to the first index number to double check, and the process repeats until there's no errors found. 
# bubble sorting time complexity is O(n^2)
# the number of passes equates to the number of index numbers you have 


bubble=[52,12,78,39,18,90,100]

for i in range(0,len(bubble)):
    for j in range(i,len(bubble)):
        if bubble[i] > bubble[j]:
            temp=bubble[i]
            bubble[i]=bubble[j]
            bubble[j]=temp 
    print(bubble)
    print() 
