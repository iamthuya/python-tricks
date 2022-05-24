import time


class TimerClassBased:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self.start)


def main():
    with TimerClassBased() as tcb:
        time.sleep(5)


if __name__ == "__main__":
    main()
