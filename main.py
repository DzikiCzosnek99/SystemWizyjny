from Image import dataImage
from Participation import Participation1

arr = []

for i in range(1, 10):
    arr.append(dataImage(f"photos/s1/p{i}.jpg"))

p1 = Participation1(arr)
print(p1.perc)

