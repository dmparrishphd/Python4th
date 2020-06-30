# Judges

What to do when your code fails? How do you judge the cause?

Earlier, you saw how to execute words one at a time.
Similarly, Ariadne allows you to step through the execution of your code one word at a time.
You will need to do this in Python 3.
If Ariadne has not already crashed and kicked you out to Python 3, you can use `ZZ` to stop Ariadne's _automatic_ operation.

    OK> ZZ
    >>>
   
From the Python 3 prompt, you can some utilities that facilitate working with Ariadne more directly.
Many of these utilities are in the `py` dictionary.

Suppse the coppy of Ariadne you want to work with is caled `a`.
You can view the Stack with

    >>> a['s']
    {'TOP': [''], 'SUB': [''], 'REST': ['']}
    >>>
    
and the Return Stack with
    
    >>> a['r']
    {'TOP': [1], 'SUB': [('QUERY',)], 'REST': []}
    >>>
    
You can drop one item from the Stack with

    >>> a['py']['drop'](a)
    
You can drop one process from the Return Stack with

    >>> a['py']['rdrop'](a)
    
If that is too much typing for you, feel free to define some functions of your own, or even modify Ariadne by adding `a['drop']` or something.

You can continue sailing with Ariadne with:

    >>> a['sail'](a)

## Heal Ariadne while She Sleeps

While Ariadne is asleep, you can whisper in her ear what she should do when she wakes up.
Perhaps there is a word called `'''` that she should interpret:

    >>> a['py']['rpush'](a, ("'''",))
    >>> a['r']
    {'TOP': [1], 'SUB': [("'''",)], 'REST': [(('QUERY',), 0)]}
    >>>

([continue](https://github.com/dmparrishphd/Python4th/edit/master/2b/Tutorial/body8.md))
