Employee_Name=["Bharat","Shailesh","Sushri"];

for names in Employee_Name:
    print names

#Reverse the list
Employee_Name.reverse()


print "Reversing the List"
for names in Employee_Name:
    print names

Employee_Name.append("Girish")
print "Sorting the List"
Employee_Name.sort()


for names in Employee_Name:
    print names

print "Append  the List"
#Append in the List
Employee_Name.append("Gaurav")
for names in Employee_Name:
    print names

# List Slicing
print "Slice  the List"
print (Employee_Name[1:5])

