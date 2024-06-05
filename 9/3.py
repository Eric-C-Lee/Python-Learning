# model1
__all__ = ['m11']  # 当使用from model1 import * 时只能调用all列表中的元素
def m11():
    print('脱敏数据')
def m12():
    print('脱敏数据')
if __name__ == '__main__':    # 测试模块功能是否正确
    m11()
    m12()

# model2
__all__ = ['m21']  # 当使用from model2 import * 时只能调用all列表中的元素
def m21(a, b):
    return a + b
def m22(a, b):
    return a - b
if __name__ == '__main__':   # 测试模块功能是否正确
    print(m21(1, 2))
    print(m22(1, 2))
