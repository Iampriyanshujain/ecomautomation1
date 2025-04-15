# import pytest
#
# @pytest.fixture(scope="class")
# def setup():
#     print("open the browser")
#     print("launch the browser")
#     print("maximize window")
#     yield
#     print("click on login")
#     print("close the browser")
# @pytest.mark.usefixtures("setup")
# class TestCase:
#
#     def test_login1(self):
#         print("you should enter the username,password and click on login button")
#
#     def test_login2(self):
#         print("you should enter the username,invaild password and click on login button")
#
#     def test_login3(self):
#         print("you should enter the invalid username,valid password and click on login button")
#
#
#     @pytest.mark.usefixtures("setup")
#     def test_login4(self):
#         print("you should enter invalid username ,password and click on login button")