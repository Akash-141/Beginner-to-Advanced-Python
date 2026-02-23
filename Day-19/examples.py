# Day 19 Examples: Context Managers

# ---------- Basic with example ----------
with open("sample.txt", "w") as f:
    f.write("Hello from Day 19!")

with open("sample.txt", "r") as f:
    print("File content:", f.read())


# ---------- Custom Context Manager (Class) ----------
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        print("Timer started")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        end = time.time()
        print(f"Timer stopped. Duration: {end - self.start:.4f} seconds")

with Timer():
    total = sum(range(1000000))


# ---------- Context Manager using contextlib ----------
from contextlib import contextmanager

@contextmanager
def simple_context():
    print("Entering simple context")
    yield
    print("Exiting simple context")

with simple_context():
    print("Inside simple context")


# ---------- Reading large file safely ----------
with open("sample.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())
