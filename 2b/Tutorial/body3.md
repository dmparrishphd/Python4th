## Leviticus: Some Rules for the Ariadne Priesthood

### IF

If you use `IF` outside a defninition, you will likely corrupt Ariadne's Stack and **Return Stack**.
The Return Stack tells Ariadne what to do next.

`IF`'s operation is as follows:

1. The top element of the Stack is removed.
2. If that item is equivalent to `False` (or if it is not equivalent to `True`):
    1. The present operation (`IF` itself) is canceled and
    2. The following operation (the definition in which `IF` occurs) is also canceled.
3. Otherwise, processing continues with the next word after `IF`.
  
 ### Then
 
 The following patterns might be useful:
 
 #### Pattern 1
 
     IF\ _NEW-WORD   NEW-WORD :;
     
 In other words, define `_NEW-WORD` to be what should happen if the top element of the Stack is equivalent to `True`.
 And define `NEW-WORD` with the `IF` in front.
 (I like to use an underscore \[_\] prefix to mean "helper function."
 This is not a requirement of Ariadne, just a discipline I find useful.)
 
 #### Pattern 2
 
     DUP\ IF\ _NEW-WORD   NEW-WORD :;
     
 This is the same as Pattern 1, except that the top element of the Stack is first duplicated.
 This pattern is useful when `_NEW-WORD` needs to know what was on top of the Stack before `IF` was processed.
 
 ### Next
 
 ([continue](https://github.com/dmparrishphd/Python4th/blob/master/2b/Tutorial/body4.md))
