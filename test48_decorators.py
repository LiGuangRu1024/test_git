# @time     ：2024/7/16 16:21
# @author   : 莉光哈哈哈
# @file     : test48_decorators.py
# @software : PyCharm
'''
1.计时装饰器-----用来测量函数执行时间
'''
import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds to execute")
        return result

    return wrapper


@timing_decorator
def example_function():
    time.sleep(1)


example_function()

'''
2.日志记录装饰器-----用于在函数调用前后打印日志信息
'''


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function:{func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished executing.")
        return result

    return wrapper


@logging_decorator
def another_example():
    pass


another_example()

'''
3.缓存装饰器-----用于缓存具有重复计算的函数结果，提高效率
'''


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))

'''
4.权限检查装饰器-----用于验证用户是否有权限执行某个操作
'''


def admin_required_decorators(func):
    def wrapper(user, *args, **kwargs):
        if user.is_admin:
            return func(user, *args, **kwargs)
        else:
            raise PermissionError("Admin access required.")

    return wrapper


@admin_required_decorators
def sensitive_operation(user):
    print(f"{user.name} performed a sensitive operation")


# 假设User类有一个is_admin属性
class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin


user = User("Alice", True)
sensitive_operation(user)

'''
5.单例模式装饰器-----确保一个类只有一个实例，并提供一个全局访问点
'''


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return get_instance


@singleton
class SingletonClass:
    pass


s1 = SingletonClass()
s2 = SingletonClass()
assert s1 is s2

'''
6.异常处理装饰器-----自动处理函数中抛出的特定异常
'''


def exception_handler(exception_type, handler):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_type as e:
                return handler(e)

        return wrapper

    return decorator


@exception_handler(ValueError, lambda e: f"Caught an error:{e}")
def minght_raise_value_error(x):
    return 1 / x


print(minght_raise_value_error(0))

'''
7.性能分析装饰器-----使用cProfile模块进行性能分析
'''
import cProfile


def profile_decorator(func):
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        profiler.print_stats()
        return result

    return wrapper


@profile_decorator
def some_function_to_profile():
    # 示例代码
    pass


some_function_to_profile()

'''
8.类方法、静态方法装饰器-----将普通方法转换为类方法或者静态方法
'''


def classmethod_decorator(func):
    def wrapper(cls, *args, **kwargs):
        return func(*args, **kwargs)

    return classmethod(wrapper)


def staticmethod_decorator(func):
    return staticmethod(func)


class MyClass:
    @classmethod_decorator
    def from_string(cls, string):
        return cls(string)

    @staticmethod_decorator
    def multiply(a, b):
        return a * b


instance = MyClass.from_string("hello")
print(MyClass.multiply(2, 3))

'''
9.重试装饰器-----当函数执行失败时自动重试一定次数
'''
import random


def retry(max_retries=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    print(f"Retrying {func.__name__} due to {e}. Attempt {retries}/{max_retries}.")
                    time.sleep(delay)
            raise Exception(f"Failed after {max_retries} attempts.")

        return wrapper

    return decorator


@retry(max_retries=3)
def flaky_function():
    if random.random() > 0.5:
        raise ValueError("Random failure")
    return "success"


print(flaky_function())

'''
10.类装饰器-----用于修改或包装类的行为
'''


def add_extra_attribute(cls):
    cls.extra_attribute = 'This is an extra attribute'
    return cls


@add_extra_attribute
class MyClass:
    pass


instance = MyClass()
print(instance.extra_attribute)

'''
11.装饰器链-----可以在一个函数上应用多个装饰器，它们会按照从下到上的顺序被调用
'''


def decor1(func):
    def wrapper():
        print("Decorator 1")
        func()

    return wrapper


def decor2(func):
    def wrapper():
        print("Decorator 2")
        func()

    return wrapper


@decor1
@decor2
def say_message():
    print("hello world")


say_message()

'''
12.functools.wraps-----保持被装饰函数的元信息（如名称、文档字符串等）
'''
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Wrapper function called.")
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def example_func():
    """This is an example function"""
    print("Original function called")


print(example_func.__name__)
print(example_func.__doc__)

'''
13.带参数的类装饰器-----结合类装饰器与传递参数的能力，可以创建更灵活的装饰器
'''


class LogDecorator:
    def __init__(self, msg):
        self.msg = msg

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(self.msg)
            return func(*args, **kwargs)

        return wrapper


@LogDecorator("Logging before and after function call")
def another_func(x, y):
    return x + y


print(another_func(2, 3))

'''
14.字符串反转装饰器-----会使函数的字符串输出逆序
'''


def reverse_string(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        if isinstance(original_result, str):
            return original_result[::-1]
        return original_result

    return wrapper


@reverse_string
def greet(name):
    return f"hello,{name}"


print(greet("Alice"))

'''
15.文本加粗装饰器-----给函数的字符串输出加上Markdown或HTML的加粗标签，是文本在支持这些格式的地方显示为粗体
'''


def boldify_text(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        if isinstance(text, str):
            return f"**{text}**"  # Markdown加粗
            # 或者返回"<strong>{text}</strong>"用于HTML
        return text

    return wrapper


@boldify_text
def print_message(message):
    return message


print(print_message("Important Note"))

'''
16.调用计数器装饰器-----为任何函数添加调用次数的统计，适合调试或性能分析
'''


def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Call {wrapper.calls} of {func.__name__}")
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@count_calls
def add(a, b):
    return a + b


print(add(1, 2))
print(add(3, 4))

'''
17.随机选择输出装饰器-----让函数的输出随机选择于几个预设值之间，增加一些不可预测性
'''
import random


def random_choice(choices):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return random.choice(choices)

        return wrapper

    return decorator


@random_choice(['yes', 'no', 'maybe'])
def answer_question():
    pass


print(answer_question())

'''
个性化计时器装饰器-----除了记录函数执行时间，还能以不同风格（如emoji、颜色）显示结果
'''
import time, termcolor


def timer_with_style(style="default"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            duration = end - start
            if style == 'emoji':
                print(f"🕒 Function '{func.__name__}' took {duration}")
            elif style == 'color':
                termcolor.cprint(f"Function '{func.__name__}' took {duration}")
            else:
                print(f"Function '{func.__name__}' took {duration}")
            return result

        return wrapper

    return decorator


@timer_with_style(style="color")
def heavy_computation():
    time.sleep(1)


heavy_computation()  # 以绿色输出执行时间
