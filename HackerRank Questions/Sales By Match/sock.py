def sockMerchant(n, ar):
    temp_list = []
    count = 0

    for i in range(n):
        if ar[i] not in temp_list:
            temp_list.append(ar[i])
        else:
            for j in range(len(temp_list)):
                if ar[i] == temp_list[j]:
                    temp_list.pop(j)
                    count += 1 
                    break
                
    return count