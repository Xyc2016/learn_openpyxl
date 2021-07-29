import psutil
p = psutil.Process()
M = 1024 * 1024
M = 1024 * 300

def print_current_rss(prefix: str = ""):
    print(f"{prefix} {p.memory_info().rss / 1024 / 1024} MB")


def f():
    def closure():
        a1 = b'A' * 500 * M
        print(len(a1))
    closure()
    a = b'b' * 100 * M 
    print(len(a))
    print_current_rss("use closure")


def f1():
    a1 = b'A' * 500 * M
    print(len(a1))

    a = b'b' * 100 * M
    print(len(a))
    print_current_rss("no optimize")



f()

f1()