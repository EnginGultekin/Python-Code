# Conditional States

# if-else Koşul Durumları

num = 2  # Blok 1 'e ait kod

if num == 2:
    print(num)  # Blok 2'ye ait kod
print("Say Hello")  # Blok 1 ' ait kod

if num == 3:
    print(num)  # Blok 2'ye ait kod
print("Say Hello")  # Blok 1 ' ait kod

print("------------------")

# 18 yaş kontrolü
age = int(input("Enter your age: "))

if age < 18:
    # if bloğu -  Girinti ile sağlanıyor.
    print("Your age under the 18. You can't enter")
else:
    # else bloğu -  if koşulu sağlanmazsa çalışacak.
    print("Welcome this place.")
