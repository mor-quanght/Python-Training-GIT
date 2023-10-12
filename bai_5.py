#Bai 5. Viết chương trình Python nhập một dãy số nguyên, sau đó kiểm tra xem nó có khả đối xứng không?
# Nếu có, hãy biến đổi nó để được một dãy đối xứng.

def doi_xung():
    day_so=int(input('Nhap day so:'))
    set_left=set()
    set_right=set()
    my_list=list(str(day_so))
    id=0

    while id < len(my_list)//2:
        set_left.add(my_list[id])
        set_right.add(my_list[-(id+1)])
        id+=1

    if set_left-set_right!=set():
        return 'Khong co kha nang doi xung'
    else:
        id=0
        while id < len(my_list)//2:
            my_list[-(id+1)]=my_list[id]
            id+=1
        output = ''.join(my_list)

        return output


print(doi_xung())

