## Numbers

Enter

    1 #   spam =
    
> (Ariadne erases\
> the _extra_ spaces,\
> but including more cases\
> in all the right places\
> makes you the winner of code-reading races.)

    S>> '' '' '' ''
    OK>> 1 #   spam =
    S>> '' '' '' ''
    
Enter `spam`.

    S>> '' '' '' ''
    OK> spam
    S>> '' '' '' 1
    
Note that the `1` on the top of the Stack is not quoted.
This symbol represents the integer (Python 3 `int`) value 1, _not_ the string `'1'`.

Input comes to Ariadne as Python 3 strings (`str`).
Ariadne uses strings as the fundamental type
(see also "Why Strings Are the Correct Fundamental Data Type" [forthcoming]).
**Ariadne does not waste time guessing what a string means.**
If you want the string `'1'` to mean the integer `1`, say so.

Many programming languages (e.g., Python) use the _number sign_ (`#`) to indicate that the remaining text on a line of text should be _ignored_.
**Ariadne uses the number sign to indicate a number.**
(More specifically, `#` converts the string on the top of the Stack into an integer \[Python 3 `int`\].)

I hope you find Ariadne's definition of `#` to be both coherent and consistent.

## Using the \#f Word: Arithmetic

Ariadne has `#f` word in case you really need to use floating point values:

    S>> '' ''
    OK> 3.14 #f
    S>> '' '' 3.14

Python 3 has an elaborate [operator precedence scheme](https://docs.python.org/3/reference/expressions.html) in which the operators (e.g., `+`, `-`) are organized into 18 (**eighteen**) different ranks in order to decide which operation to perform in what order.

Forth simply performs the operations in the order encountered.


    S>> '' ''
    OK> 4 #
    S>> '' '' 4
    OK> 3.75 #f
    S>> '' '' 4 3.75
    OK> *
    S>> '' '' 15.0
    OK> 1 #
    S>> '' '' 15.0 1
    OK> -
    S>> '' '' 14.0
    OK>

Python 3 has a special variable, `_`, that stores the most recent printed expression.
That feature can be nice when [using Python 3 like a calculator](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator).
Ariadne stores the result of arithmetic operations on the top of the Stack.
For this reason, and because the top four elements of the Stack are printed just before the OK prompt, no such special variable is necessary.



([continue](https://github.com/dmparrishphd/Python4th/blob/master/2b/Tutorial/body5.md))
