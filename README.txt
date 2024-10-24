Project Description
This project is a graphical application for parking management, developed in Python using the Tkinter library for the graphical interface and PyMySQL for connecting to a MySQL database. The system allows for the registration of vehicle entries and exits, calculates parking costs, and checks space availability. It can also calculate the total amount paid by each vehicle and the parking lot's earnings over a specified time period.

Main Features
Vehicle Entry Registration: Allows the user to input the license plate and the date/time of a vehicle's entry into the parking lot. If the AUTOS table does not exist in the database, the system automatically creates it.

Vehicle Exit Registration: By entering the license plate and the date/time of exit, the system calculates the total duration of stay and the corresponding cost, updating the information in the database.

Total Amount Paid per Vehicle: Enables querying the total amount paid by a vehicle based on its license plate.

Checking Available Spaces: Provides information on how many parking spaces are available, assuming a total of 300 spaces.

Earnings Calculation: Allows for the calculation of total parking earnings per day, month, or year from a user-specified date.

Technologies Used
Python: Main programming language.
Tkinter: For creating the graphical interface.
PyMySQL: For connecting to the MySQL database.
MySQL: Database used to store vehicle information.

Run the main script to launch the graphical interface.

Usage Instructions:
Enter the license plate and the date/time to register vehicle entries and exits.
Use the buttons available on the interface to execute cost calculation and availability functions.