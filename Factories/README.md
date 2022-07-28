## Factory Method and Abstract Factor

### Motivation
- Object creation logic becomes too convoluted
- Initializer is not descriptive
> Name is always __init__
> Cannot overload with same sets of arguments different names
> Can turn into 'optional parameter hell'

- Wholesale object creation (no-piecewise, unlike Builder) can be outsourced to
> A separate method (Factor Method)
> That may exist in a separate class (factory)
> Can create hierarchy of factories with Abstract Factory


### Formal definition
- A component responsible solely for the wholesale (not piecewise) creation of objects.