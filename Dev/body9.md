# Samuel [1]

You can ask Ariadne for a substring of length 1 with `]`:

    OK> Python word =
    S>> '' '' ''
    OK> word
    S>> '' '' '' 'Python'
    OK> word 0 # ]
    S>> '' '' 'Python' 'P'
    OK> word 5 # ]
    S>> '' 'Python' 'P' 'n'
    OK> word -1 # ]
    S>> 'Python' 'P' 'n' 'n'
    OK> word -2 # ]
    S>> 'P' 'n' 'n' 'o'
    OK> word -6 # ]
    S>> 'n' 'n' 'o' 'P'
    OK>
    
I may seem like extra work to use `#` at this point.
However, I think it is unusual to use "hard coded" numbers or "magic numbers" for indexing.
Usually, the index is computed.
The special cases of wanting the first and second elments come up a lot.
But for those cases, it may be better to use special words.
Ariadne defines `FIRST`, `SECOND`, and `LAST`:

> `1 # ONE =`

> `0 # ZERO =`

> `ZERO\ ] FIRST :;`

> `ONE\ ] SECOND :;`

> `-1\ #\ ] LAST :;`
    
You might use them like this:
    
    S>> 'n' 'n' 'o' 'P'
    OK> word FIRST
    S>> 'n' 'o' 'P' 'P'
    OK> word SECOND
    S>> 'o' 'P' 'P' 'y'
    OK> word LAST
    S>> 'n' 'o' 'P' 'n'
    
