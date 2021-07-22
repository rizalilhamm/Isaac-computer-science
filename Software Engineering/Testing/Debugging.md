# Debugging
Debugging is the process of detecting and removing existing and potential errors (also called 'bugs') in software code that can cause it to behave unexpectedly or crash.

### Syntax Error
Syntax error is error that occur because you do not follow the rules of language that you use, here is example in python]
```python
def say_hello():
    print("Hello World)

```
will return
```
SyntaxError: EOL while scanning string literal
```

### Semantic Error
Semantic errors are where there is improper use of a program code statement.
```python
def add():
    a = b + c
    return a
```
error because we reference to undefined variable (**b** and **b**)

### Logical Error
Logic errors are those that are made by the programmer (or the person who specified the program design). With a logic error, the program can be run without failing, but it does not produce the correct result.

Here's are resources:
* [ISC - Debugging](https://isaaccomputerscience.org/concepts/prog_softeng_debug?topic=testing)
* [Economictimes - Debugging](https://economictimes.indiatimes.com/definition/debugging)