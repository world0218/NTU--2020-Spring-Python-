itemA = {"柯南","灰原","步美","美環","光彦"}
itemB = {"柯南","灰原","丸尾","野口","步美"}


print(sorted(list(itemA-itemB)))
print(sorted(list(itemB-itemA)))
print(sorted(list(itemA&itemB)))
