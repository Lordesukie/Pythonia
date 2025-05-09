originals = ["Klaus","Elijah","Rebecca","Hope","Chucky"]
role_models = ["Azula","Chucky","Sasuke","The Flash","Weiss","Killer Frost"]
print("Role models are ",role_models)
print("The favorite role model is ",role_models[0])
print("Another great role model is ",role_models[-1])
print("Without accounting for Azula, the remaining models are ",role_models[1:])

#This code will grab all elements after 1 but before 4, exclduing element 4 as well
print("The models at the middle of the list are ",role_models[2:4])

role_models[1] = "Blackpink Lisa"
print("The value of Chucky is now ",role_models[1])

#other methods with lists
role_models.extend(originals)
print(role_models)
role_models.append("Chucky Wife")
role_models.append("Chucky")
print(role_models)

#To insert into the middle or any specific position
role_models.insert(2,"Blackpink Jennie")
print(role_models)
#To remove a list element
role_models.remove("Elijah")
print("Chucky has taken Elijah out: \n",role_models)

#role_models.clear() will clear the entire list, role_models.pop() will remmove the last element in the list
#you can also check to see the index of an element
print("////////////////////////////")
print("Chucky was last seen at index number ",role_models.index("Chucky"))

#You can also check to see how many items an element values appear in the list
print("The crew of Chucky are curently",role_models.count("Chucky"))

#You can sort the elements and also use .reverse() to reverse the order
role_models.sort()
print(role_models)

#To copy a list
role_models2 = role_models.copy()

