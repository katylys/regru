# -*- coding: utf-8 -*-
'''
Тесты:
    >>> human1 = Person()
    Need more argument

    Удачный брак: 
    >>> human1 = Man("kolya")

    >>> human11 = Woman("yulya")

    >>> human1
    Out[75]: kolya

    >>> human1.wife = human11
    Be happy
    
    >>> human1.wife
    Out[81]: yulya
    
    >>> human11.husband
    Out[82]: kolya
    
    Однополый брак:
    >>> human2 = Man("jorg")

    >>> human22 = Man("pol")
    
    >>> human2.marry(human22)
    You are in Russia
'''

class Person(object):
    
    def __new__(cls,*args): #проверка на отсутствие имени
        if len(args) != 1:
            del cls 
            print("Need more argument")
            return None
        return object.__new__(cls) 
    
    def __init__(self, *args): #если __new__ нашел имя
        self._name = args[0]            
    
    name = property() #для отказа от self.getname и self.setname
    
    @name.setter
    def name(self, somename):
        self._name = somename
        
    @name.getter
    def name(self):
        return self._name
             
    
    def __str__(self): #для вывода имени при вызове print()
        return self._name
    
    def __repr__(self): #для вывода имени при вызове самого объекта
        return self._name
        
    def marry(self, person): #свадьба))))
        if self.sex == 'w':
            self.husband = person
        else:
            self.wife = person
        
        
class Man(Person):
    def __init__(self, *args):
        self._wife = None 
        self.sex = 'm'
        super(Man, self).__init__(*args)
        
    wife = property()
        
    @wife.setter   
    def wife(self, Woman): 
        if (Woman.sex == 'w'):
            if self._wife != Woman:
                self._wife = Woman
                Woman.husband = self
                print("Be happy") #признак благополучной свадьбы
        else:
            print("You are in Russia") #сообщение о невозможности однополого брака
            
    @wife.getter
    def wife(self):
        return self._wife
    
class Woman(Person):
    def __init__(self, *args):
        self._husband = None
        self.sex = 'w'
        super(Woman, self).__init__(*args)
        
    husband = property()
            
    @husband.setter
    def husband(self, Man):
        if (Man.sex == 'm'):
            if self._husband != Man:
                self._husband = Man
                Man.wife = self
        else:
            print("You are in Russia")
    
    @husband.getter
    def husband(self):
        return self._husband

