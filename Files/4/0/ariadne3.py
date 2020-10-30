'''     ARIADNE III
        COPYRIGHT (2020) D. MICHAEL PARRISH.
        SEE ALSO ACCOMPANYING LICENCE.

# ONE BOOT PROCESS THAT SEEMS TO WORK BEGINS HERE AND PROCEEDS
# TO THE NEXT TRIPPLE QUOTE:

# **** DELETE EVERYTHING THAT'S NOT BUILT IN TO PYTHON 3 ****
for name in dir():
    if name != 'name' and not (name[:2] == '__' and name[-2:] == '__'):
        exec('del ' + name)

del name

from copy import deepcopy # FOR MAKING COPIES OF ARIADNE.
from os import chdir
chdir('~/ARIADNE3') # OR WHEREVER... ariadne3.py AND...
                    # ariadne3.clew ARE FOUND

with open('ariadne3.py') as f:
    exec(f.read())
    del f

# ONCE THE FOLLOWING EXPRESSION EVALUATES, YOU SHOULD SEE THE
# OK PROMPT. AT THE PROMPT, ENTER ariadne3.clew LOAD
a['sail'](a) # WE'RE NOT IN KANSAS ANYMORE.

'''
'''
# CONVENTIONS

## Annotation (in comments)

        Forth words are sometimes enclosed in braces {  },
        especially if the word or words in question are composed
        of non-alphanumeric characters.

## def

        def's with names beginning with underscore (_) are not
        intended to be called from Ariadne.

## Exceptions

        Ariadne doesn't quit. For example, when a bad index is
        given to { ] }, Ariadne halts, but does not crash. A
        KeyboardInterrupt (press CTRL + C in Linux or Windows)
        will force Ariadne to halt.

## Forth Words

    !   Words beginning with '!' are command-words that should
        be thought of as _programs_ that may not behave as
        typical Forth words. Example:  { !:- } reads the next
        line from the input stream and places that line on the
        Stack.

    !   Words ending with '!' indicate that something is being
        mutated. However, typically words that manipulate only
        the Stack do not typically have the '!' suffix.

    `   With the exception of  { ` }, there are no words which
        begin with accent grave (a.k.a. backtick, backquote).

    '   With the exception of  { ' }, there are no words which
        begin with single quote (a.k.a tick mark).

        The ` or ' characters may therefore be used to
        guarantee that a word beginning with either of these
        characters has predictable behavior (i.e., to be placed
        on the Stack).
'''


_a = {}

_a['globals'] = globals()
from sys import stdin
_a['stdin'] = stdin
del stdin

a = {}

a['_EXTERNAL'] = '_a'

a['_SELF'] = a

a['_MI'] = "API'ADNE" # _MI: A NAME I CALL MYSELF

a['_ATTN'] = [False] # WHEN SET, ARIADNE IS REQUESTING FULL ATTENTION

a['_BACK_STACK'] = [] # USED BY { BACK } AND { FORTH }

a['_DATA'] = {} # DATA FIELDS FOR WORDS HAVING DATA

a['_DICTIONARY'] = {}

a['_ARCHIVE'] = { 'DATA': {},   'DICTIONARY': {} }

a['_INPUTS'] = [lambda x: eval(x['_EXTERNAL'])['stdin']]

a['_INPUT_FILES'] = [None]

a['_Python'] = {}
a['py'] = a['_Python']

a['_Python']['DEFAULT'] = ''

a['_Python']['WILDCARD'] = '*'

def defaultlist(x):
    return [x['_Python']['DEFAULT']] * 4

a['_Python']['defaultlist'] = defaultlist
del defaultlist

a['_DATA_STACK'] = a['_Python']['defaultlist'](a)

a['_Python']['RDEFAULT'] = ('QUERY',)

a['_RETURN_STACK'] = [
    a['_Python']['RDEFAULT'],
    len(a['_Python']['RDEFAULT'])]

a['_WORD_UNDER_CONSTRUCTION'] = [None]

from collections import deque
a['_INPUT_BUFFER'] = deque()
del deque

# ALIASES
a[ 'd'] = a['_DICTIONARY']
a['in'] = a['_INPUT_BUFFER']
a[ 'r'] = a['_RETURN_STACK']
a[ 's'] = a['_DATA_STACK']



# TOOLS FOR BUILDING UP ARIADNE


def _include(x, obj):
    name = getattr(obj, '__name__')
    PY = x['_Python']
    PY[name] = obj

a['_include'] = _include
del _include


def _expand(x, NAME, name=None):
    name = NAME.lower() if name is None else name
    x['_DICTIONARY'][NAME] = lambda y: y['_Python'][name](y)

a['_include'](a, _expand)
a['_expand'] = _expand
del _expand


