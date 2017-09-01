from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
    
    
# Scope for modifying assignments and questions and the work and grades
SCOPES = 'https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/classroom.rosters https://www.googleapis.com/auth/classroom.coursework.students.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Classroom API Python Quickstart'




COURSE_ID = 7414258692 # !!! Change the COURSE ID!!! 
    
    
def main():
	""" Adds new assignment to the classroom only if all the students have completed the latest assignment"""
	# getting permissions and initializing object
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('classroom', 'v1', http=http)
	
	# initilize assignmet -> using list because modifying non local varialble is difficult in python2
	newAssignment = [True]
	
	
	# get list of all the students in the given courseId
	results = service.courses().students().list(courseId=COURSE_ID).execute()
	students = results.get('students', [])
	
	# get the assignment ID of the latest assignment
	# by default ordered by updatetime and descending. source: https://developers.google.com/classroom/reference/rest/v1/courses.courseWork/list.
	results = service.courses().courseWork().list(courseId=COURSE_ID,courseWorkStates="PUBLISHED").execute()
	assignment = results.get('courseWork', [])[0]
	

	for student in students:
		#get student profile
	    	profile= student['profile']
	    	print(profile['name']['fullName'])
	    	
	    	# get the student studentSubmssion object for the given assignment and the particular user
	    	results = service.courses().courseWork().studentSubmissions().list(courseId=COURSE_ID,courseWorkId=assignment['id'], userId=student['userId']).execute()
		studentSubmission = results['studentSubmissions'][0]
		
		# check if the student has submitted the assignment
	    	state = studentSubmission['state']
	    	if (state == "TURNED_IN" or state == "RETURNED"):
	    		print("The student {} has submitted the latest assignment {}".format(profile['name']['fullName'], assignment['title']))
	    	else:
	    		print("The student {} has NOT submitted the latest assignment {}".format(profile['name']['fullName'], assignment['title']))
	    		newAssignment[0] = False
	    		
	
	print("new assignment issuance state = {}".format(newAssignment[0]))
	
	# if all the students have submitted a new assignment, issue a new assignment
	if newAssignment[0] == True:
		courseWork = {
			'title' : 'New Assignment',
			'description' : 'added only if all the students have submitted latest assignment',
			'workType' : 'ASSIGNMENT',
			'state' : 'PUBLISHED'
			}
		courseWork = service.courses().courseWork().create(
			courseId=COURSE_ID, body=courseWork).execute()
		print("New assignment created")
		
	else:
		print("New Assignment not issued")
		


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    
    #return the argument with an initial component of ~ or ~user replaced by that user's home directory
    home_dir = os.path.expanduser('~')
    
    credential_dir = os.path.join(home_dir, '.credentials')
    
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
        
    
    credential_path = os.path.join(credential_dir,
                                   'classroom.googleapis.com-python-quickstart.json')

    # store and retrieve a single credential to and from a file
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
    
	 
		    	
		    	
if __name__ == '__main__':
	main()
