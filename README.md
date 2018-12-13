### VAR is an awesome Turing complete programming language!

Usage:      [Python 3 path] var.py [FILE]

Example:    c:\Python34\python.exe var.py test.var

Or if you have added the Python directory to your PATH variable, simply: python3 var.py test.var

Code examples can be find at the bottom of this page

### Statements
-   Takes up one line of code
-   Consists of one, two or three parts. 
-   Is in the form: Command [ Variable [ Value ] ]

### Data types
-   Integers
Examples: 1, 5, 42
-   Strings
Examples: “This is a string”, “123”

### Variables
-   Can (only) contain alphabetical and numeric characters (a-z, A-Z, 0-9)
-   Can not only contain integers
-   Could either stand alone ( a ) or be indexed ( a[3] or a[b] ). 

### Values
-   A value is either a string, an integer or a variable.

### Comments
-   Starts with //
-   Is ignored by the interpreter

### Commands (summary):
-   VAR: Assigns a variable.
-   INP: Reads input from the user.
-   OUT: Prints output to the user.
-   WHL: Branches the code reading to after the corresponding END command, if the variable does not equal 0.
         Else, enter the following code block until variable is 0. 
-   CON: Branches the code reading to after the corresponding END command, if the variable does not equal 0.
         Else, enter the following code block once.
-   END: End of code block. 
-   INC: Increments a variable.
-   DEC: Decrements a variable.

### VAR

Form: Command + Variable + Value

Description: Assigns a variable

Examples: 
```
VAR a “Hello”
VAR a 5
VAR a b
```

### INP

Form: Command + Variable

Description: Reads input from the user.

Examples: 
```
INP a
```

### OUT 

Form: Command + Value

Description: Prints output to the user.

Examples: 
```
OUT a
OUT “Hello”
```

### WHL

Form: Command + Variable

Description: Branches the code reading to after the corresponding END command, if the variable does not equal 0.
Else, enter the following code block until variable is 0.

Examples: 
```
WHL a
    // Stuff
END
```

### CON 

Form: Command + Variable

Description: Branches the code reading to after the corresponding END command, if the variable does not equal 0.
Else, enter the following code block once.

Examples: 
```
CON a
    // Stuff
END
```

### END

Form: Command

Description: End of code block. 
If preceded by WHL: Branches the code reading back to the corresponding WHL command.
If preceded by CON: Do nothing.

Examples:
```
END
```

### INC

Form: Command + Variable (+ Value)

Description: Increments a variable.

Examples:
```
INC a
INC a 5
INC a b
```

Notes: 

- Variables cannot be incremented by a string. 

- If no value is given, value 1 (integer) is assumed.

### DEC 

Form: Command + Variable (+ Value)

Description: Decrements a variable.

Examples: 
```
DEC a
DEC a 5
DEC a b
```

Notes: 

- Variables cannot be decremented by a string. 

- If no value is given, value 1 (integer) is assumed.

### INT 

Form: Command + Variable

Description: Converts a variable value from a string to an integer, if possible. 

Examples: 
```
INT a
```

### STR 

Form: Command + Variable

Description: Converts a variable value from an integer to a string, if possible. 

Examples: 
```
STR a
```

### Example programs

Hello World! program:
```
OUT "Hello World!"
```

Cat program:
```
INP a
OUT a 
```

Reverse string program:
```
VAR a "Hello, World!"
VAR index 0

WHL a[index]        // When index is equal to the length of a, then a[index] will return 0 and looping will stop
    INC index
END

WHL index           // Index starts at 13 and decrements by 1 every iteration
    DEC index
    OUT a[index]
END
```

If-else program:
```
INP a               // User inputs boolean value (1 = true, 0 = false)
INT a               // Treat a as an integer, not a string
VAR not_a 1         // Assume that "not a" is true, change in next step if incorrect

CON a               // Set "not a"
    VAR not_a 0  
END                 

CON a               // If
    OUT "True"
END
CON not_a           // Else
    OUT "False"
END
```

Program using most commands:
```
OUT "Enter your favorite number: "  // Print string to the user
INP fav_num                         // Store user input in variable (string) fav_num
INT fav_num                         // Convert the string fav_num to an integer, if possible
VAR counter 1                       // Assign 1 to variable counter

WHL fav_num                         // As long as fav_num does not equal 0, enter the following code block
    OUT "Counting: "                // Print string to the user
    STR counter                     // Convert the integer counter to a string
    OUT counter                     // Print counter value to the user
    INT counter                     // Convert the string counter back to an integer
    OUT 10                          // Print new line (ascii 10 = new line)

    INC counter 1                   // Increment counter by 1
    DEC fav_num 1                   // Decrement fav_num by 1
END                                 // Jump back to the corresponding WHL command on line 6
```
