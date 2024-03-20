from mytest import A, B
import rlcompleter
c = rlcompleter.Completer()


print(A.size, isinstance(A.size, property))
print(B.size, isinstance(B.size, property))

b = B()

c.complete('b.', 0)
print (c.matches)

b.size = 0
c.complete('b.', 0)
print (c.matches)

