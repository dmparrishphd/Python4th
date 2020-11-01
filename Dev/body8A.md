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
    
 There are a number of ways to specify non-graphic charcters:
 
    S>> '' '' '' ''
    OK> BL
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
    
_Ariadne does not control the amount of space output when a tab character is printed._
That task is left to the environment in which Ariadne (and the underlying Python 3) are running.

## line upon line, line upon line

The word `!:---` reads the "remainder" of the current intput file (could be `stdin`---standard input---often from the keyboard).

On many systems, when entering text from the keyboard,
the end of input may be indicatd by a special key combination, such as `CTRL` + `Z` `ENTER`
(Hold down the Control key, press the Z key, release, and press the Enter key)
or `CTRL` + `D`.
You may see the text `^Z` appear when you presse that sequence of keys.
In the example below, the user does not type `^Z`, but `CTRL` + `Z` `ENTER`.
Your system may require different keystrokes to indicate end-of-file.

    S>> '' '' ''
    OK> '''
    "What about the R-O-U-Ses?"
    "Rodents of Unusual Size?
    "I don't think they exist."
    ^Z
    S>> '' '' '' '"What about the R-O-U-Ses?"\n"Rodents of Unusual Size?\n"I don\'t think they exist."\n'
    OK> ?
    "What about the R-O-U-Ses?"
    "Rodents of Unusual Size?
    "I don't think they exist."

    S>> '' '' ''

\[[TPB](./References.md#TPB)\]

`!:---` is _intended_ to read from whatever is the current file, but it has been tested for `stdin` (keyboard) only.
Beware of this if you use `!:---` in a file to be loaded by Ariadne.

([continue](./body8B.md))
