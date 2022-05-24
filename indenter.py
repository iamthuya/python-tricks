class Indenter:
    def __init__(self):
        self.indent_char = "    "
        self.indent_count = 0

    def __enter__(self):
        self.indent_count += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.indent_count > 0:
            self.indent_count -= 1

    def print(self, text):
        print(f"{(self.indent_char * self.indent_count)}{text}")


def main():
    with Indenter() as indent:
        indent.print("hi!")
        with indent:
            indent.print("hello")
            with indent:
                indent.print("bonjour")
        indent.print("hey")


if __name__ == "__main__":
    main()
