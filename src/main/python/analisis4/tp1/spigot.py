
def pi_digits(n):
    """Yields a generator with the amount n digits of pi specified as a function argument"""
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while n > 0:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
        d, d1 = a / b, a1 / b1
        while d == d1 and n > 0:
            yield int(d)
            n -= 1
            a, a1 = 10 * (a % b), 10 * (a1 % b1)
            d, d1 = a / b, a1 / b1

def print_n_pi_digits(n):
    """Prints n digits of pi, with n specified as a function parameter."""
    digits = pi_digits(n)
    print(str(next(digits)))
    print('{}{}{}'.format(str(next(digits)), '.', ''.join([str(next(digits)) for j in range(n-1)])))

def pi_decimal_digits():
    """Generates digits of pi using Jeremy Gibbon's spigot generator, a streaming algorithm."""
    q, r, t, j = 1, 180, 60, 2
    while True:
        u, y = 3*(3*j+1)*(3*j+2), (q*(27*j-12)+5*r)//(5*t)
        yield y
        q, r, t, j = 10*q*j*(2*j-1), 10*u*(q*(5*j-2)+r-y*t), t*u, j+1

def print_pi_digits():
    """Prints an infinite amount of pi digits in lines of 50 digits each."""
    count, digits = 0, pi_decimal_digits()
    while 1:
        print('{}{} {}'.format(
            count, ':', ''.join([str(next(digits)) for j in range(50)])))
        count += 50

def print_n_digits_of_pi(n):
    """Prints n digits of pi, with n specified as a function parameter."""
    digits = pi_decimal_digits()
    print('{}{}{}'.format(str(next(digits)), '.', ''.join([str(next(digits)) for j in range(n)])))

#print_pi_digits()
#print_n_digits_of_pi(100)
#print_n_pi_digits(100)

def get_nth_pi_digit(n):
    """Returns the nth digit of pi"""
    digits = pi_decimal_digits()
    for i in range(n-1):
        next(digits)
    return next(digits)

#print(get_nth_pi_digit(100))

print_pi_digits()

