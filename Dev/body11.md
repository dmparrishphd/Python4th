# Kings [1]

To place an empty list on the top of the stack, use the `[]` word:

    OK> CLEAR
    S>> '' '' '' ''
    OK> []
    S>> '' '' '' []
    
To add elements to the list, use the `,` word:

    OK> Saul
    S>> '' '' [] 'Saul'
    OK> ,
    S>> '' '' '' ['Saul']
    OK> David
    S>> '' '' ['Saul'] 'David'
    OK> ,
    S>> '' '' '' ['Saul', 'David']
    OK> Solomon ,
    S>> '' '' '' ['Saul', 'David', 'Solomon']
    
OR:

    OK> CLEAR [] Saul , David , Solomon ,
    S>> '' '' '' ['Saul', 'David', 'Solomon']
    
If you are accustomed to infix languages,
it may seem like there is an "extra" `,` at the end,
but this is not so. The meaning of `,` is,
"drop the item on top of the Stack and append it to the second item on the Stack."
The `,` word---like all words Ariadne knows---has power in and of itself;
it is not a second-class, silent punctuation mark, but a first class **word** that "speaks" for itself.

([continue](./body12.md))
