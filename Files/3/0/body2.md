## Exodus: Getting Ariadne to put out

> **put out** verb
> **put out**; **putting out**; **puts out**
>
> _transitive verb_
> * exert, use put out considerable effort
> * publish, issue
>
> _intransitive verb_
> * to set out from shore \[as in sailing\]
> * to make an effort
> ([Webster's](https://www.merriam-webster.com/dictionary/put%20out) (2020-06-21); formatting altered)

    S>> '' '' '' ''
    OK>

Enter the text `Be\ careful\ not\ to\ fall\ off!` Mind the `\`'s---_backslash_, not `/` (slash).

    S>> '' '' '' ''
    OK> Be\ careful\ not\ to\ fall\ off!
    
Ariadne separates words by whitespace. Whitespace includes:

* spaces,
* end-of-line markers,
* tabs,
* etc.

**However**:
The sequence `\` followed by any amount of whitespace is considered a single, _graphic space_, **not** whitespace.

    OK> Be\ careful\ not\ to\ fall\ off!
    S>> '' '' '' 'Be careful not to fall off!'
    OK>
    
Enter the text `FLAT-WORLD-WARNING =`

    S>> '' '' '' 'Be careful not to fall off!'
    OK> FLAT-WORLD-WARNING =
    S>> '' '' '' ''
    OK>

Enter the text `the_world_is_flat\ IF\ FLAT-WORLD-WARNING\ ?` (Be mindful of the `\`).
Then `FLAT-WORLD-WARN-MAYBE`.
Then `:;`

    OK> the_world_is_flat\ IF\ FLAT-WORLD-WARNING\ ?
    S>> '' '' '' 'the_world_is_flat IF FLAT-WORLD-WARNING ?'
    OK>> FLAT-WORLD-WARN-MAYBE
    S>> '' '' 'the_world_is_flat IF FLAT-WORLD-WARNING ?' 'FLAT-WORLD-WARN-MAYBE'
    OK>> :;
    S>> '' '' '' ''
   
**On boot, Ariadne does have any words defined which contain spaces.**
This means that any word you enter that contains a space will not have a definition.
When you entered `the_world_is_flat\ IF\ FLAT-WORLD-WARNING\ ?`,
Ariadne simply placed the string on the Stack.

Before you entered `:;`, `FLAT-WORLD-WARN-MAYBE` was undefined.
So it, too, goes onto the Stack.

The word `:;` takes the top element of the Stack and begins a new definition of that word.
Then, `:;` splits the second element by whitespace and assigns the resulting sequence of words as the definition of the new word.

Enter the text `FLAT-WORLD-WARN-MAYBE`.

    OK>> FLAT-WORLD-WARN-MAYBE
    Be careful not to fall off!
    OK>
    
Ariadne puts out (issues) a warning, because, apparently, `the_world_is_flat`. If you say so.

([continue](./body3.md))
