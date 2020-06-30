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

But we wanted `DROP` on the Stack, not `` `DROP ``. You can use `REST` to replace the object on the top of Stack with the _rest_ of the object.
That is, all but the first item.

    S>> '' '' 'Ruth' '`DROP'
    OK> REST
    S>> '' '' 'Ruth' 'DROP'
    
    
## Quotes? Where We're Going, We Don't Need Quotes

Ariadne read entire words at a time, not individual characters.
Words are separated by whitespace.
The sequence `\` followed by whitespace counts as a _graphic space_, not whitespace.

What this means is that you don't _need_ quotes.
But you can use them if you _want_ to have quotes your strings:

    S>> '' '' '' ''
    OK> spam\ eggs
    S>> '' '' '' 'spam eggs'
    OK> doesn't
    S>> '' '' 'spam eggs' "doesn't"
    OK> "Yes,"\ they\ said.
    S>> '' 'spam eggs' "doesn't" '"Yes," they said.'
    OK> "Isn't"\ they\ said.
    S>> "doesn't" '"Yes," they said.' '"Isn\'t" they' 'said.'
    
You can use `?` to drop the top item of the Stack and print it:

    S>> 'spam eggs' "doesn't" '"Yes," they said.' '"Isn\'t," they said.'
    OK> ?
    "Isn't," they said.
    S>> '' 'spam eggs' "doesn't" '"Yes," they said.'
    OK> ?
    "Yes," they said.
    S>> '' '' 'spam eggs' "doesn't"
    OK> ?
    doesn't
    S>> '' '' '' 'spam eggs'
    OK> ?
    spam eggs
    S>> '' '' '' ''
    OK>
   
([continue](https://github.com/dmparrishphd/Python4th/blob/master/2b/Tutorial/body8A.md))
