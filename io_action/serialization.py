'''
我们把变量从内存中变成可存储或传输的过程称之为序列化
'''

import pickle

user = dict(name='zero', age=20)

# 获取序列化之后的字节
r = pickle.dumps(user)
# b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x04\x00\x00\x00zeroq\x02X\x03\x00\x00\x00ageq\x03K\x14u.'

# 直接写入序列化之后的字节

f = open('d','wb')
r = pickle.dump(user, f)

# 反序列化

# 读取文件内容 然后反序列化
with open("d",'rb') as f:
    r = pickle.loads(f.read())
    print(r)

# 又或者直接反序列化
r = pickle.load(open('d',"rb"))
print(r)