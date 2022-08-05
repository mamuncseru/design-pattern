# Prototype

when it's easier to copy an existing object to fully initialize a new one.


### Motivation

- Complicated objects (e.g., cars) aren't designed from scratch
    * They reiterate existing designs
- An existing (partially or fully constructed) design is a prototype
- We make a copy (clone ) the prototype and customize it
    * Requires 'deep copy' support
- We make the cloning convenient (e.g. via a Factory)

### Formal definition
Prototype is a partially or fully initialized object that you copy(clone) and make use of.