def _extend(x, obj, NAME=None, name=None):
    x['_include'](x, obj)
    NAME = getattr(obj, '__name__').upper() if NAME is None else NAME
    x['_expand'](x, NAME, name)

a['_include'](a, _extend)
a['_extend'] = _extend
del _extend



# THE STACK


def _top(x):
    return x['_DATA_STACK'][-1]

a['_include'](a, _top)
del _top


def dup(x):
    x['_DATA_STACK'].append(x['_DATA_STACK'][-1])

a['_extend'](a, dup)
del dup


def _push(x, obj):
    x['_DATA_STACK'].append(obj)

a['_include'](a, _push)
del _push


def drop(x):
    S = x['_DATA_STACK']
    if len(S) < 5:
        S.insert(0, x['_Python']['DEFAULT'])
    return S.pop()

a['_extend'](a, drop)
del drop


def over(x):
    S = x['_DATA_STACK']
    S.append(x['_Python']['DEFAULT'] if len(S) < 2 else S[-2])

a['_extend'](a, over)
del over


def clear(x):
    x['_DATA_STACK'].clear()
    x['_DATA_STACK'].extend(x['_Python']['defaultlist'](x))

a['_extend'](a, clear)
del clear


def _top4(x):
    return tuple(x['_DATA_STACK'][-4:])

a['_include'](a, _top4)
del _top4


def _isLongStr(string):
    from os import get_terminal_size
    return get_terminal_size()[0] // 2 < len(string)

a['_include'](a, _isLongStr)
del _isLongStr


def _reprstr(x, string):
    PY = x['_Python']
    return PY['WILDCARD'] if PY['_isLongStr'](string) else string

a['_include'](a, _reprstr)
del _reprstr


def _repr4(x):
    PY = x['_Python']
    from functools import partial
    return tuple(map(
        partial(PY['_reprstr'], x),
        map(repr, PY['_top4'](x))))

a['_include'](a, _repr4)
del _repr4



# THE BACK STACK

def back(x):
    x['_BACK_STACK'].append(x['_Python']['drop'](x))

a['_extend'](a, back)
del back


def forth(x):
    PY = x['_Python']
    PY['_push'](x,
        PY['DEFAULT']
        if not x['_BACK_STACK'] else
        x['_BACK_STACK'].pop() )

a['_extend'](a, forth)
del forth



# THE RETURN STACK


def opera(x):
    return x['_RETURN_STACK'][-2][x['_RETURN_STACK'][-1]]

a['_include'](a, opera)
del opera


def _defaultInterrupt(x):
    proc = x['_Python']['RDEFAULT']
    x['_RETURN_STACK'].extend((proc, len(proc)))

a['_include'](a, _defaultInterrupt)
del _defaultInterrupt


def _rclear(x):
    x['_RETURN_STACK'].clear()
    x['_Python']['_defaultInterrupt'](x)

a['_include'](a, _rclear)
del _rclear


def _rdrop(x):
    R = x['_RETURN_STACK']
    if 2 < len(R):
        R.pop()
        R.pop()
    else:
        x['_Python']['_rclear'](x)

a['_include'](a, _rdrop)
del _rdrop


def _step(x):
    R = x['_RETURN_STACK']
    while R[-1] <= 0:
        x['_Python']['_rdrop'](x)
    R[-1] -= 1

a['_include'](a, _step)
del _step


def _rpush(x, words):
    R = x['_RETURN_STACK']
    R.append(words)
    R.append(len(words))

a['_include'](a, _rpush)
del _rpush


def _execute(x):
    '''Not to be confused with Forth { EXECUTE }.
    '''
    PY = x['_Python']
    PY['_step'](x)
    WORD = PY['opera'](x)
    D = x['_DICTIONARY']
    if WORD in D:
        D[WORD](x)
    else:
        PY['_push'](x, WORD)

a['_include'](a, _execute)
del _execute



# FLOW CONTROL I


def if_(x): # { IF }
    PY = x['_Python']
    if not bool(PY['drop'](x)):
        PY['_rdrop'](x) # DROP { IF }   ITSELF
        PY['_rdrop'](x) # DROP { IF }'S CALLER

a['_extend'](a, if_, 'IF', 'if_')
del if_


def ebb(x):
    '''Unconditionally jump to beginning of present
    (sub)routine.
    '''
    R = x['_RETURN_STACK']
    #  { EBB } ITSELF SHOULD HAVE BEEN DROPPED BY _step.
    R[-1] = len(R[-2])

a['_extend'](a, ebb)
del ebb


def execute(x): # { EXECUTE }
    PY = x['_Python']
    WORD = PY['drop'](x)
    if WORD in x['_DICTIONARY']:
        PY['_rpush'](x, (WORD,))
    else:
        PY['_push'](x, WORD)

a['_extend'](a, execute)
del execute



# STRINGS


