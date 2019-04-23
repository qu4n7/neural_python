class Circle:
    
    # конструктор класса
    def __init__(self, radius):
        self.radius = radius
    
    # метод для расчета диаметра
    def diameter(self):
        diameter = 2 * self.radius
        return diameter
    
    # метод для расчета длины окружности
    def length(self):
        # не уверен, что я должен тут вызывать, но пусть так
        from math import pi
        length = round(2 * pi * self.radius, 2)
        return length
    
    # метод для расчета площади
    def area(self):
        from math import pi
        area = round(pi * self.radius ** 2, 2)
        return area