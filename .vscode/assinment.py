
users = {'Nathan':'2313','Geez':'pass231','Abebe': '092313133', 'miki':'pl3as34D0ntH4ckM3'}

for x in range(5):
        
        key1 = input('enter username: ')
        key2 =input ('enter the password: ')
        if key1 in users and users[key1] == key2:
            print('welcome to GTST company!')
            break
        else:
            if x < 4:
                print('incorrect login')
            else:
                print('Sorry You Are Limited!')
                quit()                                
