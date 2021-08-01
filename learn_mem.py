import psutil
p = psutil.Process()
M = 1024 * 1024
UNIT = 1024 * 1000

def print_current_rss(prefix: str = ""):
    print(f"{prefix} {p.memory_info().rss / 1024 / 1024} MB")

BIG_MEM_OBJECT = b"B" * 1000 * M

def f():
    def closure():
        a1 = b'A' * 150 * UNIT
        print(len(a1))
    closure()
    a = b'b' * 500 * UNIT
    print(len(a))
    print_current_rss("use closure")


def f1():
    a1 = b'A' * 150 * UNIT
    print(len(a1))

    a = b'b' * 500 * UNIT
    print(len(a))
    print_current_rss("no optimize")



f()

f1()