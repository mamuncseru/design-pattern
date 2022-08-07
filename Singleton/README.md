# Singleton
A design pattern everyone loves to hate... but is it really that bad?

When discussing which patterns to drop, we found that we still ove them all. (Not really I'm in favor of dropping Singleton. Its use is almost alawys a design smell.)
---Erich Gamma

### Motivation
- For some components it only makes sense to have one in the system
    * Database repository
    * Object factory

- E.g., the initializer call is expensive
    * We only do it once
    * We provide everyone with the same instance


- Want to prevent anyone creating addition copies
- Need to take care of lazy instantiation

## Formal definition
- Singleton is a component which instantiated only once.