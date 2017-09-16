import unittest
import from_google_api
from ClassRoomClass import classRoomOperations
course_name = "test_course"

class Test_classRoomOperations(unittest.TestCase):

    def setUp(self):
        self.crObject = classRoomOperations()
        self.credentials = from_google_api.get_credentials()
        self.http = self.credentials.authorize(from_google_api.httplib2.Http())
        self.service = from_google_api.discovery.build('classroom', 'v1', http=self.http)

    
    def test_create_course(self):
        # assert that the course with the name course_name does not exist
        results = self.service.courses().list().execute()
        courses = results.get('courses', [])
        for course in courses:
            self.assertFalse(course['name'] == course_name)


        # create a course named course_name
        new_course = self.crObject.create_course(course_name)
        if (new_course != None):
            c_id = new_course['id']

        # assert that the course with the course_name exists
        results = self.service.courses().list().execute()
        courses = results.get('courses', [])
        course_list = []
        for course in courses:
            course_list.append(course['name'])
        self.assertTrue(course_name in course_list)
        
        # delete the created course
        if (new_course != None):
            self.service.courses().delete(id=c_id).execute()

    def test_delete_course(self):
        # create a test course with name course_name
        new_course = self.crObject.create_course(course_name)

        # assert that the course with name course_name exists
        results = self.service.courses().list().execute()
        courses = results.get('courses', [])
        course_list = []
        for course in courses:
            course_list.append(course['name'])
        self.assertTrue(course_name in course_list)

        # delete the course 
        self.crObject.delete_course(course_name)

        # assert that the course with name course_name does not exist anymore        
        results = self.service.courses().list().execute()
        courses = results.get('courses', [])
        for course in courses:
            self.assertFalse(course['name'] == course_name)

    def test_invite_students(self):
        # to implement
        self.fail("Not yet implemented")

    def test_update_assignment(self):
        # to implement
        self.fail("Not yet implemented")

if __name__ == "__main__":
    unittest.main()







 
