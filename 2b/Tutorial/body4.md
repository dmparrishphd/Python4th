## Numbers

Enter `1 #` ` ` ` ` ` ` `spam =`.

(Ariadne erases\
the _extra_ spaces,\
but including more cases\
in all the right places\
makes you the winner of code-reading races.)


    S>> '' '' '' ''
    OK>> 1 #   spam =
    S>> '' '' '' ''
    
Enter `spam`.

    S>> '' '' '' ''
    OK> spam
    S>> '' '' '' 1
    
Note that the `1` on the top of the Stack is not quoted.
This symbol representd the integer (Python 3 `int`) value 1, not the string `'1'`.

Input comes to Ariadne as Python 3 strings (`str`).
Ariadne uses strings as the fundamental type
(see also "Why Stings Are the Correct Fundamental Data Type" [forthcoming]).
**Ariadne does not waste time guessing what a string means.**
If you want the string `'1'` to mean the integer `1`, say so.

Many programming languages (e.g., Python) use THE NUMBER SIGN (`#`) to indicate that the remaining text on a line of text should be _ignored_.
**Ariadne uses the number sign to indicate a number.**
(More specifically, `#` converts the string on the top of the Stack into an integer \[Python 3 `int`\].)

I hope you find Ariadne's definition of `#` neither confusing nor inconsistent.
