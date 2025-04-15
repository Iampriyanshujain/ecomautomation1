# import pytest
#
#
# class TestCalculator:
#     a=10
#     b=7
#
#     @pytest.mark.skip(reason = "add method is working fine")
#     def test_add(self):
#         assert self.a+self.b != 0, "is equal to zero"
#
#     @pytest.mark.skipif(b==0,reason="denominator should not to be zero")
#     def test_div(self):
#         assert self.a/self.b
#     #
#     @pytest.mark.xfail(reason="result will be 3")
#     def test_sub(self):
#         assert self.a-self.b == 5, "the result is not equal to 5"