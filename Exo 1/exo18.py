def parcourir_bytearray(bytearray):
    for i in bytearray:
        print(i)
    for i in range(len(bytearray)):
        bytearray[i] += 1
    return bytearray
