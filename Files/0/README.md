# Python4th

Forth, written in Python 3. Goals: low barrier to entry, extreme simplicity.

## Initial Release: Ariadne

### To Run

Launch Python 3 from the directory containing 4.py and goforth.py.

Enter `exec(open('goforth.py').read())`

### Known Issues

The argument order an/or order of returned items might be backwards in some cases.

The emulation of the computer network is incomplete.

It is easy to crash. (On crash, will kick you out into familar Python 3 prompt; CTRL+C should have same effect).

## Next Release

Should be more forgiving.

Will likely be incompatible in some important ways.
