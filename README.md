VAR is an awesome programming language!


Usage:      [Python 3 path] var.py [FILE]

Example:    c:\Python34\python.exe var.py test.var




Or if you have added the Python directory to your PATH variable, simply:

python3 var.py test.var





Statements

-   Takes up one line of code

-   Consists of one, two or three parts. 

-   Is in the form: Command [ Variable [ Value ] ]



Data types (2):

-   Integers

Examples: 1, 5, 42

-   Strings

Examples: “This is a string”, ‘This is a string too!’, “123”



Variables

-   Can (only) contain alphabetical and numeric characters (a-z, A-Z, 0-9).

-   Can not only contain integers (?)

-   Could either stand alone ( a ) or be indexed ( a[3] or a[b] ). 

-   



Values

-   A value is either a string, an integer or a variable.



Commands (summery):

-   VAR: Assigns a variable.

-   INP: Reads input from the user.

-   OUT: Prints output to the user.

-   WHL: Branches the code reading to after the corresponding END command, if the following variable evaluates to 0. 

-   END: End of while loop. Branches the code reading back to the corresponding WHL command. 

-   INC: Increments a variable.

-   DEC: Decrements a variable



Commands (7):

-   Syntax: VAR

Form: Command + Variable + Value

Description: Assigns a variable

Examples: VAR a “Hello”, VAR a 5, VAR a b



-   Syntax: INP

Form: Command + Variable

Description: Reads input from the user

Examples: INP a




-   Syntax: OUT 

Form: Command + Value

Description: Prints output to the user.

Examples: OUT a, OUT “Hello”


-   Syntax: WHL

Form: Command + Variable (+ Value)

Description: Branches the code reading to after the corresponding END command, if the variable does not equal the value.

Examples: WHL a

Notes: 

If no value is given, value 0 (integer) is assumed.



-   Syntax: END

Form: Command

Description: End of while loop. Branches the code reading back to the corresponding WHL command.

Examples: END



-   Syntax: INC

Form: Command + Variable (+ Value)

Description: Increments a variable.

Examples: INC a, INC a 5, INC a b

Notes: 

Variables cannot be incremented by a string. 

If no value is given, value 1 (integer) is assumed.



-   Syntax: DEC 

Form: Command + Variable (+ Value)

Description: Decrements a variable.

Examples: DEC a, DEC a 5, DEC a b

Notes: 

Variables cannot be decremented by a string. 

If no value is given, value 1 (integer) is assumed.



-   Syntax: INT 

Form: Command + Variable

Description: Converts a variable value from a string to an integer, if possible. 

Examples: INT a

Notes: 



-   Syntax: STR 

Form: Command + Variable

Description: Converts a variable value from an integer to a string, if possible. 

Examples: STR a

Notes: 





Example programs:



Hello World! program:

OUT "Hello World!"



Cat program:

INP a

OUT a



Program using all commands:

OUT "Enter your favorite number: "  // Print string to the user

INP fav_num                         // Store user input in variable (string) fav_num

INT fav_num                         // Convert the string fav_num to an integer, if possible

VAR counter 1                       // Assign 1 to variable counter



WHL fav_num                         // As long as fav_num does not equals 0, enter the following code block

OUT "Counting: "                // Print string to the user

STR counter                     // Convert the integer counter to a string

OUT counter                     // Print counter value to the user

INT counter                     // Convert the string counter back to an integer

OUT 10                          // Print new line (ascii 10 = new line)



INC counter 1                   // Increment counter by 1

DEC fav_num 1                   // Decrement fav_num by 1

END                                 // Jump back to the corresponding WHL command on line 6







