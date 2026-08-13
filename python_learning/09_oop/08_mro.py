# Method Resolution Order

class A:
    label = "A : Base class"

class B (A):
    label = "B: Masala blend"    

class C(A):
    label = "C: Herbal blend"    

class D(B,C):
   pass

cup = D()
# class written first its method is called D(B,C) -> B method is called
print(cup.label)
# this tells order 
print(D.__mro__)