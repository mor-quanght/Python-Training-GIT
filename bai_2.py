def tinh_giai_thua(n):
    if n==0 or n==1:
        return 1
    else:
        return tinh_giai_thua(n-1)*n


print(tinh_giai_thua(10))