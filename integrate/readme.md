In this integration part we are testing using a simple example
Here above u can see the simple calculator gui with following files
1.index.html
2.design.css
3.logic.js

We can simply view the gui by clicking on the index.html file but it is not sufficient to us 
We need to publish this in any site So that we can communicate with it using it's IP address.
So here we are publishing our GUI in the localhost(internal IP).

We are using Python which makes a normal HTTP sever so publish our index.html on localhost
server.py file creates our server.

Then to move the mouse pointer we are using another click.py file which will open the browser and and move the mouse co-ordinates and perform operations like click ,etc.,

Now we want to run both the server.py and click.py for integration of our software
so open a terminal in the folder containing above files and execute
```
python click.py & python server.py
```
u can see the result in https://drive.google.com/file/d/1mrCkr6TGo3NJhMQi3MiT8aq75q6HOyRW/view
