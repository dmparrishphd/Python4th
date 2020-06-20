## From Words to Meaning

Once text is broken up into tokens, the tokens are processed in a certain order, according to a _grammar_.

### The Python Way

If you want to understand how Python does it, you'll have to read [5 pages of text](https://docs.python.org/3/reference/grammar.html) (1,349 words as of 2020-06-19). The first bit is:

    single_input: NEWLINE | simple_stmt | compound_stmt NEWLINE
    file_input: (NEWLINE | stmt)* ENDMARKER
    eval_input: testlist NEWLINE* ENDMARKER
    
    decorator: '@' dotted_name [ '(' [arglist] ')' ] NEWLINE
    decorators: decorator+
    decorated: decorators (classdef | funcdef | async_funcdef)
    
    async_funcdef: ASYNC funcdef
    funcdef: 'def' NAME parameters ['->' test] ':' [TYPE_COMMENT] func_body_suite
    
    parameters: '(' [typedargslist] ')'

That's right. The Python grammar is not written in English or in any other natural language! It's written in something like [Backus–Naur form](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form).

> This is madness!
> This is Python!

### The Forth Way

Here's Forth's gramar:

1. Tokens are processed in the order received.

That's it.

> This is sane.
> This is Forth.

([continue to next section](https://github.com/dmparrishphd/Python4th/blob/master/Doc/Why/whyDefs.MD))
