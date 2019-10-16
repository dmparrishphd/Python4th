"""PYTHON FORTH: ARIADNE        COPYRIGHT (C) D. MICHAEL PARRISH























                          PYTHON  4-TH
                         (PYTHON FORTH)


======     +-----+-----+---+-----+----+ ++-+--+-----+     ======
]||||[     |     |     |   |     | . . \| \ \ |     |     ......
======     | ---   ---       ---  . | .           --+     ......
][  ][ . . . . . . . . . . . . . .  |  . . . . . . . . . .......
||  ||     |          \             |             --+     ......
||  ||     |  |  |  |  |   |  |  |     /| \ \ |     |     ......
======     +--+--+--+--+---+--+--+----+ +--+-++-----+     ======
[][][]                                                      ||
[][][]                                                      ||
[][][]                                                      ||
[]  []     A      R      I      A      D      N     E       ||
[]  []                                                      ||
======                                                     ====
 



       G E T   A   C L E W .   G E T   T H R E A D E D .

       G E T   O U T   O F   T H E   L A B Y R I N T H !
#








                          IN MEMORY OF

                  VIRGINIA JOHN BENNET PARRISH

                             + 2009 










#









               THE FUNDAMENTAL UNIT OF COMPUTING
               IS THE ENTIRE COMPUTER.
                                     ---ALAN KAY











"""

# A LOADER
_GO = "_2=open('4.py'); exec(_2.read()); _2.close(); del(_2)"

# A CLEAN-UP TOOL
_RESTORE = '''
for _1 in dir():
    if _1[0] != '_':
        print('4.py: _RESTORE: deleting:', _1)
        exec('del ' + _1)
del _1
'''

from collections import deque
from functools   import partial
from itertools   import chain
from sys         import stderr, stdin, stdout

dbprint = partial(print, 'db>')

def unstar(function):
    def unstarred(arg_tuple, **kwargs):
        return function(*arg_tuple, **kwargs)
    return unstarred

def irange(start, *stop, step=1):
    '''irange is similar to range, except that stop is included
    in the range. **** DESIGNED FOR **** int arguments only.
    '''
    assert isinstance(start, int), 'start is not int'
    assert isinstance(step, int), 'step is not int'
    stop = start if not stop else stop[0]
    assert isinstance(stop, int), 'stop is not int'
    assert start <= stop, 'start > stop'
    return range(start, 1 + stop)



"""TING HAS ReadChar AVAILABLE AS A HARDWARE / OS CALL. THE
FOLLOWING BUILDS A SIMILAR FACILITY FROM Python 3.
ADDITIONALLY, TING HAS THE ASCII CHARACTER SET HARD CODED. THE
FOLLOWING ALLOWS FOR / WILL ALLOW FOR ARBITRARY CHARACTER SETS
(THAT ARE MAPPED TO int-S).

A SIGNIFICANT PORTION OF THE FOLLOWING WAS BUILT UP SO THAT THE
SEQUENCE \ (REVERSE SOLIDUS, SPACE) MAY BE USED TO EMBED SPACES
INTO STRINGS, WHEREAS OTHERWISE ANY NON GRAPHIC CHARACTER,
INCLUDING SPACE, IS CONSIDERED A WORD SEPARATOR.  THE NOTATION
IS ADOPTED FROM TEX (Knuth)."""

def isgraph_py4000(integer):
    '''In hardware, this could be a 2Kb (kiloBITS) ROM chip with
    bit-addressable memory using 11 bits. Operation would be to
    query the bit.
    
    TODO: extend to include mathematical operators.'''
    EXCLUDED = tuple(
        unstar(chain)(map(tuple, map(unstar(irange), (
        (0x00, 0x20),
        (0x7f,),
        (0x80, 0xa0),
        (0xad,),
        (0x034f,),
        (0x0378, 0x0379),
        (0x0380, 0x0383),
        (0x038b,),
        (0x038d,),
        (0x03a2,),
        (0x0530,),
        (0x0557, 0x0558),
        (0x058b, 0x058c),
        (0x0590,),
        (0x05c8, 0x05cf),
        (0x05eb, 0x05ee),
        (0x05f5, 0x05ff),
        (0x061c, 0x061d),
        (0x070e,),
        (0x074b, 0x074c),
        ())[:-1])))) # () ... [:-1] # FOR EASY APPEND
    return integer < 0x0800 and integer not in EXCLUDED

def isgraph_ascii(integer):
    if not isinstance(integer, int):
        return False
    if integer < 33:
        return False
    if integer < 127:
        return True
    return False

class character_set_in:
    '''Defines an input character set. Each integer is mapped to
    either a graphic character, a blank, or nothing. Ting hard
    codes the character set.
    '''
    def __init__(self, isgraph):
        '''isgraph is an integer function that returns whether
        the integer argument is a graphic character.
        '''
        self.isgraph = isgraph

class character_set_internal:
    def __init__(self, isgraph, blank=ord(' ')):
        self.BLANK = blank 
        self.isgraph = isgraph
    def blank(self):
        '''Returns the int representing the cardinal blank.
        '''
        return self.BLANK
    def remap(self, integer):
        '''Returns the integer argument if it is mapped to a
        graphic character. Otherwise returns the integer that is
        mapped to the cardinal blank.
        '''
        return integer if self.isgraph(integer) else self.blank()

def receive(
        character_set_internal_,
        character_set_in_,
        integer_iterator):
    '''NOTE: FIRST TWO ARGS WERE PREVIOUSLY IN OTHER ORDER.
    '''
    for integer in integer_iterator:
        if character_set_in_.isgraph(integer):
            yield integer
        else:
            yield character_set_internal_.blank()

