import requests
import json 
"""
    TODO before writing code:
    Briefly over backend doc: https://studybuddies.atlassian.net/wiki/spaces/SB/pages/131134/Backend+documentation+for+refactoring+server+index.js
    Read up on RESTFUL apis 
    Read up on requests module: https://www.nylas.com/blog/use-python-requests-module-rest-apis/#:~:text=How%20to%20Use%20Python%20Requests%20with%20REST%20APIs,-Now%2C%20let's%20take&text=The%20GET%20method%20is%20used,function%20to%20do%20exactly%20this.&text=The%20response%20object%20contains%20all,headers%20and%20the%20data%20payload.
"""
class apiRequests:
    
    def __init__(self, url):
        self.url = url
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    
    # Helper method for making a POST request 
    def post_request(self, endpoint, post_body):
        return requests.post(
            self.url + endpoint, 
            data = json.dumps(post_body),  
            headers=self.headers
        )
    
    def sign_up_user(self, email, password):
        post_data = {'email': email, 'password': password}
        endpoint = '/api/signup/users'
        request = self.post_request(endpoint, post_data) 
        # output for testing for now
        status = "Successfully" if request.status_code == 200 else "Failed"
        print( f"{status} signed up user with email: {email} and password {password} ") 
    
    def log_in_user(self, email, password):
        post_data = {'email': email, 'password': password}
        endpoint = '/api/login/users'
        request = self.post_request(endpoint, post_data) 
        # output for testing for now
        status = "Successfully" if request.status_code == 200 else "Failed"
        print( f"{status} logged in user with email: {email} and password {password} ")

    """
    TODO: make more functions like the ones above of the endpoints in our index.js file
    Here is where you can see the endpoints, expected status codes, etc:
    https://studybuddies.atlassian.net/wiki/spaces/SB/pages/131134/Backend+documentation+for+refactoring+server+index.js
    """
    


def main():
    api = apiRequests("http://localhost:5000")
    # test your functions here 
    # api.sign_up_user("tester1234@tester.com", "testerPassWord1234")
    api.log_in_user("tester1234@tester.com", "testerPassWord1234") 

if  __name__ == '__main__':
    main() 

        