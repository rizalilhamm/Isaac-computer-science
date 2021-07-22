# Exception Handling
An exception is an exceptional or unexpected event that occurs when a program is running.

Exception handling refers to the way that a program handles exceptional circumstances. It is really important that, when an exception occurs, a program does not just 'crash'. This will always be a problem for the end user as it will prevent them from completing the task in hand.

Consider a game that keeps a high score table in a text file. When the user plays the game, the text file is opened and the high scores are read from the file and displayed. Now consider what will happen if the text file has been accidentally deleted, moved, or renamed. These are situations that could definitely occur and need to be handled. However, there are other less common things that could prevent the file being read (for example the file may be locked or corrupted). Trying to predict all possible situations would be difficult and could result in a rare event being missed.

Fortunately, most programming languages have a code construct that will allow an exception to be handled smoothly. It requires you to write an exception handler that will be called and run when an exception is encountered. The basic concept is that, when an exception occurs, program flow is transferred to a handler that deals with the problem in the best way possible. Once the exception has been dealt with, normal program flow resumes.

Here is example using python: 
* [Python - Exception handling](https://docs.python.org/3/tutorial/errors.html)
* [JavaScript - Exception handling](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)