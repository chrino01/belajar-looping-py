sisi=7
print("belah ketupat")
count=1
while True:
    print(" " * (sisi-count),"+"*(2*count+1))
    print(count)
    count+=1
    if count>sisi:
        break
    
while True:
    sisi-=1
    print("+"*sisi)

    if sisi ==0:
        break







# h = eval(input("Enter diamond's height: "))

# for x in range(h):
#     print(" " * (h - x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))
    