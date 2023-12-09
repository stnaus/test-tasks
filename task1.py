'''
1. Реализовать два класса: First и Second 
- в результате вызовов функции getClassname() у объекта класса First должно выводиться сообщение "First"
- в результате вызовов функции getClassname() у объекта класса Second должно выводиться сообщение "Second"
- в результате вызовов функции getLetter() у объекта класса First должно выводиться сообщение "A"
- в результате вызовов функции getLetter() у объекта класса Second должно выводиться сообщение "B"
Суммарно для двух классов должно быть реализовано 3 (три) метода.
'''


class First:

    name = "First"

    def getClassname(self):
        return self.name

    def getLetter(self):
        return "A"


class Second(First):

    name = "Second"

    def getLetter(self):
        return "B"


first = First()
second = Second()


print('getClassname() method:\n1. ' + first.getClassname() +
      '\n2. ' + second.getClassname())

print('getLetter() method:\n1. ' + first.getLetter() +
      '\n2. ' + second.getLetter())
