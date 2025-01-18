import hashlib
i,h=0,open("input.txt","rb").read().strip()
while not hashlib.md5(b"%b%i"%(h,i)).hexdigest().startswith("0"*5):i+=1
print(i)