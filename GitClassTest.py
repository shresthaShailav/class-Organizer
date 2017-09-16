from github import Github
import unittest
from GitClass import GitOperations
import sys


Git_name = raw_input("GitHub Username")
Git_pass = raw_input("GitHub Password ")

repo_name = "test_repo"

print(Git_name)
print(Git_pass)

class Test_GitOperations(unittest.TestCase):
    
    def setUp(self):
        self.u_name = Git_name
        self.u_pass = Git_pass
        # Actual GitHub Object from API
        self.git = Github(self.u_name,self.u_pass)
        # My GitHub Object
        self.my_git_obj = GitOperations(self.u_name, self.u_pass)

    def test_create_repo(self):
        # assert that that a repository with the name repo_name does not exist 
        for repo in self.git.get_user().get_repos():
            self.assertFalse(str(repo.name) == repo_name)
        
        # create a new repo named repo_name
        self.created = self.my_git_obj.create_repo(repo_name)

        # assert that the repository now exists
        repo_names = [str(repo.name) for repo in  self.git.get_user().get_repos()]
        self.assertTrue(repo_name in repo_names)
        
        # delete the created test repo

    def test_delete_repo(self):
        # create a test repository with name repo_name
        # assert that a repository with name repo_name exist
        # delete repository
        # assert that the repository doesn't exist anymore
        self.fail("Not yet implemented")


if __name__ == "__main__":
        unittest.main()
