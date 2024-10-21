class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs
    
    def __repr__(self) -> str:
        return f'Polynomial({self.coeffs})'
    
    def __str__(self) -> str:
        return f"Here's the result: Polynomial({self.coeffs})"
    # If this is defined then python will prefer this for print(), str() or format().
    # When you use !r in the formatted string then repr() is called

    def __add__(self, other):
        return Polynomial(*(x+y for x, y in zip(self.coeffs, other.coeffs)))
    
    def print_name():
        print('Hello')

p1 = Polynomial(1, 2, 3)
p2 = Polynomial(2, 3, 4)

print('{!r} this is the result of sum'.format(p1+p2))
# if you call !r explicitly then repr() method is called even if str() is defined