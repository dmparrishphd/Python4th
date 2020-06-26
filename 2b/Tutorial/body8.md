# Ruth

"Ruth" is a name.
Ariadne does not define `Ruth`.
If you enter `Ruth`, the string `'Ruth'` will be placed on the stack:

    OK> Ruth
    S>> '' '' '' 'Ruth'
    
What if you want to place the name of a defined word on the Stack?
How 'bout `DROP`?

    S>> '' '' '' 'Ruth'
    OK> DROP
    S>> '' '' '' ''
    
Oops!
Since `DROP` is defined, Ariadne applied the definition of `DROP`, which is to drop the top item from the Stack.
Let's try again.
Hint: Ariadne defines exactly one word that begins with the accent grave, `` ` ``, +(a.k.a, backquote), `` ` ``; that is, Ariadne defines the word `` ` ``.

    S>> '' '' '' ''
    OK> Ruth
    S>> '' '' '' 'Ruth'
    OK> `DROP
    S>> '' '' 'Ruth' '`DROP'
    
Except for `` ` ``, Ariadne will place any word containing `` ` `` on the Stack.

But we wanted `DROP` on the Stack, not ```DROP``. You can use `REST` to replace the object on the top of Stack with the _rest_ of the object.
That is, all but the first item.

    S>> '' '' 'Ruth' '`DROP'
    OK> REST
    S>> '' '' 'Ruth' 'DROP'
    
    
