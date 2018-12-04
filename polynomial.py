class Polynomial:
    def __init__(self, deg=0, coeffs=[0], pairs=None):
        """
            coefficients are from lower degree to higher.
            a0 + a1 x + a2 x^2 + ... + an x^n
        """
        assert deg == len(coeffs) - 1
        self.deg = deg
        self.coeffs = coeffs
        self.pairs = pairs

    def multiply(a, b):
        c = [0 for _ in range(a.deg + b.deg + 1)]
        for x in range(a.deg + 1):
            for y in range(b.deg + 1):
                c[x+y] += a.coeffs[x] * b.coeffs[y]
        return Polynomial(a.deg + b.deg, c)

    def eval_at(self, x):
        """
            x is the list of x values to evaluate the polynomial.
        """
        if type(x) is not list:
            x = [x]
        y = []
        for i in x:
            y_i = 0
            for d in range(self.deg+1):
                y_i += self.coeffs[d] * (i ** d)
            y.append(y_i)
        if len(x) >= d + 1:
            self.pairs = list(zip(x,y))
        return y
