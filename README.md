# SendingEmails

A Python  app that I made for a coding challenge. The goal is to send out emails to 1 million entries  of recipients. The email procedure is
just a fake one, waiting for half a second. 

## What I learned

* Developed the generator.py, importing the Faker module, so I could generate one million fake email addresses to use as entries.
* In the reader.py, I implemented the csv and os module for reading the file and checking if it is empty.
* Used Thread objects (from threading module) to my solution and the option for the user to choose the number of threads that they are going
to be used. 