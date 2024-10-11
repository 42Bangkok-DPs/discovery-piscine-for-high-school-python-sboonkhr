#!/usr/bin/env python3
Original_array = [2, 8, 9, 48, 8, 22, -12, 2]
New_array = [ ]
for i in range(len(Original_array)):
 New_array =  New_array + [Original_array[i] + 2]
print("Original array" , Original_array)
print("New array:", New_array)
