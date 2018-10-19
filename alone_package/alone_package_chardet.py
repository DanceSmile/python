'''
chardet 用来检测编码，简单高效
'''

import chardet

# 对bytes进行编码检测，结果是ascii，confidence为１表示概率为100%
c = chardet.detect(b'hello world')
print(c)
# {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}

# 检测的编码是GB2312，注意到GBK是GB2312的超集，两者是同一种编码，检测正确的概率是74%，language字段指出的语言是'Chinese'。
data = '离离原上草，一岁一枯荣'.encode('gbk')
c = chardet.detect(data)
print(c)
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

'''
用chardet检测编码，使用简单
获取到编码后，再转换为str，就可以方便后续处理。
'''
