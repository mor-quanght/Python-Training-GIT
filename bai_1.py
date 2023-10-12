# tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200).
# Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.

def tim_ds_so(danh_sach_so):
    output = ''
    for so in danh_sach_so:
        if so % 7 == 0 and so % 5 != 0:
            output += str(so) + ', '

    return output


danh_sach_so = range(2000, 3201)
print(tim_ds_so(danh_sach_so))
