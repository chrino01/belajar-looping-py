# # latihan looping segitiga

# sisi=9

# # dummy variabel
# count = 1

# print("menggunakan for loop")
# for i in range(sisi):
#     print("*"*count)
#     count +=1

# print("Menggunakan while")
# count=1
# while True:
#     print("*"*count)
#     count+=1

#     if count>sisi:
#         break

# print("Whiile ganjil")

# count=1
# while True:
#     if (count%2):
#         print("*"*count)
#         count+=1
        
#     else:
#         count+=1
#         continue

#     if count>sisi:
#         break

# print("segitiga sama sisi")

# count=1
# space=int(sisi/2)
# while True:
#     if (count%2):
#         print(" "*space,"+"*count)
#         space-=1
#         count+=1
        
#     else:
#         count+=1
#         continue

#     if count>sisi:
#         break
# print("akhir while sama kaki \n")
sisi=7
print("belah ketupat")
count=1
while True:
    print(" " * (sisi-count)+"+"*count)
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
# for x in range(h - 2, -1, -1):
#     print(" " * (h - x), "*" * (2*x + 1))
    