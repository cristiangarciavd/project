import requests
import sys
 
# setting path
sys.path.append('D:/JS/Api Testing/project')
from main.core.utils.json_reader import JsonReader
from main.core.api.http_methods import HttpMethods
from json import JSONDecodeError

class RequestManager():
    """Request Manager Implementation
    """
    
    __instance = None
    
    def __init__(self):
        """RM Parameters

        Args:
            conf_file (str, optional): Path to file. Defaults to "".
        """
        
        self.__config = JsonReader().get_json("./configuration.json")
            
        __environment = JsonReader().get_json('./environment.json')
        
        selected_env = self.__config.get("environment", "test")
        self.__users = __environment.get(selected_env).get("users")
        self.url = __environment.get(selected_env).get("api-url")
        self.key = self.__users.get("admin").get("key")
        self.token = self.__users.get("admin").get("token")
        self.response = None
        self.headers = {"Accept": __environment["headers"]}
        self.query = {
            'key': self.key,
            'token': self.token
        }
        
    @staticmethod
    def get_instance():
        """Get instance of the RequestManager class
        """
        if RequestManager.__instance is None:
            RequestManager.__instance = RequestManager()
        return RequestManager.__instance
        
    def make_request(self, http_method, endpoint, payload=None, **kwargs):
        """Send request

        Args:
            http_method (str): Http request method
            endpoint (str): endpoint route
            payload (_type_, optional): data. Defaults to None.

        Returns:
            _type_: Response Json , Response status code
        """
        self.query.update(kwargs)

        self.response = requests.request(
                                        method=HttpMethods[http_method.upper()].value,
                                        url=f"{self.url}{endpoint}",
                                        headers=self.headers,
                                        params=self.query,
                                        data=None if payload is None else payload
                                        )
        try:
            return self.response.json(), self.response.status_code
        except JSONDecodeError:
            current_response = {"response": self.response.text}
            return current_response, self.response.status_code