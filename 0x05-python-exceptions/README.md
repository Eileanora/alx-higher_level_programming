<h1>Exception handling in python</h1>
<h3>Errors in general are divided into two categories:</h3>
<ol>
	<li> Syntax/parsing errors</li>
	<li> exceptions</li>
</ol>
<h3>What are exceptions?</h3>
Excetions are errors detected during exection, they are not unconditionally fatal.

Most exceptions are not handled by programs, however, and result in error messages and the termination of the program.

<h2>exception types</h2>

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
	<tr>
		<th>ZeroDivisionError</th>
	</tr>
	<tr>
		<th>NameError</th>
	</tr>
	<tr>
		<th>TypeError</th>
	</tr>
	<tr>
		<th>ValueError</th>
	</tr>
	<tr>
		<th>RuntimeError</th>
	</tr>
	<tr>
		<th>OSError</th>
	</tr>
    <tr>
        <th>ImportError</th>
    </tr>
    <tr>
        <th>IndexError</th>
    </tr>
</table>

## Handling exceptions
to handle exception we use the try except statment
```
try 
    #try clause here
except <exception name>
    #exception clause here
```
<h3>what does this statment do?</h3>
first, the try clause is executed
<ul>if no exception occurs, the except clause is skipped and only the try clause is executed.</ul>
<ul>if an exception occurs during the exection of the try clause, the rest of the try clause is skipped and the code moves to the except clause to execute it.</ul>

a try statment may have more than one exception clause
```
except(RuntimeError, TypeError, NameError)
```
the except clause may specify a variable after the exception name. The variable is bound to the exception instance which typically has an args attribute that stores the arguments. For convenience, builtin exception types define __str__() to print all the arguments without explicitly accessing .args.
```
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception type
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)
```
Note: The exception’s \__str__\() output is printed as the last part (‘detail’) of the message for unhandled exceptions.

The try except statment has also an else clause
```
try
    f = open(filename, 'r')
except OSError:
    print("cannot open", filename)
else
    print("file has toomany files")
    f.close()
```
so what happend here?
<ol>
    <li> we try to open the file and read it's content</li>
    <li> if opening the file raised an os error exception, do the except clause</li>
    <li> if it raised any exception other than the os error, or no exception at all, do the else clause</li>
</ol>
The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except statement.

## q
Exception handlers do not handle only exceptions that occur immediately in the try clause, but also those that occur inside functions that are called (even indirectly) in the try clause. For example:
```
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
```