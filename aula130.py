'''
211. method vs @classmethod vs @staticmethod
# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
'''
class Connection:
    def __init__(self,host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self,user):
        self.user = user
    
    def set_password(self,password):
        self.password = password
    
    @classmethod
    def create_with_auth(cls,user,password):
        Connection = cls()
        Connection.user = user
        Connection.password = password
        return Connection
    
    @staticmethod
    def log(msg):
        print('log:',msg)

def connection_log(msg):
    print('log:',msg)

# c1 = Connection()
c1 = Connection.create_with_auth('LUIZ','1234')
# c1.set_user('luiz')
# c1.set_password('123')
print(Connection.log('Essa é a mensagem de log'))
print(c1.user)
print(c1.password)