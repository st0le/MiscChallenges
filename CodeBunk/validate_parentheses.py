"""
Given a string of arbitrary size composed of the following characters '(', ')', '{', '}', '[', and ']'.

Print if its valid.

"""
a = "{{}}([])"
b = "[{(}]{}"
c = "())"
d = "((words)go)here"

def check(s):
  stack = []
  valid = "() [] {}".split()
  for c in s:
    if c in "([{":
      stack.append(c)
    elif c in ")]}":
      if not stack or stack.pop()+c not in valid:
        return False
  return True


print a,check(a)
print b,check(b)
print c,check(c)
print d,check(d)
