import pytest
import yaml
from learnpytest.calculator import Calculator


def get_datas():
    with open('./datas/calc.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
    return [adddatas, myids]

def get_datas1():
    with open('./datas/calc.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        divdatas = mydatas['devided']['datas']
        myids = mydatas['devided']['myids']
    return [divdatas, myids]

class TestCalc:
    def setup_class(self):
        print("类级开始计算")

    def teardown_class(self):
        print("类级计算结束")

    def setup(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        '''
        测试相加
        '''
        print("测试相加")
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert expect == result


    @pytest.mark.parametrize('a,b,expect', [(0.1, 0.1, 0.2), (0.1, 0.2, 0.3)])
    def test_add_float(self, a, b, expect):
        result = round(self.calc.add(a, b), 2)
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', get_datas1()[0], ids=get_datas1()[1])
    def test_devided(self, a, b, expect):
        '''
        测试相除
        '''
        print("测试相除")
        # calc = Calculator()
        result = self.calc.div(a, b)
        assert expect == result
