
class complex_number:
    def __init__(self, a=None , b=None):
        self.a = a
        self.b = b


    def add(self ,C):
        result=complex_number()
        result.a = self.a + C.a
        result.b = self.b + C.b
        return result
        #Add

    def sub(self, C):
        result = complex_number()
        result.a = self.a - C.a
        result.b = self.b - C.b
        return result   
        #Sub

    def mul(self, C):
        result = complex_number()
        result.a = self.a * C.a + self.a + C.b
        result.b = self.b * C.a + self.b + C.b
        return result
        #Mul

    

    def show(self):
        return str(self.a ) + '+' + str(self.b) + 'i'

real = int(input())
image = int(input())

real = int(input())
image = int(input())

complex1=complex_number(real,image)
complex2=complex_number(real,image)

print('ADD:')
print((complex1.add(complex2)).show(),'\n')

print('SUB:')
print((complex1.sub(complex2)).show(),'\n')

print('MUL:')
print((complex1.mul(complex2)).show(),'\n')