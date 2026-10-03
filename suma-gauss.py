x = int(input("a1 = "))
an = int(input("an = "))
pas=int(input("pas = "))
n=(an-x )//pas+1
print(f"({an}-{x}):{pas}+1" )
l=an-x
print(f"{l}:{pas}+1")
m= l//pas
print(f"{m}+1")
a=m+1
h=(x+an)
print(f"[{n}*({x}+{an})]:2")
print(f"=[{n}*{h}]:2")
p=int(n*h)
print(f"{p}:2")
s=(p//2)
print(f"= {s}")