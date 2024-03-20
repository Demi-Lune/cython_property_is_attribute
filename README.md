A small cython class to show that Cython `@property` is problematic with rlcompleter.

See https://github.com/python/cpython/issues/112821

```
make
cd test ; python3 test1.py
```
throws the `RuntimeError`. 

Completion is also broken in repl:
```
>>> from mytest import A, B
>>> b = B()
>>> b.size
42
>>> b.<TAB><TAB>
b.name  b.size
>>> b.size = 0
>>> b.<TAB><TAB>
# no completion
```