def rest(x):
    PY = x['_Python']
    PY['_push'](x, PY['drop'](x)[1:])

a['_extend'](a, rest, "'", 'rest')
del rest



# THE DICTIONARY

def _extend_archive(x, key):
    if key not in x['_DICTIONARY']:
        return
    if key not in x['_ARCHIVE']['DICTIONARY']:
        x['_ARCHIVE']['DICTIONARY'][key] = []
        if key in x['_DATA']:
            x['_ARCHIVE']['DATA'][key] = []

a['_include'](a, _extend_archive)
del _extend_archive


def _archive(x, key):
    if key not in x['_DICTIONARY']:
        return
    PY = x['_Python']
    PY['_extend_archive'](x, key)
    x['_ARCHIVE']['DICTIONARY'][key].append(x['_DICTIONARY'].pop(key))
    if key not in x['_DATA']:
        return
    x['_ARCHIVE']['DATA'][key].append(x['_DATA'].pop(key))
    
a['_include'](a, _archive)
del _archive


def ddrop(x):
    D = x['_DICTIONARY']
    PY = x['_Python']
    PY['rest'](x)
    K = PY['drop'](x)
    if K in D:
        D.pop(K)
        DATA = x['_DATA']
        if K in DATA:
            DATA.pop(K)

a['_extend'](a, ddrop)
del ddrop



# OUTPUT


def echo(*args, prompt='1>> ', sep=' ', end='\n', file=1):
    from sys import stderr, stdout
    file = (None, stdout, stderr)[file]
    print(prompt, end='', flush=True, file=file)
    print(*args, sep=sep, end=end, flush=True, file=file)

a['_include'](a, echo)
del echo


def dot(x): #  { . } "DOT" (REMAPPED TO "?")
    print(x['_Python']['drop'](x))

a['_include'](a, dot)
a['_expand'](a, '?', 'dot')
del dot



# INPUT


def ok(x):
    '''Prompt user.
    '''
    PY = x['_Python']
    PY['echo'](*PY['_repr4'](x), '\nOK> ', prompt='S>>', end='')

a['_include'](a, ok)
del ok


def read(x):
    PY = x['_Python']
    In = x['_INPUTS']
    file = In[-1](x)
    if file is In[0](x):
        PY['ok'](x)
    PY['_push'](x, file.readline())
    if not PY['_top'](x):
        file.close()
        x['_INPUT_FILES'].pop()
        In.pop()

a['_extend'](a, read, '!:-', 'read')
del read


def load(x):
    PY = x['_Python']
    file = open(PY['drop'](x))
    x['_INPUT_FILES'].append(file)
    x['_INPUTS'].append(lambda x: x['_INPUT_FILES'][-1])

a['_extend'](a, load)
del load


def parse(string):
    string = string + ' '
    string = ''.join(map(lambda s: ' ' if s.isspace() else s, string))
    string = string.replace('\\ ', '\t')
    strings = filter(None, string.split(' '))
    strings = tuple(map(lambda s: s.replace('\t', ' '), strings))
    return strings

a['_include'](a, parse)
del parse


def query(x):
    PY = x['_Python']
    In = x['_INPUT_BUFFER']
    while not In:
        PY['read'](x)
        In.extend(PY['parse'](PY['drop'](x)))
    PY['_rpush'](x, (In.popleft(),))

a['_extend'](a, query)
del query



# THE CONSTANT COMPILER


def docon(x):
    PY = x['_Python']
    OP = PY['opera'](x)
    PY['_push'](x, x['_DATA'][OP])

a['_include'](a, docon)
del docon


def constant(x):
    PY = x['_Python']
    WORD = PY['drop'](x)
    PY['_archive'](x, WORD)
    x['_DICTIONARY'][WORD] = PY['docon']
    x['_DATA'][WORD] = PY['drop'](x)

a['_include'](a, constant)
a['_expand'](a, '=', 'constant')
del constant



# THE COLON COMPILER


def docolon(x):
    '''Push current WORD's definition onto the Return Stack.
    '''
    PY = x['_Python']
    OP = PY['opera'](x)
    PY['_rpush'](x, x['_DATA'][OP])

a['_include'](a, docolon)
del docolon


def colon(x):
    '''Start a new Dictionary entry.
    '''
    PY = x['_Python']
    WORD = PY['drop'](x)
    x['_WORD_UNDER_CONSTRUCTION'][0] = WORD
    PY['_archive'](x, WORD)
    x['_DICTIONARY'][WORD] = PY['docolon']
    x['_DATA'][WORD] = []

a['_include'](a, colon)
a['_expand'](a, ':', 'colon')
del colon


def backtick(x):
    PY = x['_Python']
    PY['rest'](x)
    TOKEN = PY['drop'](x)
    WORD = x['_WORD_UNDER_CONSTRUCTION'][0]
    x['_DATA'][WORD].append(TOKEN)

