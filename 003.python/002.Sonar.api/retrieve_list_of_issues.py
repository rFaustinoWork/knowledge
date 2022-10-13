"""
Retrieves all issues identified by the sonar for the specified project.
Creates two output files for the main and test source code issues, 
"issues_main.csv" and "issues_test.csv".
The issues are selected according to the file name. All issues belonging 
to a file name ending in "Test.java" are considered test issues and are
written into the output test file "issues_test.csv". All other go to the
"issues_main.csv" file.
"""

import requests
import math

BASE_URL = "https://example.com"
PROJECT_NAME = "ProjectName"
BRANCH_NAME = "dev"
SSL_KEY = "2a3c27a600952ba5b0e83cf6ef8a63d89d3a4d8c"

MAX_ITEMS_PER_PAGE = 500

##############################################################################################################################
def build_url(nbPage, nbItemsPerPage):
   global PROJECT_NAME, BRANCH_NAME
   
   return BASE_URL+"/api/issues/search?componentKeys="+PROJECT_NAME+"&branch="+BRANCH_NAME+"&resolved=false&p="+str(nbPage)+"&ps="+str(nbItemsPerPage)

##############################################################################################################################
def write_to_file(f_handler, issue_data):
   f_handler.write(f"{issue_data['rule']};")
   f_handler.write(f"{issue_data['severity']};")
   f_handler.write(f"{issue_data['type']};")
   if 'line' in issue_data:
      f_handler.write(f"{issue_data['line']};")
   else:
      f_handler.write("all;")
   f_handler.write(f"{issue_data['component'][97:]};")
   f_handler.write(f"{issue_data['message']};")
   
   f_handler.write("\n")
   
##############################################################################################################################
def decode_json(f_handler_main, f_handler_test, json_data):
   issues = json_data['issues']

   for issue in issues:
      if issue['component'].endswith("Test.java"):
         write_to_file(f_handler_test, issue)
      else:
         write_to_file(f_handler_main, issue)

##############################################################################################################################
if __name__ == "__main__":
   
   if SSL_KEY == "":
      print("Auth key not defined.")
      exit(1)
      
   f_main = open("issues_main.csv", mode="w")
   f_test = open("issues_test.csv", mode="w")

   f_main.write("Rule;Severity;Type;Line;Component;Message;\n")
   f_test.write("Rule;Severity;Type;Line;Component;Message;\n")


   jsonData = requests.get(build_url(1, MAX_ITEMS_PER_PAGE), auth=(SSL_KEY, "")).json()
   decode_json(f_main, f_test, jsonData)

   total = math.floor(int(jsonData['total'])/MAX_ITEMS_PER_PAGE)
   for i in range(0, total):
      jsonData = requests.get(build_url(i+2, MAX_ITEMS_PER_PAGE), auth=(SSL_KEY, "")).json()
      decode_json(f_main, f_test, jsonData)


   f_main.close()
   f_test.close()

