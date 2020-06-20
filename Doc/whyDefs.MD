## From Meaning to Functionality

Both Python and Forth can be used to add functionality to the basic system. One way to do this is with definitions.

### The Python Way

This is just about the simplest definition you can write in Pytyon:

    def doNothing():
        pass
        
In other words, it requires seven symbols {`def`}{`doNothing`}{`(`}{`)`}{`:`}{`<indentation>`}{`pass`} to make a defintion that does nothing (except waste time). And, yes I count `<indentation>` as a symbol, because it is required by the Python grammar.

**Python requires invisible symbols!**

### The Forth Way

You can write a defintion that does nothing in Forth using only three symbols:

    doNothing : ;
    
Discounting the name, _Python is three times more wasteful_ than Forth (6 symbols vs. 2) in this case.
    
([continue to next section](https://github.com/dmparrishphd/Python4th/blob/master/Doc/whyPython.MD))
