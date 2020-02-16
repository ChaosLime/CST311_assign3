# CST311_assign3
Austin Ah Loo <br>
Mikie Reed <br>
Mitchell Saunders <br>
Nicholas Saunders

Run Server, then run at least 2 instances of client
<br>

See Comments in within programs for setup

To be ran on Python 3

UPDATE:
To test scenarios under client-aa.py and server-aa.py, run as follows:

server-aa.py
python server-aa.py 8001 <enter>
  
client-aa.py (instance 1)
python client-aa.py 8001 X Bob <enter>
  
client-aa.py (instance 2)
python client-aa.py 8001 Y Alice <enter>
  
There should be the message received and displayed on the server, and the server will send back results to each client, to be displayed by the clients


We can tweak the messages and client input as needed...

UPDATE and NOTICE: <br>
Withn the "nick" directory, I am built and developed a 
<br>client server system that can connect any number of clients.
<br> Please advise. Still needs to return other clients inputs back to 
<br>the users, but it is pretty cool. Runs on python 3.

To use programs, you can run server.py plainly,<br>
for client.py use "python client.py X Bob" as an example.

Uses port 12000 on localhost currently.

UPDATE! Feb 15
Nick's directory has client that is now threaded, but there appears to some sort<br>
of infinite loop going on after some inputs. Not entirely sure what's up.
