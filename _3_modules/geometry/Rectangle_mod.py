class Rectangle:
    
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    # для удобства вызову значение pi как функцию
    def pi(self):
        from math import pi
        pi = pi
        return pi
    
    # расчет площади прямоугольника
    def area(self):
        area = 2 * self.width * self.length
        return area
    
    # расчет диагонали прямоугольника
    def diagonal(self):
        diagonal = (self.length ** 2 + self.width * 2) ** 0.5
        return diagonal
    
    # расчет радиуса описанной вокруг прямоугольника окружности
    def radius_out(self):
        radius_out = self.diagonal() * 0.5
        return radius_out
    
    # расчет площади описанной окружности
    def area_out(self):
        area_out = self.pi() * self.radius_out() ** 2
        return area_out
    
    # расчет площади вписанной окружности
    def area_in(self):
        area_in = self.pi() * (0.5 * min(self.width, self.length)) ** 2
        return area_in
    
    # расчет длины окружности вписанной окружности
    def length_in(self):
        length_in = self.pi() * min(self.width, self.length)
        return length_in
    
    # расчет длины окружности описанной окружности
    def length_out(self):
        length_out = self.pi() * self.diagonal()
        return length_out   