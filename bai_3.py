#Bai 3.Với số nguyên n nhất định, hãy viết chương trình để
# tạo ra một dictionary chứa (i, i*i)
# như là số nguyên từ 1 đến n (bao gồm cả 1 và n)
# sau đó in ra dictionary này.


def tao_dictionary(n):
    dict={}
    for i in range(1,n+1):
            dict[i]=i*i
    return dict


print(tao_dictionary(10))