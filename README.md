# Attributes and Properties

## Learning Goals

- Differentiate between variables, attributes, and properties.
- Use the `property()` function to create properties and validate input.

***

## Key Vocab

- **Class**: a bundle of data and functionality. Can be copied and modified to
accomplish a wide variety of programming tasks.
- **Initialize**: create a working copy of a class using its `__init__`
method.
- **Instance**: one specific working copy of a class. It is created when a
class's `__init__` method is called.
- **Object**: the more common name for an instance. The two can usually be used
interchangeably.
- **Object-Oriented Programming**: programming that is oriented around data
(made mobile and changeable in **objects**) rather than functionality. Python
is an object-oriented programming language.
- **Procedural Programming**: programming that is oriented around procedures
that are called in sequential order. Fortran and C are procedural programming
languages.
- **Function**: a series of steps that create, transform, and move data.
- **Method**: a function that is defined inside of a class.
- **Magic Method**: a special type of method in Python that starts and ends
with double underscores. These methods are called on objects under certain
conditions without needing to use their names explicitly. Also called **dunder
methods** (for **d**ouble **under**score).
- **Attribute**: variables that belong to an object.
- **Property**: attributes that are controlled by methods.

***

## Introduction

So far, we've learned how to build classes and give them instance methods. We
also learned how to use the `__init__` magic method to instantiate objects and
the `self` keyword to modify its **attributes**.

In this lesson, we will continue to explore attributes and **properties**, a
special type of attribute.

***

## Class Attributes vs Instance Attributes

Let's take a look at a class definition:

```py
class Human:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name
```

This class, `Human`, takes a `name` as an argument for its initialization
method and saves it as an attribute of `self`. This attribute varies from one
instance of the `Human` class to the next, so we call this an _instance
attribute_.

Since `species` is set outside the scope of any methods, it is a _class
attribute_. All members of the `Human` class have the same `species`, so this
makes more sense than setting the same value for every new human upon
instantation.

An interesting note about class attributes is that they can be
accessed on the class itself, in addition to any instances:

```py
guido = Human("Guido")
guido.species
# Homo sapiens
Human.species
# Homo sapiens
```

Since `name` is an instance attribute, calling it on the `Human` class will
result in an error:

```py
guido = Human("Guido")
guido.name
# Guido
Human.name
# AttributeError: type object 'Human' has no attribute 'name'
```

<details><summary><em>If we enter <code>guido.nationality = "Dutch"</code>
into the interpreter, will <code>nationality</code> be a class or instance
attribute?</em></summary>
<p>

<h3>Instance Attribute</h3>
<p>Because it is assigned to an object, it is an instance attribute.</p>
<p>The <code>Human</code> class remains unchanged.</p>
</details>
<br/>

***

## Setting and Getting Attributes

Many programming languages opt to protect their objects' attributes and
methods (members). They accomplish this by making the distinction between _public_,
_private_, and _protected_. These terms are good to know, as you will almost
certainly encounter them in your software career:

- _Public_ members are available to anyone that can access the class.
- _Private_ members are available to the class that instantiated them.
- _Protected_ members are available to the class that instantiated them and any
object that inherits from that class, but is not accessible otherwise.

Python does not make the distinction between public, private, and protected.
This makes it very easy for us to manipulate the members of a class or object
with dot notation:

```py
class Human:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name

guido = Human("Guido")
guido.species
# Homo sapiens
guido.name
# Guido

# Changing species and name using dot notation
guido.species = "Python programmer"
guido.name = "Guido van Rossum"

guido.species
# Python programmer
guido.name
# Guido van Rossum

# Adding new attributes using dot notation
guido.nationality = "Dutch"
guido.nationality
# Dutch
```

**Because it is so simple to modify the attributes of classes and objects in
Python, it is very rare that we write extra code to get or set attributes.**

Python also provides us a few built-in functions to manipulate attributes:

- `getattr()` retrieves the value of an attribute.
- `setattr()` changes the value of an attribute, just as you would with dot
notation.
- `hasattr()` checks for the presence of an attribute.
- `delattr()` removes an attribute from a class or object.

You might be wondering at this point why `getattr()` and `setattr()` even exist
when dot notation can be used to accomplish the same tasks:

```py
# Getting
guido.name
# Guido van Rossum
getattr(guido, "name")
# Guido van Rossum

#Setting
guido.nationality = "Dutch"
setattr(guido, "nationality", "Dutch")
```

The value in Python's `attr()` functions comes in their ability to create,
retrieve, update, and delete attributes for which the names are unknown.

> NOTE: `getattr()` also allows us to provide an optional third argument as a
> default value if the attribute does not exist.

```py
my_attr = "is_a_friend"
getattr(guido, my_attr, False)
# False

# Oh no! Let's try again.
setattr(guido, my_attr, True)
getattr(guido, my_attr, False)
# True
```

## Instructions

Fork and clone the lab and run the tests with `pytest -x`.

### 1. `Person.__init__` with a Name

Define a `Person` class in `lib/person.py`. In the class, define an
`__init__` method that accepts an argument for the person's name. That
argument should be stored within a `self.name` attribute.

### 2. `Dog.__init__` with Name and Breed defaulting to "Mutt"

Define a `Dog` class in `lib/dog.py`. In the class, define an `__init__`
method that accepts an argument for the dog's name. That argument should be
stored within a `self.name` attribute.

Additionally, `Dog.__init__` should accept a second _optional_ argument for
the dog's breed stored in an attribute `self.breed`. When no breed is provided,
it should default to "Mutt".

***

## Conclusion

In Python, when we use `self` keyword in an **instance method**, `self` refers
to whatever instance that method was called on. It's like a special variable
that changes meaning depending on the context. Using `self` in conjunction with
`__init__` allows us to create objects and set their most important attributes
in one line of code. This also ensures that any objects of one class always
contain the data that they need to be useful later on.

This concept of our objects being self-aware is key to our ability to write
object-oriented code. It may take some time to familiarize yourself with this
concept, and that's ok! Just make sure to test out your code, and find ways to
determine what `self` is (like using `ipdb.set_trace()`) if you're ever not
sure.

***

## Resources

- [__init__ in Python](https://www.geeksforgeeks.org/__init__-in-python/)
- [Python self](https://www.w3schools.com/python/gloss_python_self.asp)
- [What do __init__ and self do in Python?](https://stackoverflow.com/questions/625083/what-do-init-and-self-do-in-python)
