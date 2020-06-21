## Genesis

In the beginning, Ariadne boots, and you will see something like the following on the last two lines of the console:

    S>> '' '' '' ''
    OK>

Ariadne is displaying the top four elments of the stack after the `S>>`.
Their representation is determined by Python 3.
In the above examaple, there are four null strings (`str`) on the top of the Data Stack (or "the Stack").
The more recent items on the Stack are displayed further to the _right_.

Because Ariadne interprets words in the order received, and
because whitespace separates words,
this means you can very often execute words one at a time so as to beter understand Ariadne's behavior.

Enter _the text_ `True` and Ariadne will do what _the word_ `True` means: place _the Python 3 `True` object on the Stack.
    
    OK> True
    S>> '' '' '' True
    OK>
    
Enter _the text_ `the_world_is_flat`.

    OK> the_world_is_flat
    S>> '' '' True 'the_world_is_flat'
    OK>
    
The _word_ `the_world_is_flat` is not yet defined.
**Ariadne places undefined words on the Stack.**

Enter _the text_ `=`.

    S>> '' '' True 'the_world_is_flat'
    OK> =
    S>> '' '' '' ''
    OK>
    
The top 2 items on the Stack are gone!
`=` takes the top two elements from the Stack and creates a new word from them.

The top item becomes the new word.
The second item becomes the value to place on the Stack when the new word is invoked:

    S>> '' '' '' ''
    OK> the_world_is_flat
    S>> '' '' '' True
    OK>
    
([continue](https://github.com/dmparrishphd/Python4th/edit/master/2b/Tutorial/body2.md))
