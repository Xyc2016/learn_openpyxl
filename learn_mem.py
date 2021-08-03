import resource
import psutil
p = psutil.Process()


def print_mem(prefix: str) -> None:
    print(f"{prefix}:peak {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024}")
    print(f"{prefix}:current {p.memory_info().rss / 1024 / 1024} MB")

