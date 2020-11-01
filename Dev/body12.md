# Kings [2]

The extraction and slicing words work for lists, too:

    OK> CLEAR [] Saul , David , Solomon ,
    S>> '' '' '' ['Saul', 'David', 'Solomon']
    OK> 2 # :]
    S>> '' '' '' ['Solomon']
    OK> RECALL
    S>> '' '' ['Solomon'] ['Saul', 'David', 'Solomon']
    OK> 2 # [:
    S>> '' '' ['Solomon'] ['Saul', 'David']
    OK> RECALL
    S>> '' ['Solomon'] ['Saul', 'David'] ['Saul', 'David', 'Solomon']
    OK> 2 # ]
    S>> '' ['Solomon'] ['Saul', 'David'] 'Solomon'
    
Lists can be concatenated (Note that `CALL` is quoted.
This is necessary because `CALL` is a defined word):

    OK> CLEAR
    S>> '' '' '' ''
    OK> [] BETTER ,
    S>> '' '' '' ['BETTER']
    OK> [] 'CALL ' ,
    S>> '' '' ['BETTER'] ['CALL']
    OK> [] SAUL ,
    S>> '' ['BETTER'] ['CALL'] ['SAUL']
    OK> +
    S>> '' '' ['BETTER'] ['CALL', 'SAUL']
    OK> +
    S>> '' '' '' ['BETTER', 'CALL', 'SAUL']

Items of lists can be altered using the `]=` word (a ternary operator):

    S>>'' '' '' ['BETTER', 'CALL', 'SAUL']
    OK> 2 #    DAVID    ]=
    S>>'' '' '' ['BETTER', 'CALL', 'DAVID']
    
Place the length of a list on the Stack:

    S>>'' '' '' ['BETTER', 'CALL', 'DAVID']
    OK> len
    S>>'' '' '' 3
    
Reminder / Note: most words consume their arguments, as does `len`.

Ariadne can nest lists:

    OK> CLEAR
    S>> '' '' '' ''
    OK> [] ANA ,
    S>> '' '' '' ['ANA']
    OK> [] MARY ,
    S>> '' '' ['ANA'] ['MARY']
    OK> [] JESUS ,
    S>> '' ['ANA'] ['MARY'] ['JESUS']
    OK> ,
    S>> '' '' ['ANA'] ['MARY', ['JESUS']]
    OK> ,
    S>> '' '' '' ['ANA', ['MARY', ['JESUS']]]
    
