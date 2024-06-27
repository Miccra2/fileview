from sys import argv


def dump_line(data: bytes, offset: int = 0) -> str:
    sLine: str = ""
    cLine: str = ""

    sLine += "%.8X:  " % offset

    for byte in data:
        sLine += "%.2X " % byte
        
        if byte < 0x7E and byte > 0x1F:
            cLine += chr(byte)
        else:
            cLine += "."

    if len(data) < 16:
        sLine += "   " * (16 - len(data))
        cLine += " " * (16 - len(data))

    return sLine + "| %s |\n" % cLine

def dump(data: bytes, offset: int = 0, size: int = -1) -> str:
    start: int = int(offset - (offset % 16))
    end: int = int(size)
    lLine: bytes = b""
    bLine: bytes = b""
    string: str = ""
    count: int = 0

    if size < 0:
        end = len(data)

    for r in range(start, end, 16):
        if r + 16 > len(data):
            bLine = data[r:]
        else:
            bLine = data[r:r+16]

        if len(bLine) < 1:
            break

        if bLine == lLine:
            count += 1
            continue
        elif count > 0:
            string += "* %i\n%s" % (count, dump_line(lLine, r - 16))
            count = 0

        string += dump_line(bLine, r)
        lLine = bLine
    
    if string == "":
        string += dump_line(bLine, start)

    if count > 0:
        string += "* %i\n%s" % (count, dump_line(lLine, r))

    return string

def main() -> None:
    file: bytes = b""
    start: int = 0
    end: int = -1

    if len(argv) > 2:
        start = int(argv[2])

    if len(argv) > 3:
        end = int(argv[3])
    
    if len(argv) > 1:
        try:
            with open(argv[1], "rb") as f:
                file = f.read()
            print(dump(file, start, end))
        except IOError:
            print("No valid PATH given, please provide a valid PATH!")
    else:
        print("No PATH given, please provide a valid PATH!")

if __name__ == "__main__":
    main()
    print()
