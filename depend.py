# import pytest
#
# c
#
# @pytest.mark.dependency
# def test_login():
#     assert True
#
# @pytest.mark.dependency(depends=["test_login"])
# def test_add_to_cart():
#     assert False
#
# @pytest.mark.dependency(depends=["test_add_to_cart"])
# def test_checkout():
#     assert True