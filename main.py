# 在此文件中实现 isOdd 函数

def isOdd(value):
    """
    判断输入是否为奇整数    
    参数:
    value - 任意类型的输入值    
    返回:
    bool - 如果是整数且为奇数返回 True，否则返回 False
    """
    # 学生实现代码区域
    # 判断输入是否为整数
    if not isinstance(value, int):
        return False
    # 判断是否为奇数（使用取模运算）
    if value % 2 != 0:
        return True
    else:
        return False
    # 提示：首先检查类型是否为整数，然后检查奇偶性
    
