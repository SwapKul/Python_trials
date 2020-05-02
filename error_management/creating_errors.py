class MyCustomError(TypeError):
    """
    Exception raised when a specific error code is needed.
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

#raise MyCustomError("Oops, there seems to be an error", 500)
err = MyCustomError("Oops, there seems to be an error", 500)
print(err.__doc__)
