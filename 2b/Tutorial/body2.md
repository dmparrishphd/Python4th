    S>> '' '' '' ''
    OK>

Enter the text `Be\ careful\ not\ to\ fall\ off!`

    S>> '' '' '' ''
    OK> Be\ careful\ not\ to\ fall\ off!
    
Ariadne separates words by whitespace.
Whitespace includes spaces, end-of-line markers, tabs, etc.
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
   
**Ariadne does not define any words containing spaces.**
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
