# Samuel [2]

## Slicing

_Slicing_ refers to the extraction of multiple elements, often contiguous elements.

The words `[:` and `:]` can be used to extract multiple elements:

    OK> Samuel
    S>>'' '' '' 'Samuel'
    OK> 4 # :]
    S>>'' '' '' 'el'
    OK> Samuel
    S>>'' '' 'el' 'Samuel'
    OK> 3 # [:
    S>>'' '' 'el' 'Sam'

`[:` extracts from the beginning _up to_, but _excluding_ the index given
(Ariadne, like Python 3, indexes from zero) and
`:]` extracts from the index given to the end.

You could also think of `[:` as "left" and `:]` as "right".
Mnemonic: the position of the bracket (`[` or `]`) relative to the colon (`:`).

    >> '' '' '' ''
    OK> Samuel
    S>> '' '' '' 'Samuel'
    OK> DUP
    S>> '' '' 'Samuel' 'Samuel'
    OK> 3 # [:
    S>> '' '' 'Samuel' 'Sam'
    OK> SWAP
    S>> '' '' 'Sam' 'Samuel'
    OK> 3 # :]
    S>> '' '' 'Sam' 'uel'
 
`[:]` extracts a range of elements:

    OK> CLEAR
    S>>'' '' '' ''
    OK> Samuel
    S>>'' '' '' 'Samuel'
    OK> 2 # 4 #
    S>>'' 'Samuel' 2 4
    OK> [:]
    S>>'' '' '' 'mu'
    OK>

You can think of `[:]` as "middle".
Mnemonic: The position of the colon (`:`) is in the middle of the brackets (`[]`).

## The Fix

If you are accustomed to "infix languages" (like Python 3),
which place operators _between_ the arguments insteadof _after_ them,
you might use this mnemonic to help you remember how _postfix_
languages, like Ariadne, do it:

| Infix Language  | Postfix Language |
| :-------------: | :--------------: |
| `'Samuel' [: i` | `'Samuel' i [:`  |

The operator "hops over" the second argument.

Similarly:

| Infix Language       | Postfix Language   |
| :------------------: | :----------------: |
| `'Samuel' [ i : j ]` | `'Samuel' i j [:]` |

`[:]` is a _ternary_ operator (taking three arguments).
One mnemonic is to imagine that the characters making up the word are
either interlaced among the arguments or gathered together after the arguments,
depending upond which perspective you have in mind as a reference point.

Note that Python 3 requires three distinct symbols and a special,
complex interpretation to accomplish slicing a specified range,
Ariadne requires only one symbol and can (and does) apply consistent interpretation
(words separated by whitespace, words applied in the order encountered).
