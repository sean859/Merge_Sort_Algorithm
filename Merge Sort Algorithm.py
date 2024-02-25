# This imports pandas and time into the project allowing you to utilize it to read the excel file, and track the time needed
import pandas as pd 
import time

# This line declares a variable called 'rugby_data' that holds all the information from the excel file
rugby_data = pd.read_excel(r'C:\Users\seana\Desktop\rugby_players_data.xlsx')


# This makes a new list called 'Agedata' that will hold all the data from the excel file under the column labeled 'Age'
Agedata = list(rugby_data.Age)


# This is the merge sort algorithm consiting of two functions 

# This function essentially takes the split up list and continues to split it until the sublist have a total value of one
# to which the algorithm will now start working backwards, sorting the data as it goes along until it has one full sorted list
# just the way the merge sort works normally 
def merge(left, right):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right): # When this is true we keep adding values into the different lists until the lists have 
        if left[i] <= right[j]:             # a value of one placing the first value in the 'left' list and doing the same for every
            result.append(left[i])          # other value (3, 5, 7, 9, 11, 13, etc) well placing the other values into the 'right' list
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result

# This function essentially breaks the full unsorted list up into two sublists, with it being an even amount in each list
# if its an odd number list then it will place the extra value in the sublist named 'left', once the sublist have been created
# it sends those sublists to the main merge function above labeled as 'left' and 'right'
def mergesort(lst):
    if(len(lst) <= 1): # This will get a new variable called 'mid' that is the value in the very middle (rounded up), and placing all
        return lst     # all values on the left side of the 'mid' value and the 'mid' value itself into the 'left' sublist, well placing
    mid = int(len(lst)/2) # all the values on the right side of the 'mid' value is then placed into the 'right' sublist
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left, right)

# Then this last bit of code will call the mergesort function and assign it the list we have, being 'Agedata' which is just
# all the values from the excel spreadsheet 'Age' column, then it prints the results of the full sorted list, well also printing
# the time needed to execute the code below it
timer_start = time.time()
print(mergesort(Agedata))
timer_ends = time.time()
full_time = timer_ends - timer_start
print('Time Taken:', full_time)

