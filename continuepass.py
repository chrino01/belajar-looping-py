
# continue pass break

# pass

angka= 0

# while angka<5:
#     angka+=1
#     if angka==3: #kondisi ini tidka akan di eksekusi hanya sebagai dummy
#         pass
#     print(f"sekarang angka ke-{angka}")


# continue

while angka<5:
    angka+=1
    print(f"Sekarang angka ke-{angka}")
    if angka==3:
        print("anjayy") #untuk continue jika kondisi true maka looping akan melanjutkan ke step looping berikutnya tidak menjalankan program bawahnya 
        continue
    
    print("gege juga kau")

print("END")