
Cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
Cities2 = {"Tokyo", "Madrid", "Seoul", "Kabul"}

# Union operation

union_Cities = Cities.union(Cities2)
print(union_Cities)
print('\n') 

# Intersection operation

intersection_Cities = Cities.intersection(Cities2)
print(intersection_Cities)
print('\n') 

# Intersection.update operation

Cities.intersection_update(Cities2)
print(Cities)
print('\n')

# Symmetric Difference operation
# This operation updates the all the uncommon cities.

symmetric_difference_Cities = Cities.symmetric_difference(Cities2)
print(symmetric_difference_Cities)
print('\n') 

# Difference operation

MyDifference = Cities.difference(Cities2)
print(MyDifference)
print('\n')

# IsDisJoint Operation 

print(Cities.isdisjoint(Cities2))
print('\n')


