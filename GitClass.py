from github import Github
import sys
	

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
			    
