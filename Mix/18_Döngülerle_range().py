
# range() fonksyonu range(başlangıc , bitiş)

range(0,10)
print(range(0,10))

print(*range(0,10))

print(*range(10))

print(*range(0,100,10))

print(*range(10,0))    # Birşey yazmaz
print(*range(10,0,-1))

for x in range(0,10):
	print("*" * x)