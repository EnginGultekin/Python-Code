# Conditional States

# User Login

print("**********\nKullanıcı Girişi\n**********\n")

# Sistemde Kayıtlı Olduğunu Düşündüğümüz Kullanıcı
sysUserName = 'el'
sysPassword = '123'

userName = input('Kullanıcı adınızı giriniz: ')
password = input('Parolanazı giriniz: ')

if sysUserName != userName and sysPassword == password:
    print('Kullanıcı adı hatalıdır')
elif sysUserName == userName and sysPassword != password:
    print('Parola Hatalıdır')
elif sysUserName != userName and sysPassword != password:
    print("Kullanıcı adı ve parola hatalıdır")
else:
    print("Kullanıcı girişi başarılıdır")
