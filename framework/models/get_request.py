import requests


class GetRequest:
    def __init__(self, url, credentials=None, parameters=None):
        self.__request_result = requests.get(url, auth=credentials, data=parameters)

    @property
    def request_result(self):
        return self.__request_result.json()
