# Python 4th (Python Forth)

Forth, written in Python 3

## Goals

- low barrier to entry,
- extreme simplicity,
- actual freedom

## Why?

[Why](https://github.com/dmparrishphd/Python4th/blob/master/Doc/Why/why.MD) write Forth in Python 3?

## Ariadne IIa

[Pre-release](https://github.com/dmparrishphd/Python4th/tree/master/2a) of July "Forth" 2020 edition.

Accompanies ["Why can't Python deepcopy stdin?"](https://stackoverflow.com/questions/62373655/why-cant-python-deepcopy-stdin)

### To Run

See the example at the top of the [source code](https://github.com/dmparrishphd/Python4th/blob/master/2a/ariadne2a.py).

### Known Issues

Ariadne IIa is barely tested. The basic operations like `DUP`, `DROP`, and `OVER` seem to work, as do the two compilers (`:;` and the tripple `:`, \`, `;`).

A lot of essential features are yet to be incorporated (one development goal was to get the compiler working as soon as possible).

## Next Release

Ariadne II (without the "a") should have a more complete set of features, and should be more thoroughly tested.

## Acknowledgements

I draw inspiration chiefly from [Charles H. "Chuck" Moore](https://www.youtube.com/watch?v=tb0_V7Tc5MU) (Forth's inventor), Leo Brodie (author of [Thinking Forth](http://thinking-forth.sourceforge.net/) and other texts), and Charles-Hanson Ting (creator of several Forth implementations and author of [eForth and Zen](https://www.amazon.com/eForth-Zen-32-bit-86eForth-Visual-ebook/dp/B06VXR1TX3/) and other texts).
