from classtak import Stack



s1 = Stack()
s2 = Stack()
s3 = Stack()


s1.push(3)
s1.push(2)
s1.push(1)

print(s2.push(s1.pop()))
print(s3.push(s1.pop()))
print(s3.push(s2.pop()))
print(s2.push(s1.pop()))
print(s1.push(s3.pop()))
print(s2.push(s3.pop()))
print(s2.push(s1.pop()))
