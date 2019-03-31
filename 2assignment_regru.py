# -*- coding: utf-8 -*-

def check(text): #на самом деле, не знаю даже, что здесь объяснять, несложно же
    if type(text) == str:
        stack = [] #для скобок
        brackets = [('{', '}'), ('(', ')'), ('[', ']')]
        start = 0 #положение в паре открывающей скобки
        end = 1 #положение в паре закрывающей скобки
        for i in range(len(text)):  #цикл по text
            for j in range(len(brackets)): #цикл по парам скобок
                if text[i] == brackets[j][start]: #проверка на наличие скобок на данной позиции
                    stack.append(text[i]) #добавление скобок в stack
                elif text[i] == brackets[j][end]:
                    if len(stack) > 0:
                        if stack.pop() != brackets[j][start]: #условие закрытия скобок
                            return False
                    else:
                        stack.append(text[i])                    
        
        if len(stack) == 0: #если все скобки закрыты, то 
            return True
        
    return False
                    