# import pytest
# class TestCalculator:
#     a=10
#     b=20
#     @pytest.mark.group_a
#     def test_add(self):
#         assert self.a+self.b<100, "is greater than 100"
#     @pytest.mark.group_b
#     def test_sub(self):
#         assert self.a-self.b == 0, "is not equals to zero"
#     @pytest.mark.group_a
#     @pytest.mark.group_b
#     @pytest.mark.group_c
#     def test_mul(self):
#         assert self.a*self.b == 200, "is equal to zero"
#     @pytest.mark.group_b
#     @pytest.mark.group_c
#     def test_div(self):
#         assert self.a/self.b !=0 ,"is eqaul to zero"
#     @pytest.mark.group_e
#
