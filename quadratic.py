# Replace the "ANSWER HERE" for your answer

# Replace the "ANSWER HERE" for your answer
import math     
def roots (a, b, c):
    discriminante = (b**2-4*a*c)
    if discriminante<0 : return ("( )")
    else:
        raiz_1 = ((-b+math.isqrt(discriminante))//2*a)
        raiz_2 = ((-b-math.isqrt(discriminante))//2*a)
        raiz_1 = float (raiz_1)
        raiz_2 = float (raiz_2)
        if (discriminante)>0: return (f"({raiz_1}, {raiz_2})")
        else: return (f"({raiz_1})")

def value_y(a, b, c, x):
    return (a*(x**2)+b*x+c)


def to_string(a, b, c):
    if a==0 and b==0:return (f"f(x) = {c}")
    elif a==0 : return (f"f(x) = {b} * X + {c}")
    elif b==0 : return (f"f(x) = {a} * X^2 + {c}")
    elif c==0 : return (f"f(x) = {a} * X^2 + {b} * X")
    elif a==0 and b==0:(f"f(x) = {c}")
    else : return (f"f(x) = {a} * X^2 + {b} * X + {c}")


def derivation(a, b, c):
    if a ==0: return (f"f'(x) = {b}")
    elif b == 0: return (f"f'(x) = {a*2} * X")

    else: return (f"f'(x) = {a*2} * X + {b}")