a['_include'](a, backtick)
a['_expand'](a, '`', 'backtick')
del backtick


def semicolon(x):
    WORD = x['_WORD_UNDER_CONSTRUCTION'][0]
    x['_DATA'][WORD] = tuple(reversed(x['_DATA'][WORD]))

a['_include'](a, semicolon)
a['_expand'](a, ';', 'semicolon')
del semicolon



# THE COLONSEMICOLON COMPILER  { :; }

def colonsemicolon(x):
    PY = x['_Python']
    WORD = PY['drop'](x)
    PY['_archive'](x, WORD)
    x['_DICTIONARY'][WORD] = PY['docolon']
    x['_DATA'][WORD] = tuple(reversed(PY['drop'](x).split()))

a['_include'](a, colonsemicolon)
a['_expand'](a, ':;', 'colonsemicolon')
del colonsemicolon



# THE CODE COMPILER

def docode(x):
    PY = x['_Python']
    PY['_push'](x, x['_DATA'][PY['opera'](x)](x))

a['_include'](a, docode)
del docode


def code(x):
    '''Define a word in terms of Python.
    '''
    PY = x['_Python']
    WORD = PY['drop'](x)
    STRING = PY['drop'](x)
    PY['_archive'](x, WORD)
    x['_DICTIONARY'][WORD] = PY['docode']
    x['_DATA'][WORD] = eval(STRING)

a['_extend'](a, code)
del code



# FLOW CONTROL II 


def _warm(x): # SYSTEM START-UP (WARM)
    x['_Python']['_rclear'](x)

a['_include'](a, _warm)
del _warm


def _cold(x): # SYSTEM START-UP (COLD)
    PY = x['_Python']
    PY['clear'](x)
    PY['_warm'](x)

a['_include'](a, _cold)
del _cold


def sail(x): # a.k.a "main"
    INTERRUPTING = {KeyboardInterrupt}
    PY = x['_Python']
    def maybeStop(e):
        if e in INTERRUPTING:
            PY['echo'](' Attention flag will reset.',
                prompt='', file=2, end='')
            x['_ATTN'][0] = False
            return True
        else:
            return False
    x['_ATTN'][0] = True
    while x['_ATTN'][0]:
        try:
            PY['_execute'](x)
        except:
            PY['echo'](x['_MI'], ' (id:', str(id(x['_SELF'])),
                ') caught exception.',
                prompt='2>> ', sep='', file=2, end='')
            from sys import exc_info
            e = exc_info()
            PY['_push'](x, e)
            maybeStop(e[0])
            INTERRUPT = '_defaultInterrupt'
            PY['echo'](' Flow will be interrupted by ', INTERRUPT, '.',
                sep='', prompt='', file=2, end='')
            if x['_ATTN'][0]:
                PY['echo'](prompt='', file=2)
            else:
                PY['echo'](' This node will sleep until called upon.',
                    prompt='', file=2)
            x['_Python'][INTERRUPT](x)

a['_include'](a, sail)
a['sail'] = a['_Python']['sail']
del sail


def z(x): # SLEEP / PAUSE: RETURN TO Python 3
    x['_ATTN'][0] = False

a['_extend'](a, z)
del z



# MISC.


def nop(x): # FOR TESTING, ETC.
    pass

a['_extend'](a, nop)
del nop



def exec_(x):
    exec(
        x['_Python']['drop'](x),
        eval(x['_EXTERNAL'])['globals'],
        x['_Python'])

a['_extend'](a, exec_, 'EXEC', 'exec_')
del exec_



def eval_(x):
    PY =x['_Python']
    PY['_push'](x, eval(
        PY['drop'](x),
        eval(x['_EXTERNAL'])['globals'],
        PY))

a['_include'](a, eval_)
a['_expand'](a, 'EVAL', 'eval_')
del eval_



def self(x):
    PY = x['_Python']
    PY['_push'](x, x['_SELF'])

a['_include'](a, self)
a['_expand'](a, 'SELF')
del self



def call(x):
    PY = x['_Python']
    function     =  PY['drop'](x)
    args, kwargs =  PY['drop'](x)
    PY['_push'](x, function(*args, **kwargs))

a['_extend'](a, call)
del call



def fimport(x):
    '''import a Python function;
    make a Python function available in Forth.
    '''
    PY = x['_Python']
    NAME     = PY['drop'](x)
    function = PY['drop'](x)
    NAME = NAME if NAME else getattr(function, '__name__')
    def inner(y):
        PY = y['_Python']
        args, kwargs = PY['drop'](y)
        PY['_push'](y, function(*args, **kwargs))
    x['_DICTIONARY'][NAME] = inner

a['_extend'](a, fimport)
del fimport



a['_Python']['_cold'](a)
