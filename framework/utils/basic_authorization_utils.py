from framework.models.get_request import GetRequest

from framework.utils.logger import info


def authorize(url, login, password):
    return GetRequest(url, (login, password)).request_result


def is_authorization_success(authorization_result, login):
    info("Checking that authorization was successful")
    success_answer = {"authenticated": True, "user": login}
    return authorization_result == success_answer
