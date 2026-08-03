# Neripresence
**A tiny wrapper for the nerimity desktop app :3**

this readme will contain a few examples and explenations for neripresence

for suggestions or feedback please contact me on nerimity: @tosiek:tost

# Installation
To install neripresence you can use pip:

```pip install --upgrade neripresence```

... or download and install from [this github repo](https://github.com/toskowski/neripresence)

# Code examples:
**code examples that will help you get started**

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

The Client has 3 methods:
```Client.start()```
```Client.push()```
```Client.close()```

## Client.start()
This method starts a websocket on another thread that listens for data from ```Client.push()``` .

## Client.push()
This method sets the presence to given data, all data fields are supported.

as per [nerimity docs](https://docs.nerimity.com/rpc) only the `name` argument is required and the rest can be omitted.

```ts
{
  name: 'UPDATE_RPC',
  data: {
    name: string;
    link?: string;
    action?: string;
    title?: string;
    subtitle?: string;
    imgSrc?: string;
    startedAt?: number;
    endsAt?: number;
  }
}
```
`TODO SCREEN Z WSZYSTKIMI WARTOSCIAMI`
TODO dodać opcję żeby wysłać puste dane client.clear() ????

notable arguments:

`link` - is the link that the user gets redirected to when clicking the title
`imgSrc` - should be a valid link to an image
`startedAt`/`endsAt` - used for displaying a bar showing the time progress of the presence, both values need to be **unix timestamp in miliseconds**

## Client.close()
This method is used to close the connection and free the socket

Good practice is to always make sure that the connection is properly closed before stopping the program, as that could lead to some connection issues later on.
