# Python 4th (Python Forth)

Forth, written in Python 3

## Hello, World!

In Python 4th, the
["Hello, World" program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)
can be written in _two_ words:

    Hello,\ World!   ?
 
No, I did not count wrong.
`Hello,\ World!` is _one_ word;
[here's](./Doc/Why/whyWords.MD#the-forth-way)
why.

## Goals

> Let's say that we \[programmers\] did pick \[a _single_, common\] language
> \[Chemistry, Physics, and Biology all have common languages\].
> What would that language look like?...
> \[Some popular languages are\] syntax-heavy.
> Learning all that syntax is just horrible....
> **[One] thing we want** out of our languages is **simplicity... of syntax**.
> Think of a language like **Forth**. ---Robert "Uncle Bob" Martin (2020-03-31)
> "The Last Programming Language." Clean Coders.
> https://www.youtube.com/watch?v=P2yr-3F6PQo&t=38m2s

The goals of Python Forth include:

- actual freedom,
- low barrier to entry,
- extreme simplicity

## Why?

[Why](.Doc/Why/why.MD) write Forth in Python 3?

## Releases

### Current Release

[Ariadne III](./Files/4/0)

### Earlier Releases

[Ariadne IIb](./Files/2/0) for July "Forth" 2020.

Ariadne IIa [(Pre-release)](./Files/1/0) of July "Forth" 2020 edition; accompanies
["Why can't Python deepcopy stdin?"](https://stackoverflow.com/questions/62373655/why-cant-python-deepcopy-stdin)

### To Run

See the example at the top of the source code.

### Known Issues

Ariadne IIa is barely tested. The basic operations like `DUP`, `DROP`, and `OVER` seem to work, as do the two compilers (`:;` and the tripple `:`, \`, `;`).

A lot of essential features are yet to be incorporated (one development goal was to get the compiler working as soon as possible).

## Acknowledgements

I draw inspiration chiefly from
[Charles H. "Chuck" Moore](https://www.youtube.com/watch?v=tb0_V7Tc5MU)
(Forth's inventor), Leo Brodie (author of
[Thinking Forth](http://thinking-forth.sourceforge.net/)
and other texts), and Charles-Hanson Ting
(creator of several Forth implementations and author of
[eForth and Zen](https://www.amazon.com/eForth-Zen-32-bit-86eForth-Visual-ebook/dp/B06VXR1TX3/)
and other texts).
