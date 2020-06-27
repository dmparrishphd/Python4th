# Ruth (cont'd)

## End of the Line

You can use `LF` ("line feed") to tell Ariadne to place a newline character on the Stack.
You can use in combination with other input to form multi-line strings:

    S>> '' '' '' ''
    OK> First\ line.
    S>> '' '' '' 'First line.'
    OK> LF
    S>> '' '' 'First line.' '\n'
    OK> Second\ line.
    S>> '' 'First line.' '\n' 'Second line.'
    OK> + +
    S>> '' '' '' 'First line.\nSecond line.'
    OK> s =
    S>> '' '' '' ''
    OK> s ?
    First line.
    Second line.
    S>> '' '' '' ''
    
 ## Setting a Path
 
 Because of the way Ariadne sees text, you don't need to use sepecial work-arounds to specify any graphic character, including `\`:
 
    OK> C:\some\name ?
    C:\some\name
    
 There are a number of ways to specify non-graphic chaarcters:
 
    S>> '' '' '' ''
    OK> BLANK
    S>> '' '' '' ' '
    OK> LF
    S>> '' '' ' ' '\n'
    OK> 9 # chr
    S>> '' ' ' '\n' '\t'
    OK> TAB
    S>> ' ' '\n' '\t' '\t'
    OK> TABS TAB +   TABS +   TAB +   TABS +    TAB +   TABS +
    S>> '\n' '\t' '\t' 'TABS\tTABS\tTABS\tTABS'
    OK> ?
    TABS    TABS    TABS    TABS
    
Ariadne does not control the amount of space output when a tab character is printed.
