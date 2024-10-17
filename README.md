I decided to make A repository for some things I learned at devry in CEIS150 - Programming with objects. This repository deals with module 7 lesson 2.


listprocessing.py: 

In the first for loop, we are displaying the list using the index value or position within the list. Remember that index values start at 0.

In the second for loop, we display the list using the elements in the list rather than using the index. This is useful information.


iterator.py:

Iterators are objects with a collection of items. Iterators use the next() function to return the next value in the list. Iterators only let you go forward through the items one at a time. You can't go backwards or pick a specific item.

Here, we start with our simple shopping list. We use the iter() function which return an iterator.

In our for loop we use the next() function to get the next value in the list.

Although this is a simple case, you can add iterators to your own classes to make it easy to get the next item.


fib.py:

Creating Iterators
You can add an iterator to your class using the special __iter__() method along with the __next__() method.

Using the __iter__() method that returns self will add the iterator to your class.

You define what you want to return as the next item in the __next__() method.

Here, we have implemented a simple class which will produce the Fibonacci sequence. The Fibonacci sequence starts with 0, 1, and each subsequent number is the sum of the previous two numbers. So the sequence begins:

0, 1, 1, 2, 3, 5, 8, 13, and so on.

In this simplified example, we do not display the initial two numbers, starting with the first generated number.


lists.py:

Python supports several types of collections that can be used to store multiple values.

Lists - ordered, changeable, allows duplicates
Tuples - ordered, unchangeable, allows duplicates
Sets - unordered, unindexed, no duplicates
Dictionaries - unordered, changeable, indexed, no duplicates
You have already seen lists but we'll review them here.

This is a simple program that lets the user search for a job description and display the matching employee. We'll use parallel lists to store the data. First, we create the lists for employee names and job descriptions.

We then prompt the user for a job position they want to find.

We use a for loop to search through the jobDescription list. When the position is found, it looks in the same position in the employee list to display the name of the employee.

I created a better file for this code. It is under suggestedNewLists.py


fibgen.py:

Another way to work with sequences of values is by using a generator. A generator is a special type of function that can return a value then continue running at the next statement the next time the function is called rather than returning to the beginning of the function.

Generators use the yield statement instead of the return statement. Using the yield statement is what turns a regular function into a generator. Like return, yield will send a value back to the calling statement. However, the state of the function is maintained so that it can continue running from where it left off the next time it's called.

We see here a generator-based example of our simplified Fibonacci number program. In this example, we have a while loop inside the generator that computes the next Fibonacci number. We then use the yield statement to return the value and pause the generator. On the next call, the generator resumes at the line after the yield statement and continues with the loop.

Sadly enough, DeVry's code from fibgen.py does not display the fibonacci sequence. However, I have provided a file called suggestedFibGen.py that does.


dictionary.py:

Another type of collection supported by Python is the dictionary. A dictionary is a key-value collection. Each value in the list has an associated key, which makes it easy to locate. With a dictionary, the key is similar to the index in a list and each key can only appear once (just as each index value can only appear once in a list).

Here, we have simplified our employee job description program using a dictionary. The key represents the job description and the value represents the employee name. The list is contained within braces {} with keys and values separated by a colon.

To access a position in the dictionary, we use the key rather than an index. For example

personnel[searchPosition]
We can update values as well. For example

personnel[searchPosition] = "James Smith"


gui.py:

Python has many libraries that can be used to create GUI-based programs. Tkinter is a popular one that is installed in most Python distributions. Tkinter is an interface to the Tcl/Tk GUI toolkit. This toolkit is cross platform, so your GUI applications will work on Windows, Mac, or Linux.

Python also supports popular GUI frameworks such as Gtk, Qt, and wxWidgets. There are many other frameworks that can be used, both cross-platform, as well as those specific to a particular platform, such as Mac, Windows, or Android.

Here, we have the code for our simplified Tip Calculator. It may seem complex at first, but most of the code is simply setting up the various items on the form and positioning them.

Let's take a more detailed look at the code.

In the first part of our code (lines 1-9), we are importing tkinter and setting up the Window class that will represent.

Our constructor (__init__()) creates three Tkinter objects to hold the data we'll use in the calculations (service level, bill amount, and tip amount). We use these Tkinter data types rather than the standard string or float data types because they can be bound to the objects on our form.

We then call the Frame constructor, which is in the tkinter library.

Finally, we call our init_window() method, which creates the form design, including the title and objects such as labels, text entry boxes, buttons, and so forth.

The next two functions, calcTip() and client_exit(), are the event handlers. When we created the buttons we specified these functions as the command to execute when the button is clicked.

calcTip() uses the billAmountText and serviceLevel objects we created in the constructor. We convert the values to float so we can use them in the calculation. Once we have the tip, we format it as currency and use the tipAmountText object, which is bound to the corresponding widget on our form to display the results.

The main program is short. It creates a new Tk object called root. Then we specify the size of the form and create a new Window. Finally, we run the mainloop(), which will process the form and its events until the program is closed.

This part of our code (lines 10-37) controls the look and feel of our application.

We start by setting the text on the title bar to "Tip Calculator." The pack() function organizes the widgets and places them in the window.

Next, we add a main menu using the Menu object. We add a File menu to the main menu, and we add an Exit command to the File menu.

We then add a place for the user to enter the bill amount. This includes a label and an entry box. Note the x and y positions for the controls. The x position indicates how many pixels from the left side, and the y position indicates how many pixels from the top. In our Entry object, we bind it to the billAmountText object we created earlier. This makes it easy to set or get the value from the Entry box on the screen.

We use the same technique to add the other elements to the form. Note that with the calcButton and quitButton, we have assigned commands. These are the functions that will run when the user clicks the button or triggers an event in our event-driven programming model.
