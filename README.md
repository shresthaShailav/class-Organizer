# classroom_assignments
Add new assignment to google classroom only if all the students have completed the latest assignment


# libraries
pip install --upgrade google-api-python-client

# before proceeding with any of the script run the command: (deleting a .credential home in home directory if any)
rm -r ~/.credentials/ 

# Using the add_assignment.py script requires you to modify the COURSE_ID value within the SCRIPT
# use the list_course_ids.py script to determine the courseId and then modify COURSE_ID value in add_assignment.py script
