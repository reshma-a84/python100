indian_states = ["Andhra Pradesh", "Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa", "Gujarat","Haryana","Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", 
"Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram"
"Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttarakhand","Uttar Pradesh ","West Bengal"]

positive_index = input("Enter positive index: ")
negative_index = input("Enter negative index: ")
print("State of india in positive index is " + indian_states[int(positive_index)])  #Takes the list from beginning

print("State of india in negative index [-1,-2 etc] is " + indian_states[int(negative_index)]) #Takes the list from end

print("Total number of States of india is " , len(indian_states))
# Reference :https://docs.python.org/3/tutorial/datastructures.html