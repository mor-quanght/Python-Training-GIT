#Bai 5. Viết chương trình Python nhập một dãy số nguyên, sau đó kiểm tra xem nó có khả đối xứng không? Nếu có, hãy biến đổi nó để được một dãy đối xứng.

def doi_xung(day_so):
        to_string=str(day_so)
        if to_string==to_string[::-1]:
            print(day_so)
        else:
            to_list=list(to_string)
            id=0
            while id<len(to_string)//2:
                to_list[-(id+1)]=to_list[id]
                id+=1
            out_put= ''.join(to_list)

            return int(out_put)

day_so=1234

print(doi_xung(day_so))