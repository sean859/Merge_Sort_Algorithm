# This imports pandas into the project allowing you to utilize it to read the excel file
import pandas as pd 

# This line declares a variable called 'data' that holds all the information from the excel file
data = pd.read_excel(r'C:\Users\seana\Desktop\rugby_players_data.xlsx')

# This prints the data to make sure its right 
print(data)

# This makes a new list called 'Agedata' that will hold all the data from the excel file under the column labeled 'Age'
Agedata = list(data.Age)

# This will print it to show the datas correct
print(Agedata)

# This is the merge sort algorithm consiting of two functions 

# This function essentially takes the split up list and continues to split it until the sublist have a total value of one
# to which the algorithm will now start working backwards, sorting the data as it goes along until it has one full sorted list
# just the way the merge sort works normally 
def merge(left, right):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result
# This function essentially breaks the full unsorted list up into two sublists, with it being an even amount in each list
# if its an odd number list then it will place the extra value in the sublist on the left, once the sublist have been created
# it sends those sublists to the main merge function above labeled as 'left' and 'right'
def mergesort(lst):
    if(len(lst) <= 1):
        return lst
    mid = int(len(lst)/2)
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left, right)
# Then this last bit of code will call the mergesort function and assign it the list we have, being 'Agedata' which is just
# all the values from the excel spreadsheet 'Age' column, then it prints the results of the full sorted list
print(mergesort(Agedata))

