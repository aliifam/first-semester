#oop inherit
class Manusia(object):
    nama = None
    
    def __init__(self, nama):
        self.nama = nama
    
    def makan(self):
        print('{} makan nasi', format(self.nama))

class ManusiaMillenial(Manusia):
    email = None
    
    def email(self, email):
        self.email = email
    
    def info(self):
        print('nama = {}, email = {}'.format(self.nama, self.email))
        
programmer = ManusiaMillenial('aliif')
programmer.email('aliif@test.com')
programmer.info()

