Project Report: Customtkinter Voting System Application

Goal of the Project 

The primary objective of this project is to develop a user-friendly voting system application using Python with the Customtkinter library. This application allows users to log in with different roles, choose candidates, and cast votes securely. The system is designed for easy administration of voting processes, allowing administrators to manage candidates and view voting results in real-time.

Significance of the Project 

The significance of this project lies in its ability to make the process of voting simple and easy within various settings, such as schools, small communities, or corporate environments. By digitizing the voting process, the application ensures transparency, accuracy, and security, significantly reducing the likelihood of fraudulent activities and human errors. The novel integration of Customtkinter provides a modern and customizable user interface, enhancing user experience and engagement.



Installation and Instructions to Use:

- Go to a terminal located on the bottom left corner of Pycharm and pip install customtkinter and matplotlib to begin using the program
  
- User Registration: If you're a new user, click on the "Register" button to create a new account. Enter your desired username, and password, confirm the password, and provide your email address. Click the "Submit" button to register.
  
- Login: After registration or if you already have an account, enter your username, and password, and select your role (User or Administrator) in the login interface. Click the "Login" button to log in.

- Candidate Selection: After logging in, you'll see a window displaying candidate options. Click on the candidate you want to vote for, and then click the "Vote" button to cast your vote.

- Simulation: The program allows you to simulate events that may influence voting behavior, such as gun murder, war, disease, or payment issues. Click on the "Simulation" button to access the simulation page and select the event you want to simulate.

- Admin Dashboard: If you log in as an administrator, you'll have access to an admin dashboard where you can view statistics, and user information, and perform simulations.
Exit the Program: Close the program window when you're done by clicking the close button or selecting the exit option from the menu.

Code structure in words

Import Statements:
    - Import necessary modules and libraries such as customtkinter, messagebox, json, os, random, and matplotlib.pyplot.

2. Class Definitions:
    a. UserData:
        - Methods:
            - __init__(self)
            - load_from_json(self, filename)
            - save_to_json(self, filename)
            - authenticate_user(self, username, password)

    b. Register (inherits from UserData):
        - Methods:
            - __init__(self, root)
            - open_registration(self)
            - submit_registration(self)

    c. VoteManager:
        - Methods:
            - __init__(self)
            - load_from_json1(self, filename)
            - save_to_json1(self, filename, data)
            - cast_vote(self, candidate, username)

3. Function Definitions:
    - on_login_pressed(): Handles the login button click event.
    - open_candidate_selection(username): Opens the candidate selection window.
    - open_admin_dashboard(username): Opens the admin dashboard window.
    - open_stats_page(): Opens the statistics page.
    - open_user_info_page(): Opens the user information page.
    - merge_sort(arr): Implements the merge sort algorithm.
    - display_vote_counts(): Displays the vote counts.
    - simulate_gun_murder_event(): Simulates a gun murder event.
    - simulate_War(): Simulates a war event.
    - simulate_disease(): Simulates a disease event.
    - simulate_payment(): Simulates a payment issue event.

4. Main Code:
    - Instantiates necessary objects such as UserData and VoteManager.
    - Creates the main GUI window using customtkinter.
    - Defines GUI elements such as entry fields, labels, buttons, etc.
    - Binds event handlers to GUI elements.
    - Runs the main event loop using the `root.mainloop()` method.

5. Exception Handling:
    - Try exception blocks for error handling.
  
   

Discussion and Conclusions

The project successfully demonstrates the application of Python programming and GUI development skills in creating a functional voting system.

Limitations: Currently, the system does not support large-scale candidates data also the program does not allows the administrator to add a new candidate. It lacks advanced security features for public elections like email more verification method, also there is improvement part for the GUI so the user can have a better experience. 

Conclusions:
Our program adeptly employs various data structures, including dictionaries and lists, to efficiently manage user data, candidate information, and voting records. Dictionaries serve as an organized repository for key-value pairs, facilitating swift access to essential data such as usernames and passwords. Meanwhile, lists offer a flexible means of storing and manipulating collections of items, such as aggregating votes for each candidate.

The integration of merge sort underscores our program's commitment to efficient sorting methodologies. By implementing merge sort, our program ensures not only stable and reliable sorting but also scalability, enabling seamless handling of increasingly larger datasets. This algorithm's time complexity of O(n log n) underscores its efficiency, contributing significantly to the program's overall performance.

Our program is further reinforced through strategic error handling, employing try/except blocks to gracefully manage exceptions that may arise during file operations. By preemptively addressing potential errors, such as file not found exceptions, our program maintains stability and resilience, ensuring a seamless user experience.

A standout feature of our  program is its innovative simulation methodology, which anticipates real-world scenarios and forecasts their potential impact on voting outcomes. By simulating events such as disease outbreaks or policy changes, our program provides valuable insights into how voting patterns might evolve under varying circumstances. This predictive modeling capability enhances the program's analytical depth, offering valuable perspectives on electoral dynamics and decision-making processes.

