from fractions import Fraction as frac

pi = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2]

# input: a list of elements describing a continued fraction
# output: decimal expansion of the continued fraction 
def cf_decimal_expansion(elements = []):
    el = elements.copy()
    if len(el)==1: return el[0]
    else: return el.pop(0) + 1/cf_decimal_expansion(el)

# input: a list of elements describing a continued fraction
# output: fraction object representation of the continued fraction 
def cf_fractional_representation(elements = []):
    el = elements.copy()
    if len(el)==1: return el[0]
    if len(el)==2: return el[0] + frac(1,el[1])
    else: return el.pop(0) + frac(1, cf_fractional_representation(el))

# input: a list of elements describing a continued fraction
# output: a list of fraction objects representing the rational convergents 
def cf_convergents(elements = []):
    output = []
    for i in range(1,len(elements)+1):
        arr = [elements[j] for j in range(i)]
        output.append(cf_fractional_representation(arr))
    return output

def cf_square_root(n):
    a = 0
    for i in range(n):
        if i**2 < n: a = i 
        else: break
    one = frac(2*a,n-a**2)
    two = 2*a
    return [a,one,two,one,two,one,two,one,two,one,two]



def euclids_algorithm(n, m):
    output = []
    a = n
    b = m
    while True:
        k = a//b
        r = a%b
        output.append([k,r])
        if r==0: break
        else:
            a = b
            b = r
    return output

def frac_to_cf(n,m):
    euclid = euclids_algorithm(n,m)
    output = []
    for i in euclid: output.append(i[0])
    return output


def dec_to_cf(n):
    output = []
    x = n
    while True:
        k = int(x // 1)
        r = x - k
        output.append(k)
        try:
            x = 1/r
        except:
            break
        if len(output)>10: break
    return output

