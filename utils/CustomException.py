# Import the sys module to access system-specific parameters and functions (used here for exception info)
import sys

# Define a custom exception class inheriting from the built-in Exception class
class CustomException(Exception):
    # Initialize the exception with a specific error message and optional detailed error info
    def __init__(self, message: str, error_detail: Exception = None):
        # Generate the detailed error message using the helper method
        self.error_message = self.get_detailed_error_message(message, error_detail)
        # Call the parent class (Exception) constructor with the detailed error message
        super().__init__(self.error_message)

    # Define a static method to construct the detailed error message (doesn't need 'self')
    @staticmethod
    def get_detailed_error_message(message, error_detail):
        # Extract the exception type, value, and traceback object from sys.exc_info()
        _, _, exc_tb = sys.exc_info()
        # Get the filename where the exception occurred (if traceback is available)
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        # Get the line number where the exception occurred
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
        # Return a formatted string containing the custom message, original error, filename, and line number
        return f"{message} | Error: {error_detail} | File: {file_name} | Line: {line_number}"

    # Define the string representation of the exception
    def __str__(self):
        # Return the detailed error message when the exception is printed or converted to a string
        return self.error_message