def next_graph(character_set_internal_, integer_iterator):
    return next(
        filter(
            character_set_internal_.isgraph,
            integer_iterator),
        -1)

class queue:
    '''queue can be viewed as a stripped down version of
    collections.deque, **** EXCEPT **** that append and extend
    both return the queue rather than None. Additionally, queue
    has a peek method, where deque has none (perhaps because it
    has __getitem__ and __bool__).
    '''
    from collections import deque
    def __init__(self):
        self.Data = deque()
    def __bool__(self):
        return bool(self.Data)
    def __repr__(self):
        return (
            '<' + ('non-' if self else '') +
            'empty queue object at ' + hex(id(self)) + '>')
    def append(self, item):
        self.Data.append(item)
        return self
    def extend(self, iterable):
        self.Data.extend(iterable)
        return self
    def pop(self):
        return self.Data.popleft()
    def drop(self):
        self.pop()
    def peek(self, default=None):
        '''peek returns the next item in the queue, WITHOUT
        removing it from the queue. However, if the queue is
        empty, returns default.
        '''
        return default if not self else self.Data[0]

class prophet:
    '''Similar to an iterator, but the next few values are kept
    in memory for peeking
    '''
    def _pull(self):
        '''Move the next available item from the iterator to the
        Deque.
        '''
        item = next(self.Iterator, self.DEFAULT)
        if item is self.DEFAULT:
            return
        self.Deque.append(item)
    def __init__(self, iterator, forecast=1, default=None):
        '''forecast should be a small integer: 1 or 2 in most
        cases.
        '''
        try:
            hash(default)
        except:
            assert False, 'default must be hashable'
        assert isinstance(forecast, int), (
            'forecast should be a number of items to advance'
            'the iterator.')
        self.DEFAULT = default
        self.Iterator = iterator
        self.Deque = deque()
        self.N = forecast
        for k in range(self.N):
            self._pull()
    def peek(self, n=None):
        n = self.N if n is None else n
        memo = []
        for k in range(self.N):
            if self.Deque:
                memo.append(self.Deque.popleft())
        for item in reversed(memo):
            self.Deque.appendleft(item)
        return tuple(memo)
    def __repr__(self):
        return 'prophet(' + str(list(self.peek())) + ')'
    def __next__(self, *default):
        default = self.DEFAULT if not default else default
        self._pull()
        return default if not self.Deque else self.Deque.popleft()

def crunch(character_set_internal_, integer_iterator):
    integer = next_graph(character_set_internal_, integer_iterator)
    BLANK = character_set_internal_.blank()
    if integer < 0:
        return
    yield integer
    for integer in integer_iterator:
        if integer is BLANK:
            yield integer
            integer = next_graph(
                character_set_internal_,
                integer_iterator)
            if integer < 0:
                return
            else:
                yield integer
        else:
            yield integer

def interpret(
        character_set_internal_,
        clean_integer_iterator,
        escape=ord('\\')):
    DEFAULT = -1
    p = prophet(
        clean_integer_iterator,
        forecast=2,
        default=DEFAULT)
    characters = []
    while p.peek():
        item = next(p)
        if item is escape:
            if not p.peek():
                break # IGNORE ESCAPE CHARACTER JUST BEFORE EOF
            characters.append(next(p))
        elif item is character_set_internal_.blank():
            if characters: # I.E., DO NOT yield A NULL STRING
                yield tuple(characters)
            characters.clear()
        else:
            characters.append(item)
    if characters:
        yield tuple(characters)

def hex8(n):
    return '{:08X}'.format(n)

