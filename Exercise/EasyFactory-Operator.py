
class Operation(object):
    '''
    四则运算的父类,接收用户输入的数值
    '''
    def __init__(self, number1=0, number2=0):
        self.num1 = number1
        self.num2 = number2

    def GetResult(self):
        pass
    pass


class OperationAdd(Operation):
    def GetResult(self):
        return self.num1 + self.num2


class OperationSub(Operation):
    def GetResult(self):
        return self.num1 - self.num2


class OperationMul(Operation):
    def GetResult(self):
        return self.num1 * self.num2


class OperationDiv(Operation):
    def GetResult(self):
        if self.num2 == 0:
            return '除数不能为0 '
        return 1.0*self.num1 / self.num2


class OperationUndef(Operation):
    def GetResult(self):
        return '操作符错误'


class OperationFactory(object):
    def choose_oper(self,ch):
        if ch == '+':
            return OperationAdd()
        elif ch == '-':
            return OperationSub()
        elif ch == '*':
            return OperationMul()
        elif ch == '/':
            return OperationDiv()
        else:
            return OperationUndef()

if __name__ == "__main__":
    ch = ''
    while not ch == 'q':
        num1 = float(input('请输入第一个数值:  '))
        num2 = float(input('请输入第二个数值:  '))
        oper = str(input('请输入一个四则运算符:  '))
        # Operation(num1,num2)
        OF = OperationFactory()
        oper_obj = OF.choose_oper(oper)
        oper_obj.num1 = num1
        oper_obj.num2 = num2
        print( '运算结果为:',oper_obj.GetResult())
