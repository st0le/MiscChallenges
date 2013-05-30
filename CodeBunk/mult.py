#Without using the multiplying operator, find the product of two integers.
def mult(a,b):
    def _mult(a,b):
        p2 = 1
        s = 0
        while p2 <= b:
            if b & p2:
                s += a
            a = a + a
            p2 = p2 << 1
        return s
    return _mult(abs(a),abs(b)) if (a <= 0 and b <= 0) or (a > 0 and b > 0) else -_mult(abs(a),abs(b))

print mult(13,-1)