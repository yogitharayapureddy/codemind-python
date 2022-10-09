def add(address):
    naddress=""
    saddress=address.split(".")
    s="[.]"
    naddress=s.join(saddress)
    return naddress
iaddress=add(input())
print(iaddress)