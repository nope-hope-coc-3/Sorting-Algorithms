'''first the array arr is divided into 3 parts with m1 and m2 as its two middle elements index and
s and e are the starting and ending index of the input array arr respectively
arr is divided into 3 sub-arrays with two middle elements index m1 and m2'''

#function for sorting each sub-array after dividing the array into 3 parts
def merge_sort(arr, s, e):

    if len(arr[s-1 : e]) < 2:
        return arr
    else: 
        m1 = s + ((e - s) // 3)
        m2 = s + 2 * ((e-s) // 3)

        merge_sort(arr, s, m1) #sorting of leftmost array from index s to m1
        merge_sort(arr, m1+1, m2 + 1)  #sorting of middle array from index m1+1 to m2+1
        merge_sort(arr, m2+2, e)  #sorting of righttmost array from index m2+2 to e
        merge(arr, s, m1, m2, e) #merging of all the three sorted arrays 
        return arr              #it returns the sorted array

#function for merging all the three sorted arrays into a single array 
def merge(arr, s, m1, m2, e):

    left_arr = arr[s-1 : m1] 
    mid_arr = arr[m1: m2+1]
    right_arr = arr[m2+1 : e]

    left_arr.append(float('inf')) #float('inf') is used to represent an infinite integer
    mid_arr.append(float('inf'))
    right_arr.append(float('inf'))
    
    ind_left = 0  #starting index of leftmost array
    ind_mid = 0   #starting index of middle array
    ind_right = 0 #starting index of rightmost array
    for i in range(s-1, e):
        minimum = min([left_arr[ind_left], mid_arr[ind_mid], right_arr[ind_right]]) #finds the minimum element
        if minimum == left_arr[ind_left]:
            arr[i] = left_arr[ind_left]
            ind_left += 1              #increments left array index to 1
        elif minimum == mid_arr[ind_mid]:
            arr[i] = mid_arr[ind_mid]
            ind_mid += 1               #increments middle array index to 1
        else:
            arr[i] = right_arr[ind_right]
            ind_right += 1          #increments left array index to 1
    
arr = [52,41,7,19,1,3,78,1,99,29] #taken a random unsorted array as an argument for the above function
s = 1 #Starting index of arr is 1 to comprise with code errors while dividing the array
e = len(arr) #calculating and storing the length of the array into e
print (merge_sort(arr, s, e)) #prints the final sorted array
