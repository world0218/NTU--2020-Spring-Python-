itemsA = {"蘋果", "香蕉", "鳳梨", "芭樂"}# 這是第一個集合
itemsB = {"鳳梨", "蘋果", "水梨", "蓮霧"}# 這是第二個集合

itemsA.add(input())
itemsA.add(input())
itemsA.remove('蘋果')

itemsB.add(input())
itemsB.add(input())
itemsB.remove('蓮霧')

print('iA:',sorted(list(itemsA)))
print('iB:',sorted(list(itemsB)))
print('union:',sorted(list(itemsA|itemsB)))
print('intersection:',sorted(list(itemsA&itemsB)))
print('A diff B:',sorted(list(itemsA.difference(itemsB))))
print('B diff A:',sorted(list(itemsB.difference(itemsA))))
print('A xor B:',sorted(list(itemsA^itemsB)))
