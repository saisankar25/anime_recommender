# Import the logging module to handle log creation and management
import logging
# Import the os module to interact with the operating system (e.g., file paths, directories)
import os
# Import datetime to timestamp the log files
from datetime import datetime

# Define the directory name where logs will be stored
LOGS_DIR = "logs"
# Create the logs directory if it doesn't already exist
os.makedirs(LOGS_DIR, exist_ok=True)

# Generate a log file name based on the current date (YYYY-MM-DD format) inside the logs directory
LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure the basic settings for the logging system
logging.basicConfig(
    # Set the filename where logs will be written
    filename=LOG_FILE,
    # Define the format of the log messages: Timestamp - Log Level - Message
    format='%(asctime)s - %(levelname)s - %(message)s',
    # Set the default logging level to INFO (captures INFO, WARNING, ERROR, CRITICAL)
    level=logging.INFO
)

# Define a function to retrieve a specific logger instance by name
def get_logger(name):
    # Get the logger instance with the specified name
    logger = logging.getLogger(name)
    # Explicitly set the logging level to INFO for this logger
    logger.setLevel(logging.INFO)
    # Return the configured logger instance
    return logger