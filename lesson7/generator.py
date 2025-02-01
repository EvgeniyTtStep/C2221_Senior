def degrees(num, max_degree):
    i = 0
    for item in range(max_degree):
        yield num * i
        i+=1

res = degrees(10, 15)

print(res)

for i in res:
    print(i)

print("==============")

for i in res:
    print(i)