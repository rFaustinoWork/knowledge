"""
Access to git repository via python
"""
import os
from git import Git

# repository path
repo_path = 'c:/001.Projects/007.Siemens.ILTIS/02.repo/implementation/'
conf_rel_path = 'IIA/src/test/java/com/criticalsoftware/ibccommunicator'



git_repo = Git(repo_path)

for (root,dirs,files) in os.walk(os.path.join(repo_path,conf_rel_path), topdown=True):
   for file in files:
      if "TC_" in file:
         log = git_repo.log('--pretty=%an', os.path.join(root, file))         
         print(file, " -> ", log)






# print(log)
   
   
   
   
   