from github import Github
import unittest
import sys
	
class GitOperations:
	
	def __init__(self, name, password):
	    self.git_object = Github(name, password)
            self.user = self.git_object.get_user()

	def create_repo(self, repo_name):
            """ Creates a new repository an returns a repository"""
            repo = self.user.create_repo(repo_name)
            return repo

        def delete_repo(self, repo_name):
            """ Deletes the repo_name if it exists in the repository"""
            repo = self.user.get_repo(repo_name)
            repo.delete()	    
