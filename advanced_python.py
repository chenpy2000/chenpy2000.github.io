def pretty(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!!!"
    return wrapper

@ pretty
def add(*args, **kwargs) -> str:
    ret = []
    for s in args:
        ret.append(s)
    return ' '.join(ret)

print(add("I am", "very, very", "happy"))