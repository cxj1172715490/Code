# 定义一个通用装饰器
def decorator(func):
    def inner(*args, **kwargs):
        print("扩展功能...")
        result = func(*args, **kwargs)
        print("扩展功能...")
        return result

    return inner


# 定义一个带有参数的装饰器
def route(flag):
    def decorator(func):
        def inner(*args, **kwargs):
            if flag == "+":
                pass
            elif flag == "-":
                pass
            else:
                pass
            result = func(*args, **kwargs)
            return result

        return inner

    return decorator


@route("+")  # 1.route("+")返回decorator 2、产生@decorator装饰器
def add():
    pass


@route("-")  # 1.route("-")返回decorator 2、产生@decorator装饰器
def sub():
    pass
	


@decorator  # 有参无返回值类型
def test01(a, b):
    print(a + b)


@decorator  # 无参无返回值
def test02():
    print("发表评论")


@decorator  # 有参有返回值
def test03(a, b):
    return a + b


@decorator  # 不定长参数
def test04(*args, **kwargs):
    print(args, kwargs)


if __name__ == '__main__':
    test01(1, 2)

    test02()

    ret = test03(1, 2)
    print(ret)

    test04(1, 2, a=10, b=20)
