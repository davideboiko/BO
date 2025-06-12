def merge_intervals(intervals):


    lista_n = []

    for i in range(len(intervals)-1):

        if intervals[i][i] != intervals[i+1][i-1]:
            





print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])) # restituisce [[1, 6], [8, 10], [15, 18]] 
print(merge_intervals([[1, 4], [4, 5]])) # restituisce [[1, 5]]
