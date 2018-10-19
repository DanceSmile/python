'''
使用@property
'''

class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value


s = Student()
s.birth = 100
r = s.birth
print(r)
