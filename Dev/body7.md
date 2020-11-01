# Judges

What to do when your code fails? How do you judge the cause?

Earlier, you saw how to execute words one at a time.
Similarly, Ariadne allows you to step through the execution of your code one word at a time.
You will need to do this in Python 3.
If Ariadne has not already crashed and kicked you out to Python 3,
you can use `Z` to put Ariadne to sleep.

    OK> Z
    >>>
   
From the Python 3 prompt, you can some utilities that facilitate working with Ariadne more directly.
Many of these utilities are in the `py` dictionary.

Suppse the coppy of Ariadne you want to work with is caled `a`.
You can view the Stack with

    >>> a['s']
    ['', '', '', '']
    >>>
    
and the Return Stack with
    
    >>> a['r']
    [('QUERY',), 0, ('Z',), 0]
    >>>

Unless something has broken Ariadne's design,
the first item on the Return Stack should be the Python 3 tuple `('QUERY',)`.
The other items on the Return Stack will depend on what Ariadne was doing before she went to sleep.

You can drop one item from the Stack with

    >>> a['py']['drop'](a)
    
You can drop one process from the Return Stack with

    >>> a['py']['_rdrop'](a)
    
If that is too much typing for you, feel free to define some functions of your own, or even modify Ariadne by adding `a['drop']` or something.

You can continue sailing with Ariadne with:

    >>> a['sail'](a)

## Heal Ariadne while She Sleeps

While Ariadne is asleep, you can whisper in her ear what she should do when she wakes up.
Perhaps there is a word called `'''` that she should interpret:

    >>> a['py']['_rpush'](a, ("'''",))
    >>> a['r']
    [('QUERY',), 0, ('Z',), 0, ("'''",), 1]
    >>>

([continue](./body8.md))
