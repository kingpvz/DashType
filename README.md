# DashType
Another scripting language of mine made in python. I don't know why.

## Instalation
Download `dashtype.py` to use it.  
You can also download `test.dash` for an example program.

## Documentation
### 1. Files
To create a file, simply name it `<name>.dash`.  
To open a file, run `dashtype.py` and type the `<name>` when asked.

### 2. Syntax
### 2.1. Comments
You can comment code by placing a semicolon (`;`) at the beginning of a line.

### 2.2. Variables
Variables in DashType are a single letter (a-z, A-Z, _ and $) and can only store numerical values.  
You can declare a variable like this: `a<<7` - variable `a` has the value `7`.  
You can also assign an expression to a variable: `a<<5/2` - variable `a` stores the value `2.5`.

### 2.3. Output
You can output values using `<<` at the beginning of the line.  
You can output various types of data:
- `<<a`: Output the value of the variable `a`
- `<<a*2`: Output the result of the expression `a*2`
- `<<?Hello, world!`: Output the string `Hello, World!`
- `<<;`: Print a new line.
- `<<a*2;`: Output the result of `a*2` and begin a new line.
  
Example:
```
a<<5
<<?A=
<<a;
<<?end.

; A=5
; end.
```

### 3. Math
Supported math operands:
- `+` Addition
- `-` Subtraction
- `/` Division
- `*` Multiplication
- `()` Parenthesis
- `^` Exponetiation

### 4. Example program
```
a<<2
b<<3
c<<2^3
<<?a^b=
<<c;
<<?Good night.

; 2^3=8
; Good night.
```
