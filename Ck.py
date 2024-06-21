# Import necessary libraries
import pyximport
pyximport.install()

# Create a Cython file
mahadi = """
def reverse_string(str):
    return str[::-1]
"""

# Write the Cython code to a .pyx file
with open("reverse_string.pyx", "w") as f:
    f.write(mahadi)

# Compile the Cython file
import reverse_string

# Test the function
print(reverse_string.reverse_string("Hello, Cython!"))
