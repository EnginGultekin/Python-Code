# Loops

print("**********\nKullanıcı Girişi\n**********\n")

# Sistemde Kayıtlı Olduğunu Düşündüğümüz Kullanıcı
sysUserName = "EnHan"
sysPassword = "1598"
attempts = 3

# Kullanıcı Doğru Giriş Yaptığında ve Giriş Hakkı bittiğinde sona erecek.
while True:
    userName = input("User Name: ")
    password = input("Password: ")

    if userName != sysUserName and password == sysPassword:
        print("User Name Wrong...")
        attempts -= 1
        print("Number of Attempts: ", attempts)

    elif userName == sysUserName and password != sysPassword:
        print("Password Wrong...")
        attempts -= 1
        print("Number of Attempts: ", attempts)

    elif userName != sysUserName and password != sysPassword:
        print("User name and password wrong...")
        attempts -= 1
        print("Number of Attempts: ", attempts)

    else:
        print("Login Successful...")
        break
    if attempts == 0:
        print("Number of Attempts done...")
        break
