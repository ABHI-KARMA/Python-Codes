# The code that can cause an exception to occur is put in the try block and the handling of the exception is implemented in the except block.
# The code in the except block will only execute if the try block runs into an exception.

# SINGLE ERROR HANDLING
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
	

# MULTIPLE ERROR HANDLING
# METHOD : 1 We can use three methods to handle multiple exceptions. The first one involves putting all the exceptions which are likely to occur in a tuple.
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))
	
# METHOR : 2 : to handle individual exceptions in separate except blocks. We can have as many except blocks as we want. Here is an
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    raise e
except IOError as e:
    print("An error occurred.")
    raise e

# METHOD : 3 This can be helpful when you have no idea about the exceptions that may be thrown by your program.
# If you are just looking to catch all execptions, but don't actually care about what they are, you can even exclude the Exception as e part.
try:
    file = open('test.txt', 'rb')
except Exception as e:
    # Some logging if you want
    raise e
