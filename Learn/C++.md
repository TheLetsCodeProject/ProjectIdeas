# Understanding C++
***
C++ (See-Plus-Plus) is one of the most common programming languages in use. It is used in everything from hobbyist electronics to full scale video games (Fortnite or Call of Duty are examples). The only issue with C++ is that it can be a little confronting to new learners. Here I will try and break down the core concepts of programming and try to aid in your understanding of this language.

## Variables
Ok so the first step in pretty much every programming tutorial is the demonstration of variables. Variables are simply a way for us to store data so that we can use it later. Let's write a variable to store our age.
```C++
int age = 16;
```
Woah! Thats not the most obvious thing in the world. Lets break it down a little bit.

This code is whats known as a 'variable declaration', it has three main parts.
1. The first part is the 'data type'. This is a way for us to tell the computer what kind of information we want to store. In the above example, our data type is 'int' which is short for integer, a whole number. There are many data types but we will come back to those later.
2. The name of our variable. In the above example we have named our variable 'age'. The name of a varibale may not start with a number but can contain them after the first letter: `m10` is allowed but a name like `10m` is not.
3. The assignment. This is where we give our value. In the above example we set our value to 16.

You may have nooticed the ';' at the end of the line. This is our line terminator and is the coding example of a full stop. We have to put this at the end of every line unless the line finishes with `{ or }`.

With that said, lets declare a variable for how much water can be stored in a bottle.
```C++
float capacity = 2.5;
```
'float' is a data type which allows us to store decimals instead of integers, You can store whole numbers in floats but you cannot store decimals in ints.

### Reassignment
Once we have declared a variable, we are then able to modify its value. To do this we simply write the name of the variable we wish to change followed by an equals sign and our new value:
```C++
int age = 13;
age = 16; // Age is now equal to 16
```
It is important to note that you can only set a varible to another value of its data type; We cannot assign a float to an int:
```C++
int age = 16;
age = 16.6;
// This code would throw an error as we are trying to assign a decimal (float) to a whole number (int)
```
## Math
C++ supports all normal mathematical operations.
- Additoon: **+**
- Subtraction: **-**
- Multiplication: **\***
- Division: **/**
We can use them in assignments like the following:
```C++
int number = 1;
int newNumber = number + 1;
```
Like assignments, maths can only happen between two similar data types.
