# HOLISTIC-STUDENT-DEVELOPMENT-SYSTEM

#DESCRIPTION OF MY PROJECT

#I have designed a Holistic Student Development System. The students from class 9 to 12 need to show case an all-round development of themselves to the school authorities. Contributing to different activities other than academics lead them to get additional credits to their overall score in the school. Such credits can be used by the school to share further opportunities like positions in the student council, providing scholarships etc.
#The system design has been done using the python tkinter and SQL server in the backend. Tkinter is the only framework that's built into the Python standard library.
#The design of the program involves general user registration, additional registrations as admin, student, and teacher.   In addition, the user also can reset their password. The admin user can update the contact details of the students, marks etc. The student can login to the relevant class and update their question responses and see their scores. The teachers have the ability to search for student scores based on the class.

#Now we walk through the different scenarios

#Standard User Creation
#1.	We are creating a standard user to the system. We have put basic validation on the phone number for 10 digits, but we can put additional validations also
#2.	The user as you can see now is registered in the sql table in the back end. Please note the password
#Password Reset
#1.	In case the password is lost, you can reset the password with the previous information like first , last name and phone number
#2.	We can now log in using the new password
#Additional role as Admin
#1.	We have now used the earlier created user and password and login as an Admin
#2.	Once you have logged in you can now update as student profiles with 
#3.	Add/ Select and Update/ Delete/ Reset all data and Logout from the screen
#4.	The Data can be seen below for on the same screen with scroll bar enabled for ease
#Now let us look at the student roles
#Additional role as Student
#	We have now used the earlier created user and password and login as a student
#1.	In the landing screen you enter the registered name, age, and relevant class
#2.	In the questionnaire screen we have 10 questions that need to be answered. A confirmation will give you 100 points else you have none
#3.	Once you submit the total score is now shown and the score is saved in the back end
#4.	Additional role as Student
#Additional role as teacher
#1.	Once you login as the teacher, you can now choose your class
#2.	The class report will show the total scores for all the students
#3.	On pressing save the report is saved on the desktop for review
