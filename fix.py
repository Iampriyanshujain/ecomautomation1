# import pytest
#
#
# @pytest.fixture()
# def setup():
#     print("open the browser")
#     print("launch the webpage")  #pretask
#     print("maximize window")
#     yield
#     print("clock on login")
#     print("close the browser") #post task
#
#
# def test_login1(setup):
#     print("actual test case withn valid username and password")
#
# def test_login2(setup):
#     print("actual test case withn valid username and invalid password")
#
# def test_login3(setup):
#     print("actual test case withn invalid username and valid password")
#
# def test_login4(setup):
#     print("actual test case withn invalid username and invalid password")