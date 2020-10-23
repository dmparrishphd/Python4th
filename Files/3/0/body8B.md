# Ruth (cont')

## Say Again

The `+` and `*` operators accomplish string concatenation and repetition ([TPB]()):

    S>> '' '' ''
    OK> "Do\ you\ promise\ not\ to\ hurt\ him?" LF +   "What\ was\ that?" LF +   2 # *   + ?
    "Do you promise not to hurt him?"
    "What was that?"
    "What was that?"
    
    S>> '' '' ''
  
[Python 3 contatenats addjacent strings](https://docs.python.org/3/tutorial/introduction.html#strings):

    >>> 'Py' 'thon'
    'Python'
    >>>
  
Ariadne thinks it is silly to use use _five_ symbols (open quote, close quote, space, open quote, close quote) to concatenate strings when _you need only one_:

    S>> '' '' ''
    OK> Ari adne +
    S>> '' '' '' 'Ariadne'
    OK>
  
If you think you need really long string concatenations to program Ariadne, we suggest that you break up your code into smaller phrases and definitions.

([continue](https://github.com/dmparrishphd/Python4th/blob/master/2b/Tutorial/body9.md))
