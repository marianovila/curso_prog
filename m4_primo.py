
def is_prime(valor):
    contador=0
    for i in range(2,valor):
        if valor%i==0:
            contador=contador+1
    if contador==0:
        return True
    else:
         return False   
    

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()