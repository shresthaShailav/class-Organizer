import from_google_api
  
class classRoomOperations:
    def __init__(self):
        """ Gets the permission and initializes the classroom object as service""" 
        self.credentials = from_google_api.get_credentials()
        self.http = self.credentials.authorize(from_google_api.httplib2.Http())
        self.service = from_google_api.discovery.build('classroom', 'v1', http=self.http)

    def create_course(self, course_name):
         """ Creates a new course with name course_name and some other default parameters"""
         course = {
                 'name' : course_name,
                 'ownerId' : 'me',
                 'courseState' : 'PROVISIONED'
                 }
         course = self.service.courses().create(body=course).execute()
         return course

    def delete_course(self, course_name):
        """ Deletes the course with the given course name, 
            if muliple course name then deletes all the course with that course_name"""
        results = self.service.courses().list().execute()
        courses = results.get('courses', [])
        for course in courses:
            if (course['name'] == course_name):
                self.service.courses().delete(id=course['id']).execute()

    def invite_students(self, student_list):
        """ Invites all the students in the student list. 
            student_list is a dictionary that contains the student name and their email_id"""
        return None

    def update_assignment(self, course_id, assignment_file):
        """ Updates the assignment of the course if all the students have submitted the assignment"""
        return None
