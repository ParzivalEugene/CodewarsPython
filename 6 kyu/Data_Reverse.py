def data_reverse(data):
    arr = []
    print(data)
    for i in range(len(data) // 8):
        arr.append(data[i * 8:(i + 1) * 8])
    res = []
    for i in arr[::-1]:
        res.extend(i)
    return res

