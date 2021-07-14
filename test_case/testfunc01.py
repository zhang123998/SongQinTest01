import pytest
import os
import allure


@allure.feature('登录模块')  # 一级标签
class TestLogin:
    def setup_class(self):
        print('--执行测试类之前，我需要执行的操作')

    @allure.story('登录login01')  # 二级标签
    @allure.title('login01')
    @pytest.mark.parametrize('a,b', [(1, 1), (2, 4), (2, 6), (6, 7)])
    def test_login01(self, a, b):
        print('---test_login01---')
        assert a + b == 2

    @allure.story('登录login02')
    @allure.title('login02')
    def test_login02(self):
        print('---test_login01---')
        assert 1 + 1 == 2

    def teardown_class(self):
        print('--该测试类的环境清除')


@allure.feature('购物模块')  #一级标签
class Test_Shoping:         #二级标签
    @allure.story('shoping')
    @allure.title('shoping01')
    def test_Shoping01(self):
        print('---test_login01---')
        assert 1 + 1 == 2


if __name__ == '__main__':
    pytest.main(['testfunc01.py', '-s', '--alluredir', '../report/tmp'])
    os.system('allure generate ../report/tmp -o ../report/report --clean')
