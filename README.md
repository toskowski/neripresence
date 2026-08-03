# Neripresence
**A tiny wrapper for the nerimity desktop app :3**

this readme will contain a few examples and explenations for neripresence

for suggestions or feedback please contact me on nerimity: @tosiek:tost

# Installation
To install neripresence you can use pip:

```pip install --upgrade neripresence```

... or download and install from [this github repo](https://github.com/toskowski/neripresence)

# Code examples:

A very simple example program to set a static presence and close it after any user input:
```python
import  neripresence  as  ns
import  time

client = ns.Client() #returns a client object

client.start() # starts a connection with nerimity

# sets a simple presence
client.push(action="Is playing",name="simple presence",title="nice title")

input("") # waits for user input to continue the program

client.close() # closes the connection

time.sleep(1) # waits for the connection to fully close before finishing the program
```

# Reference
To use neripresence you will need to create a Client() object:
`client = neripresence.Client()`
the client has 3 callable methods
