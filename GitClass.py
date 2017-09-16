from github import Github
import unittest
import sys
	


class Test_github_object(unittest.TestCase):
	def setUp(self):
		u_name = sys.argv[1]
		u_pass = sys.argv[2]

	def test_repo(self):
		self.assertTrue(1==1)

	def test_repo2(self):
		self.assertFalse(1==5)


class GitOperations:
	
	def __init__(self, name, password):
	    self.git_object = Github(name, password)
            self.user = self.git_object.get_user()

	def create_repo(self, repo_name):
            """ Creates a new repository an returns a repository"""
            return False
                
        def delete_repo(self, repo_name):
            """ Deletes the repo_name if it exists in the repository"""
            return False


if __name__ == "__main__":
	unittest.main()
			    
