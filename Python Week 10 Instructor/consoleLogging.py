# Logging
import logging

"""
"Critical"		Level 5	<-- Highest
"Error"			Level 4
"Warning"		Level 3
"Info"			Level 2
"Debug" 		Level 1 <-- Lowest
"""
# Configure the logging module
logging.basicConfig(
	level = logging.DEBUG, 
	filename = "errors.log",
	format = "%(levelname)s : %(asctime)s - %(message)s"
)

logging.critical("THIS IS A CRITICAL LEVEL MESSAGE!!!!")
logging.error("This is an Error Level message!!!!")
logging.warning("This is a Warning Level Message.")
logging.info("This is an Information Level Message.")
logging.debug("This is a debugging level message.")



# Print isnt always viable for debugging
# Print is mainly for the User
# print("This is an debug message.")
