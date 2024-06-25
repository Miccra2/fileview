from sys import argv

class Dump:
    data: bytes
    offset: int
    length: int

    def __init__(self, data_or_path: str | bytes) -> None:
        if type(data_or_path) == str:
            try:
                with open(data_or_path, "rb") as f:
                    self.data = f.read()
            except IOError:
                assert False, "no valid PATH given, please provide a valid PATH!"
        elif type(data_or_path) == bytes:
            self.data = data_or_path
        else:
            assert False, "data_or_path must be of type `str` or `bytes`!"

    def putc(self, c: bytes) -> list[str, str]:
        a: str = ""
        n: str = ""
        for j in c:
            n += "%.2X " % j
            a += "." if j < 0x20 or j > 0x7E else chr(j)
        if len(c) < 16:
            n += "   " * (16 - len(c))
            a += " " * (16 - len(c))
        return n + "| %s |\n" % a

    def dump(self, offset: int = 0, length: int = -1) -> str:
        data: bytes = self.data
        length: int = len(data) if length == -1 else length
        end: int = offset + length
        n: str = ""
        s: int = -1
        l: bytes = b""
        c: bytes
        a: str
        x: bytes
        for i in range(offset, end, 16):
            c = data[i:i+16] if i + 16 < len(data) else data[i:]
            if l == c:
                s += 1
                x = c
                continue
            elif s > 0:
                n += "* %i\n%.8X:  " % (s, i) + self.putc(x)
                s = 0
            n += "%.8X:  " % i
            n += self.putc(c)
            l = c
        if s > 0:
            n += "* %i\n%.8X:  " % (s, i)
            n += self.putc(c)
        return n

    def print(self, offset: int = 0, length: int = -1) -> None:
        print(self.dump(offset, length))


if __name__ == "__main__":
    if len(argv) > 1:
        d = Dump(argv[1])
        d.print()
