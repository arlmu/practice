
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0<= score <= 100:
            self._score = score
        else:
            raise ValueError('bad score')


bart = Student('Bart', 90)

bart.print_score()
print(bart.score)
print(bart.name, bart.get_grade())




