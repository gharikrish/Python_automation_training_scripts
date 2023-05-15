xyz123 = ["1.1.1.1","2.2.2.2",'3.3.3.3']
print(xyz123)

xyz123 = ["1.1.1.1","2.2.2.2","3.3.3.3"]
print(len(xyz123))

#String and Number inside List array:
list1 = ['abc',32,True,40,"male"]
print(list1)
#type()
xyz123 = ["1.1.1.1","2.2.2.2","3.3.3.3"]
print(type(xyz123))

#changeable allowed
xyz123 = ["1.1.1.1","2.2.2.2","3.3.3.3"]
xyz123[1] = "192.168.1.1"
print(xyz123)

#append
numbers = [1,2,3]
numbers.append(4)
print(numbers)

#extend
numbers = [1,2,3]
numbers.extend([4,5,6])

#insert
numbers = [1,2,4]
numbers.insert(2,3)
print(numbers)

#remove
numbers = [1,2,3,2]
numbers.remove(2)
print(numbers)

#pop
numbers = [1,2,3]
last = numbers.pop()
print(last)

#clear
numbers = [1,2,3,4]
numbers.clear()
print(numbers)

#list.index
numbers = [1,2,3,2]
index = numbers.index(2)
print(index)

#list.count
numbers = [1,2,3,2]
count = numbers.count(2)
print(count)

#sort
numbers = [3,1,2]
numbers.sort()
print(numbers)

#reverse
numbers = [1,2,3]
numbers.reverse()
[print(numbers)]

print("------------list_over---------------")
deviceinfo = {
    "ip":"1.1.1.1",
    "username":"admin",
    "password":"cisco"
}

print(deviceinfo)
print(deviceinfo["username"])

deviceinfo["username"] = "Tom"
print(deviceinfo)

comp = {"key1":"cisco","product":"nexus","version":"2.2.1"}
print(comp["key1"])

comp["key4"] = "18.4.2023"
print(comp)

if "key1" in comp:
    print("key found")
del comp["key1"]
print(comp)
val = comp.get("key1",'default value')
print(val)

print(len(comp))

for key in comp.keys():
    print(key)

for value in comp.values():
    print(value)

upd = {"key5":"cisco"}
comp.update(upd)
print(comp)

for key,value in comp.items():
    print(key,value)

new = comp.copy()
comp.clear()
print(comp)
print(new)