def character_chart(start=0, stop=0xff, isgraph=isgraph_py4000):
    '''Used for testing.
    '''
    HEADER = 8 * ' ' + ' '.join(
        map(lambda n: '{:X}'.format(n), range(16)))
    for j in range(start // 16 * 16, stop // 16 + bool(stop % 16)):
        print()
        if not (j % 8):
            print('\n', HEADER)
        print(hex8(16 * j), end='')
        for i in range(0, 16):
            ic = i + 16 * j
            print('', ' ' if not isgraph(ic) else chr(ic), end='')
    print()

def ascodepoints(string):
    return tuple(map(ord, string)) 

def fromcodepoints(integer_iterable):
    return ''.join(map(chr, integer_iterable))

#TODO: REFACTOR FOR PARSING CHARACTERS FROM A FILE
def parse_string(
        character_set_internal_,
        character_set_in,
        string,
        escape=ord('\\')):
    return tuple(map(fromcodepoints, interpret(
        character_set_internal_,
        crunch(
            character_set_internal_,
            receive(
                character_set_internal_,
                character_set_in,
                ascodepoints(string))),
        escape=escape) ) )



# _seq, seq, AND wseq HAVE TO DO WITH READING CHARACTERS AND
# WORDS FROM FILES.

class _seq:
    '''facilitates reading a file in strict sequence.
    '''
    def __init__(self, filename):
        try:
            self.Data = [open(filename)]
        except:
            self.Data = []

class seq(_seq):
    '''for reading through a file one character at a time.
    '''
    def __next__(self):
        '''Conceptually, returns the next character in the
        underlying file.
        '''
        if not self.Data:
            return ''
        c = self.Data[0].read(1)
        if c:
            return c
        else:
            self.Data[0].close()
            self.Data.pop()
            return ''

class wseq:
    '''for reading through a file one word at a time.
    '''
    def __init__(self, filename, isgraph=isgraph_py4000):
        self.Data = seq(filename)
        self.isgraph = isgraph
    def _advance(self):
        '''read and return the next graphic character.'''
        while True:
            c = next(self.Data)
            if not c or self.isgraph(ord(c)):
                return c
    def __next__(self):
        '''Conceptually, returns the next word in the
        underlying file.
        '''
        c = self._advance()
        if not c:
            return c
        l = [c]
        while True:
            c = next(self.Data)
            if not c or not self.isgraph(ord(c)):
                return ''.join(l)
            else:
                l.append(c)
 
class dict_:
    '''Dictionary items are numbered from the beginning / root:
    indices of existing words are to remain constant for the
    duration of a Dictionary.
    '''
    # Recent: KEYS ARE NAMES, VALUES ARE INDICES INTO Data
    #TODO: VALUES OF Recent SHOULD BE list-S THAT ARE APPENDED
    # WHEN ITEMS ARE ADDED AND pop-PED WHEN ITEMS ARE REMOVED.
    def __init__(self, code_default=lambda: None):
        self.CODE_DEFAULT = code_default
        self.Data = [] # HOLDS ALL THE WORDS, IN THE ORDER DEFINED
        self.Recent = {}
                # FOR A GIVEN NAME, HOLDS ALL THE WORDS, IN THE
                # ORDER DEFINED.
    def _parse(self, string):
        return tuple(string.split())
    def _unparse(self, string_tuple):
        return ' '.join(string_tuple)
    def __contains__(self, key):
        '''key is a string, possiby with whitespace. Internally,
        names are stored as tuples of strings. For example, 'set
        color' would become ('set', 'color')
        '''
        return self._parse(key) in self.Recent
    def _contains_nodename(self, key):
        '''The key is as stored internally (see __contains__).
        '''
        return key in self.Recent
    def __contains__(self, key):
        return key in self.Recent
    def __getitem__(self, key):
        return ( {} if key not in self else self.Data[
            self.Recent[key][-1] ] )
    def __iter__(self):
        '''Iterate beginning with the most recent node.'''
        return reversed(self.Data)
    def __repr__(self):
        return 'dictionary(' + str(len(self.Data))  + '): ' + \
            ' '.join(map(str, self.keys())) + '.'
    def __len__(self):
        return len(self.Data)
    def top(self):
        return self.Data[-1]
    def keys(self):
        return self.Recent.keys()
    def _name(node):
        return '' if 'NAME' not in node else node['NAME']
    def enumerate(self):
        '''Dictionary nodes are enumerated beginning with the
        last item. Numbering descends from -1.
        '''
        return map(
            lambda enum_item: (
                len(self) - enum_item[0], enum_item[1]), 
            enumerate(iter(self), 1))
    def index(self, name):
        '''Returns a (possibly empty) tuple containing the
        indices of all nodes matching name.
        '''
        from functools import partial
        unparsed_name = self._unparse(name)
        tuple(map(
            lambda enum_name: enum_name[0],
            filter(
                lambda enum_name:
                    enum_name[1] == unparsed_name,
                enumerate(iter(self), 1))))
    def _extend(self): #WAS extend
        '''Create a new, empty entry at the end of the
        Dictionary.
        '''
        self.Data.append({})
    def edit(self, key, value):
        '''Update the key-value pair in the entry at the end of
        the Dictionary. Reminder: this method is not protected
        (e.g., _edit) because the ability to edit the top of the
        Dictionary is fundamental to Forth.

        key should be one of 'NAME', 'CODE', or 'DATA'.
        '''
        self.Data[-1].update({key: value})
    def head(self):
        '''Return the entry at the end of the Dictionary.
        '''
        return self.Data[-1]
    def pop(self):
        '''Removes the most recent entry in the Dictionary.
        Nearly the opposite of extend-link.
        '''
        WORD = self.Data.pop()
        word = WORD['NAME']
        if len(self.Recent[word]) < 2:
            self.Recent[word].pop()
        else:
            self.Recent[word].pop()
        return WORD
    def link(self):
        HEAD = self.head()
        if 'NAME' in self.head():
            INDEX = len(self) - 1
            NAME = HEAD['NAME']
            if self._contains_nodename(NAME):
                # DUPLICATE NAME.
                # APPEND AN INDEX TO THE NEW NODE.
                self.Recent[NAME].append(INDEX)
            else:
                # NEW NAME.
                # MAKE A NEW ENTRY IN THE INDEX OF RECENT ITEMS.
                self.Recent.update({NAME: [INDEX]})
    def append(self, name=None, code=None, data=None):
        '''Now (2019-08-05), every dictionary entry will have all
        three fields---expected to be simpler in the long
        run---allowed removal of include_data method (since
        there will always be a data field).
        '''
        self._extend()
        #dbprint('dict_: append: name:', name)
        if name:
            assert isinstance(name, str)
        self.edit('NAME', '' if not name else name)
        self.edit('DATA', data)
        self.edit('CODE', self.CODE_DEFAULT if not code else code)
        self.link()

class base:
    '''A base class for the Data Stack, Return Stack, etc.'''
    def __init__(self, default=''):
        self.DEFAULT = default
        self.Data = list()
    def __len__(self):
        return len(self.Data)
    def clear(self):
        self.Data.clear()
    def pop(self):
        return self.DEFAULT if not self.Data else self.Data.pop()
    def _popn(self, n):
        '''pop n items, return them as a tuple.
        '''
        return tuple(map(lambda _: self.pop(), range(n)))
    def __repr__(self):
        return repr(self.Data)

class primitive_stack(base):
    '''Originally created to support io_istack class.
    '''
    def __repr__(self):
        return 'primitive_stack(' + base.__repr__(self) + ')'
    def tos(self):
        '''Return Top of Stack.'''
        if not self.Data:
            self.Data.append(self.DEFAULT)
        return self.Data[-1]

class io_istack(primitive_stack):
    '''
    '''
    def repr(self):
        return 
    def push(self, filename):
        dbprint('io_istack: ', self.tos())
        self.Data.append(wseq(filename))
    def drop(self):
        if self.tos() is not stdin:
            # wseq ELEMENTS ARE EXPECTED TO CLOSE THE UNDERLYING
            # FILES.
            self.pop()

class stack(primitive_stack):
    '''ancestor of data stack and return stack.
    '''
    def __repr__(self):
        return 'stack(' + base.__repr__(self) + ')'
    def sos(self):
        '''Return Second on Stack.'''
        return self.DEFAULT if len(self.Data) < 2 else self.Data[-2]
    def push(self, item):
        self.Data.append(item)
    def drop(self):
        self.pop()
    def dec(self):
        '''Decrement TOS.'''
        self.Data[-1] -= 1

class clock:
    '''Allows tracking of artificial clock cycles.
    Originally intended that each return stack should have
    only one Clock and that it is incremented each time the
    program counter is altered.
    '''
    def reset(self, time=-1):
        self.time = time
    def __init__(self, time=-1):
        self.reset(time)
    def tick(self):
        self.time -= 1
    def read(self):
        return self.time

class return_stack(stack):
    '''Conceptually, the return stack holds double cells. One
    element of a double cell is a local counter that is used in
    leiu of a program counter. The other element is an address
    of a word list.'''
    def push_list(self, list_):
        self.push(list_)
        self.push(len(list_))
    def drop2(self):
        self.drop()
        self.drop()
        if not len(self): # RETURN STACK EMPTY
            self.push_list(self.DEFAULT_LIST)
    def ebb(self):
        '''Jump to beginning of word.
        '''
        self.drop()
        self.push(len(self.tos()))
    def __init__(self, default_list=('QUERY',)):
        stack.__init__(self)
                # WANT TO DO ALL THE STEPS OF THE BASE CLASS
        self.DEFAULT_LIST = default_list
        self.drop2()
        self.clock = clock()
    def _repr_fmt_s(self, width):
            return '{:' + str(width) + '.' + str(width) + '}'
    def _repr_fmt_i(self, width):
            return '{:0' + str(1 + width) + '}'
    def _word_list_repr(self, words, width):
        return \
            ' '.join(map(
                lambda s: self._repr_fmt_s(width).format(s),
                words))
    def _overbar(self, length, k, width):
        '''print-s an overbar above the current word in the list
        under evaluation.
        '''
        return (
            self._repr_fmt_i(width).format(k) +
            ':' * (1 + width) * (length - k) + '_' * width)
    def __repr__(self, width=4):
        k = len(self) - 1 # START AT THE TOP
        deq = deque()
        for _ in range(4):
            deq.appendleft(self._overbar(
                len(self.Data[k - 1]),
                self.Data[k],
                width))
            deq.appendleft(
                self._word_list_repr(
                    (' ' * width,) + self.Data[k - 1],
                    width))
            k -= 2
            if k < 0:
                break # RETURN STACK MIGHT NOT BE 4 UNITS DEEP
        deq.append('Return Stack:---')
        deq.reverse()
        return '\n'.join(deq)
    def reset_clock(self, time=-1):
        self.clock.reset(time)
    def read_clock(self):
        return self.clock.read()
    def opera(self, n=1):
        '''Return the next token in the list under evaluation.'''
        return self.sos()[self.tos() - n]
    def step(self):
        self.clock.tick()
        self.dec()
        if not self.tos(): # NO MORE INSTRUCTIONS
            self.drop2()
            if not len(self): # RETURN STACK EMPTY
                self.push_list(self.DEFAULT_LIST)

class data_stack(stack):
    '''Also known as "the stack" or "S".
    '''
    def __init__(self):
        stack.__init__(self)
        self.SideStack = []
    def _repr_fmt(self, width):
        return '{:' + width + '.' + width + '}'
    def __repr__(self):
        '''TODO: replace magic number 8, number of items to
        show, with a paramter. TODO: replace magic number 64,
        number of columns to print, with a parameter.
        '''
        TAG = list(map('{:d}: '.format, range(8)))
        TAG.reverse()
        MAX_ITEMS =  8
        SNC       = str(64)
        n = min(MAX_ITEMS, len(self))
        l = ['Data Stack (' + str(len(self.Data)) + '):---']
        for k in range(-1, -1 - n, -1):
            l.append(TAG[k] + repr(self.Data[k]))
        if MAX_ITEMS < len(self):
            l.append('    ...')
        l.append('---;')
        return '\n'.join(map(
            lambda s: self._repr_fmt(SNC).format(s),
            l))
    def cover(self):
        self.SideStack.append(
            self.DEFAULT if not len(self) else self.Data.pop())
    def recover(self):
        self.Data.append(
            self.DEFAULT if not len(self.SideStack) else
            self.SideStack.pop())
    def dup(self):
        self.push(self.tos())
    def over(self):
        self.push(self.sos())
    def extend(self, iterable):
        '''Intended use: place multivalues (tuples returned from
        codewords) onto the Stack.
        '''
        self.Data.extend(iterable)

class common:
    '''Functions common to all computers.  These functions
    return tuples whose values are to be placed on the stack.

    TODO (Maybe) build dict of these, to be partial-ed for
    specific computer-s?
    
    Allows computers to be interactive?
    '''
    def rub(string):
        dbprint('common: rub.')
        return (string,) if not string else (string[1:],)
    def nop(*args, **kwargs):
        dbprint('common: nop.')
        return ()
    def number(string):
        '''Attempt to convert the string at TOS to an int.
        Returns the converted value at SOS and a flag at TOS.
        The flag indicates whether there was an error: 0 (FALSE)
        ==> no error, -1 (TRUE) ==> error
        '''
        try:
            n = (int(string), 0)
        except:
            n = (-1, -1)
        return n
    def aint(obj):
        '''Convert any object that into an int, event if it
        ain-t.
        '''
        if obj is None:
            return 0
        if isinstance(obj, bool):
            return -int(obj)
        if isinstance(obj, int):
            return obj
        if isinstance(obj, float):
            return int(obj)
        if isinstance(obj, complex):
            return common.aint(obj.real)
        if isinstance(obj, (bytes, bytearray)):
            return any(tuple(obj))
        return -1 if obj else 0
    def _demote(obj):
        '''Returns the cardinal flag corresponding to an object.
        '''
        return (0, -1)[bool(obj)]
    def digit(obj):
        digits =tuple(chain(
            map(str, range(10)),
            map(chr, range(65, 65+26))))
        return '?' \
            if \
                not isinstance(obj, int) or \
                len(digits) <= obj \
            else digits[obj]
    def eval_(obj):
        return eval(obj),
    def chr_(obj):
        return chr(obj),
    def str_(obj):
        return str(obj),
    def demote(obj):
        return common._demote(obj),
    def zless(obj):
        return common.aint(obj) < 0,
    def less(a, b):
        return common.aint(a) < common.aint(b),
    def and_(a, b):
        return common.aint(a) & common.aint(b),
    def or_(a, b):
        return common.aint(a) | common.aint(b),
    def xor(a, b):
        return common.aint(a) ^ common.aint(b),
    def divmod_(a, b):
        return divmod(common.aint(a), common.aint(b))
    def div(a, b):
        return common.aint(a) // common.aint(b),
    def mod(a, b):
        return common.aint(a) % common.aint(b),
    def not_(a):
        return ~ common.aint(a),
    def plus1(n):
        return n + 1,
    def neg(n):
        return -n,
    def plus(a, b):
        return a + b,
    def subtract(a, b):
        return b - a,
    def abs_(a):
        if isinstance(a, (int, float)):
            return abs(a),
        return a,
    def equal(a, b):
        return common._demote(a == b),
    def less(a, b):
        return common._demote(b < a),
    def min_(a, b):
        return min(a, b),
    def max_(a, b):
        return max(a, b),
    def starslash(a, b, c):
        bc = b * c
        return bc // a, bc % a
    def len_(a):
        return len(a),

class worm:
    '''STATUS: IN PROGRESS An append-only list. Designed for
    key-value pairs. A building block for branching vocabularies
    / namespaces.
    '''
    def __init__(self):
        #TODO PROVISION FOR 1-LAYER DEEP COPY FOR PURPOSE OF
        # COPY AND MODIFY. ALLOW COPY OF ANY OR ALL ITEMS.
        self.Data = []
        self.Keys = set()
    def __contains__(self, key):
        return key in self.Keys
    def __getitem__(self, key):
        for k, v in reversed(self.Data):
            if k == key:
                return v
    def __len__(self):
        return len(self.Data)
    def __repr__(self):
        return 'worm(' + str(len(self)) + ')'
    def _ispair(item):
        if not isinstance(item, tuple):
            return False
        if not len(item) == 2:
            return False
            item[0]
    def __append__(self, item):
       self.Data.append(item)
    def extend(self):
        pass

class memory:
    def __init__(self):
        self.Data = []
    def __len__(self):
        return len(self.Data)
    def __getitem__(self, key):
        if key < len(self):
            return self.Data[key]
        return None
    def __repr__(self):
        return 'memory(' + str(len(self.Data)) + ')'
    def clear(self):
        self.Data.clear()
    def extend(self, iterable):
        self.Data.extend(iterable)
    def __setitem__(self, key, value):
        overreach = key - len(self) + 1
        if 0 < overreach:
            self.extend((None,) * overreach)
        self.Data[key] = value
    def dump(self, key, n=16, sep='\n\n'):
        print(*self.Data[key:(key + n)], sep=sep)

class computer:
    '''This is the central class. The system consists of a
    deque of instances of computer, along with a few common
    interfaces.

    From the outside, typically call resume.

    TODO: Prompt shold indicate compile or interpret mode.
    '''
    def bye(self):
        '''reutrn 'BYE' to forth. Expectation is that computer
        will be destroyed. FUTURE: the state of the computer
        might be saved (hibernate).
        '''
        return 'BYE'
    def ttfn(self):
        '''That's, "ta-ta for now." return 'TTFN' to forth.
        Expectation is that computer will be suspended for
        possible reanimation at a later time.
        '''
        return 'TTFN'
    def revisit(self):
        return 'REVISIT'
    def neighbors(self):
        '''return 'NEIGHBORS' to forth. Expectation is that a
        representation of the the cluster members will be
        print-ed.
        '''
        return 'NEIGHBORS'
    def __init__(self,
            id_='42', prompt='OK> ', default_list=('QUERY',),
            character_set_in_ =
                    character_set_in(isgraph_py4000),
            character_set_internal_=
                    character_set_internal(isgraph_py4000)):
        '''**** IN PROGRESS ****
        default_list must be a singleton tuple of str. see next_'''
        self._CHARACTER_SET_INTERNAL = character_set_internal_
        self._CHARACTER_SET_IN = character_set_in_
        self.stream = deque()
        self.I = io_istack(default=stdin)
        self.ID = id_
        self.S = data_stack()
        self.R = return_stack(default_list=default_list)
        self.D = dict_()
        self.N = []
        self.PC = [None] # PROGRAM COUNTER: WORD UNDER EVALUATION
                # ONLY _execute SHOULD CHANGE THE VALUE. USE
                # self._pc TO READ THE VALUE
        self.Halted  = [True] # A REGISTER: TRACK HALTED NODES
        self.PROMPT = '<' + self.ID + prompt
        #TAG PRIMITIVES
        self.parse_string = partial(
            parse_string,
            self._CHARACTER_SET_INTERNAL,
            self._CHARACTER_SET_IN)
        def mappend(arg):
            '''multiple append. A throw-away function to
            facilitate the building of the dictionary using the
            call below.
            '''
            # THE if ALLOWS () AT END OF TUPLE IN MAPPED OBJECT
            # IN THE CALL BELOW.
            if arg:
                self.D.append(
                    name=arg[0],
                    code=arg[1],
                    data=None if len(arg) <3 else arg[2])
        tuple(map(mappend, (
            ('SNIP',        self.snip),
            ('LINK',        self.link),
            ('EXECUTE',     self.execute),
            ('DOLST',       self.dolst),
            ('EMIT',        self.emit),
            ('FIND',        self.find),
            (',',           self.comma),
            (',,',          self.commacomma),
            (':',           self.colon),
            (';',           self.semicolon),
            ('BACK',        self.tor),
            ('BL',          self.docon,      (' ',)),
            ('DOCON',       self.docon, (self.docon,)),
            ('DOVAR',       self.docon, (self.dovar,)),
            ('@',           self.fetch),
            ('!',           self.store),
            ('BYE',         self.bye),
            ('DROP',        self.drop),
            ('DUP',         self.dup),
            ('FORTH',       self.fromr),
            ('HALT',        self.halt),
            ('HERE',        self.here),
            ('NEIGHBORS',   self.neighbors),
            ('NOP',         self.nop),
            ('OVER',        self.over),
            ('QUERY',       self.query),
            ('RUB',         self.rub),
            ('SEE',         self.see),
            ('TTFN',        self.ttfn),
            ('REVISIT',     self.revisit),
            ('WORDS',       self.words),
            ('LOAD',        self.load),
            ('##',          self.number),
            ('DEMOTE',      self.demote),
            ('NOT',         self.not_),
            ('AND',         self.and_),
            ('EOR',         self.xor),
            ('OR',          self.or_),
            ('0<',          self.zless),
            ('<',           self.less),
            ('+',           self.plus),
            ('1+',          self.plus1),
            ('/MOD',        self.divmod_),
            ('MOD',         self.mod),
            ('/',           self.div),
            ('-',           self.neg),
            ('--',          self.subtract),
            ('ABS',         self.abs_),
            ('==',          self.equal),
            ('MAX',         self.max_),
            ('MIN',         self.min_),
            ('*/',          self.starslash),
            ('DIGIT',       self.digit),
            ('STR',         self.str_),
            ('CHR',         self.chr_),
            ('EVAL',        self.eval_),
            ('.',           self.dot),
            ('LEN',         self.len_),
            ('DEPTH',       self.depth),
            ('EBB',         self.ebb),
            ('IF',          self.if_),
            () ))) # EMPTY TUPLE AT END FOR EASY APPEND
    def _pc(self): return self.PC[0]
    def __repr__(self):
        return 'computer(' + self.ID + ')'
    def ishalted(self):
        '''Intended to be called externaly.'''
        return self.Halted[0]
    def _halt(self):
        self.Halted[0] = True
    def _unhalt(self):
        self.Halted[0] = False
    def halt(self):
        '''Suspend execution. Return control to Forth.  Should
        be called when two undefined words in a row are
        encountered.
        '''
        self._halt()
        return 'HALT'
    def warm(self):
        '''TODO: Should warm actually start the interpreter?'''
        self._unhalt()
        self.next_()
    def cold(self, boot=()):
        self.S.clear()
        self.R.clear()
        if boot:
            self.R.push_list(boot)
        self.warm()
    def _execute(self):
        self.PC[0] = self.D[self.S.pop()]
        return self._pc()['CODE']()
    def execute_maybe(self):
         return (
            self.next_
            if self.S.tos() not in self.D
            else
            self._execute() )
    def next_(self):
        '''Place on the Stack the word being processed then, if
        it is defined, execute it (undefined words are left on
        the Stack ---after all, traditional forth places numbers
        on the stack, and a numbers meaning is not determined at
        that time.)
        '''
        self.S.push(self.R.opera())
        self.R.step()
        return self.execute_maybe()
    def wake(self, *args, **kwargs):
        '''Activate this computer from external call.
        '''
        self.Halted[0] = False
        return self.next_()
                # AND self.next TYPICALLY RETURNS ITSELF
    def sleep(self):
        '''Activate this computer from external call.
        '''
        self.Halted[0] = False
        return 'SLEEP'
    def resume(self):
        '''Intended to be called after the computer is modified
        by an external process so that recovery from halt is
        possible.'''
        self.Halted[0] = False
        self.wake()
    def codeword_fn(function):
        '''Transforms a primitive function that returns zero or
        more values into a codeword: apply the function, place
        the elements of the returned tuple on the Stack, then
        call next_.'''
        def inner(self, *args, **kwargs):
            from inspect import getargspec
            self.S.extend(function(
                *self.S._popn(
                    len(getargspec(function)[0])), **kwargs))
            return self.next_
        return inner
    nop    = codeword_fn(common.nop)
    number = codeword_fn(common.number)
    demote = codeword_fn(common.demote)
    not_   = codeword_fn(common.not_)
    and_   = codeword_fn(common.and_)
    or_    = codeword_fn(common.or_)
    xor    = codeword_fn(common.xor)
    zless  = codeword_fn(common.zless) #ZLESS
    less   = codeword_fn(common.less)  #LESS
    digit  = codeword_fn(common.digit) #DIGIT
    str_   = codeword_fn(common.str_)  #str
    chr_   = codeword_fn(common.chr_)
    eval_  = codeword_fn(common.eval_)
    plus   = codeword_fn(common.plus)
    plus1  = codeword_fn(common.plus1)
    neg    = codeword_fn(common.neg)
    divmod_= codeword_fn(common.divmod_)
    div    = codeword_fn(common.div)
    mod    = codeword_fn(common.mod)
    subtract=codeword_fn(common.subtract)
    abs_   = codeword_fn(common.abs_)
    equal  = codeword_fn(common.equal)
    max_   = codeword_fn(common.max_)
    min_   = codeword_fn(common.min_)
    starslash=codeword_fn(common.starslash)
    len_   = codeword_fn(common.len_)
    def codeword(function):
        '''Transforms a 'None'-returning primitive function
        into a codeword: apply the function, then return next_.
        '''
        def inner(self, *args, **kwargs):
            function(self, *args, **kwargs)
            return self.next_
        return inner
    @codeword
    def dot(self):
        '''Ting's DOT puts the space afterwards.
        '''
        print('', self.S.pop(), end='')
    @codeword
    def execute(self):
        self.execute_maybe()
    @codeword
    def emit(self):
        string = self.S.pop()
        if isinstance(string, str):
            print(string, end='')
    @codeword
    def if_(self):
        '''Quit current word if zero flag on Stack.
        '''
        if not self.S.pop():
            self.R.drop2()
    @codeword
    def ebb(self):
        self.R.ebb()
    @codeword
    def depth(self):
        self.S.push(len(self.S))
    @codeword
    def load(self):
        self.I.push(self.S.pop())
        self.stream.extend(('NOP',))
        dbprint('load: self.stream:', self.stream)
    @codeword
    def semicolon(self): # SEMICOLON
        '''Similar to conventional Forth semicolon.
        '''
        self.D.edit(
            'DATA',
            tuple(reversed(self.D.head()['DATA'])))
    def _rub(self):
        if self.S.tos():
            self.S.push(self.S.pop()[1:])
    rub = codeword(_rub)
    @codeword
    def ddump(self): #TAGS TOD TOP OF DICTIONARY
        '''Display the DATA portion of the top of the
        Dictionary, limited to 16 words.
        '''
        words = self.D.top()['DATA']
        name = '' if 'NAME' not in self.D.top() else \
                self.D.top()['NAME']
        print("Dictionary['", name, "']['DATA']:---", sep='')
        if words:
            print(
                *reversed(words[:16]),
                '' if len(words) < 17 else '  +   [...]')
        print('---;')
    @codeword
    def see(self):
        key = self.S.pop()
        print('Definition (', key, '):---', sep='')
        if key in self.D:
            D = self.D[key]
            if 'DATA' in D:
                print(*reversed(D['DATA']))
        print('---(End Definition)')
    @codeword
    def find(self):
        '''Place the specified Dictionary item to the Stack.
        '''
        self.S.push(self.D[self.S.pop()])
    @codeword
    def snip(self):
        '''remove the last Dictionary item to the Stack.
        '''
        self.S.push(self.D.pop())
    @codeword
    def commacomma(self): # COMMACOMMA
        '''moves an item from the Stack to the CODE
        item of the Dictionary.
        '''
        self.D.edit('CODE', self.S.pop())
    @codeword
    def comma(self): # COMMA
        '''moves a string from the Stack to the end of the DATA
        item of the Dictionary, first removing its first
        character.
        '''
        self._rub()
        self.D.top()['DATA'].append(self.S.pop())
    @codeword
    def here(self):
        '''Pushes the DATA list at the top of the Dictionary on
        to the Stack.
        '''
        self.S.push(self.D.top())
    @codeword
    def words(self):
        print(*iter(self.D.keys()))
    def _link(self): # CF. { n$ } IN TING
        '''Create a new entry in the Dictionary with the NAME
        popped from the Stack.
        '''
        self.D.append(name=self.S.pop())
        self.D.link()
        self.D.edit('DATA', [])
    @codeword
    def link(self): # CF. { n$ } IN TING
        '''Create a new entry in the Dictionary with the NAME
        popped from the Stack.
        '''
        self._link()
    @codeword
    def colon(self): # COLON
        '''Create a new entry in the Dictionary with the NAME
        popped from the Stack and dolst as the CODE.
        '''
        self._link()
        self.D.edit('CODE', self.dolst)
    def _dovar(self):
        self.S.push(
            self.S.DEFAULT if 'DATA' not in self._pc() else
            self._pc()['DATA'])
    def _make2var(self):
        self._link()
        WORD = self.D.top()
        WORD['DATA'].extend((None, None))
    @codeword
    def dovar(self):
        self._dovar()
    @codeword
    def docon(self):
        self._dovar()
        self.S.push(self.S.pop()[0])
    def _dolst(self):
        self.R.push_list(self._pc()['DATA'])
    @codeword
    def dolst(self):
        self._dolst()
    @codeword
    def drop(self):
        self.S.drop()
    @codeword
    def dup(self):
        self.S.dup()
    @codeword
    def over(self):
        self.S.over()
    @codeword
    def fromr(self):
        self.S.recover()
    @codeword
    def tor(self):
        self.S.cover()
    @codeword
    def fetch(self): #AT FETCH
        '''Extract the first item from the list-like container
        at TOS.'''
        self.S.push(self.S.pop()[0])
    @codeword
    def store(self):
        value = self.S.pop()
        container = self.S.tos()
        container[0] = value
    @codeword
    def query(self):
        while not self.stream:
            from_ = self.I.tos()
            if from_ is stdin:
                print('- ' * 32)
                self.ddump()
                print(self.S) # EQUIVALENT OF CALL TO DOTS IN TING
                print(self.PROMPT, end='') #SEE DOTOK IN TING
                stdout.flush()
                text = from_.readline()
            else:
                # WORDS IN FILES NEED TO BE READ ONE AT A TIME
                # BECAUSE ONE OF THEM MIGHT BE ANOTHER { LOAD }.
                text = next(self.I.tos())
            self.stream.extend(self.parse_string(text))
            if not self.stream:
                self.I.drop()
        items = self.stream.popleft()
        self.R.push_list((items,))

class cluster:
    '''Conceptually, an enumerated list of computers.
    '''
    def drop(self):
        if 0 <= self.Ring[0][0]:
            self.Ring.popleft()
        else:
            print("Can't drop master node.")
    def __init__(self, names=('/Master/', '/Slave 0/', '/Slave 1/')):
        '''Slave 1 is the name of Boba Fett's ship.
        '''
        self.Ring = deque(enumerate(map(computer, names), -1))
                # THE ONE NUMBERED -1 IS SPECIAL. SEE LOGIC IN
                # self.next.
    def __iter__(self):
        for enumerated_computer in self.Ring:
            yield enumerated_computer
    def _rotate(self):
        '''Move *IN PLACE* first computer to the back of the
        ring.
        '''
        self.Ring.append(self.Ring.popleft())
    def _unrotate(self):
        '''Move *IN PLACE* first computer to the back of the
        ring.
        '''
        self.Ring.appendleft(self.Ring.pop())
    def __len__(self):
        return len(self.Ring)
    def __repr__(self):
        return 'cluster(' + ', (' + \
                ', '.join(map(lambda x: repr(x[1]), self.Ring)) + ')'
    def _next(self, direction):
        '''Find and return the next non-halted computer.
        '''
        HEAD, NUMBER, COMPUTER = 0, 0, 1
        for i in range(len(self.Ring)):
            if direction:
                self._rotate()
            else:
                self._unrotate()
            if self.Ring[HEAD][NUMBER] == -1:
                Node = self.Ring[HEAD][COMPUTER]
            elif not self.Ring[HEAD][COMPUTER].ishalted():
                return self.Ring[HEAD][COMPUTER]
        return Node
    def next(self):
        return self._next(True)
    def prev(self):
        return self._next(False)
    def current(self):
        '''return the currnet computer.
        '''
        HEAD, NUMBER, COMPUTER = 0, 0, 1
        return self.Ring[HEAD][COMPUTER]

class forth:
    '''Coordinates computation among the computer-s
    '''
    def __init__(self,
        computer_names=('/Master/',
            '/Slave 0/', '/Slave 1/',
            '/Slave 2/', '/Slave 3/',
            '/Slave 4/', '/Slave 5/',
            '/Slave 6/', '/Slave 7/'),
        save=[]):
        '''Creates one or more computers (one for each of the
        computer_names) and begins execution of the first one.
        '''
        self.Cluster = cluster(computer_names)
        for enumerated_computer in self.Cluster:
            enumerated_computer[1].cold(boot=('HALT',))
            enumerated_computer[1].sleep()
        save.append(self)
        self.run()
    def run(self):
        '''Check the Ring for next non-halted computer. Hand
        control to it.
        Control could return on the following conditions:
                - after a number of clock cycles,
                - after that computer defaults to QUERY,
                - after a computer executes BYE.
        '''
        fun = self.Cluster.next().wake
        while (True):
            while (isinstance(fun, (
                    type(lambda: None), # function
                    type(self.run)      # class method
            ))):
                fun = fun()
                # Python 3 BUSIES ITSELF WITH SIMULATING THE
                # ACTION OF THE WOKE computer. WHEN THE WOKE
                # computer IS DONE, IT MIGHT RETURN SOMETHING
                # OTHER THAN A function.
            if fun == 'NEIGHBORS':
                print(self.Cluster)
            elif fun == 'BYE':
                fun = self.Cluster.next().wake
                self.Cluster.prev().wake
                self.Cluster.drop()
                continue
            elif fun == 'REVISIT':
                fun = self.Cluster.prev().wake
                continue
            elif fun == 'TTFN':
                # SHOULD NOT NEED TO DO ANYTHING SPECIAL.
                # JUST CONTINUE TO NEXT computer.
                pass
            else:
                print('Received unrecognized message from computer.')
            fun = self.Cluster.next().wake
