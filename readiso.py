from sys import argv
from dumb import dump
from iso_struct import *


def dump_hex_iso(data: bytes) -> None:
    # TODO: implement BDA standards
    i: int = 0
    string: str = ""

    string += "IVT (Interrupt Vector Tabel) [1 KiB]:\n%s\n" % dump(data, i, 1024); i += 1024
    string += "BDA (BIOS Data Area) [256 B]:\n%s\n" % dump(data, i, 256); i += 256
    string += "conventional memory [29.75 KiB]:\n%s\n" % dump(data, i, 29.75 * 1024); i += 29.75 * 1024
    string += "OS boot sector [512]:\n%s\n" % dump(data, i, 512); i += 512
    string += "conventional memory [480.5 KiB]:\n%s\n" % dump(data, i, 480.5 * 1024); i += 480.5 * 1024
    string += "EBDA (Extended BIOS Data Area) [128 KiB]:\n%s\n" % dump(data, i, 128 * 1024); i += 128 * 1024
    string += "video display memory [128 KiB]:\n%s\n" % dump(data, i, 128 * 1024); i += 128 * 1024
    string += "video BISO [32 KiB]:\n%s\n" % dump(data, i, 32 * 1024); i += 32 * 1024
    string += "BIOS Expansions [160 KiB]:\n%s\n" % dump(data, i, 160 * 1024); i += 160 * 1024
    string += "motherboard BIOS [64 KiB]:\n%s\n" % dump(data, i, 64 * 1024); i += 64 * 1024
    string += "... [... B]:\n%s\n" % dump(data, i)

    return string

def dump_info_iso(data: bytes) -> None:
    offset: int = 32 * 1024 # 32 KiB

    pass

def main() -> None:
    hex_or_info: str = "info"
    file: bytes = b""

    if len(argv) > 2:
        hex_or_info = argv[2][1:]

    if len(argv) > 1:
        try:
            with open(argv[1], "rb") as f:
                file = f.read()
        except IOError:
            print("No valid PATH given, please provide a valid PATH!")
            return

        if hex_or_info == "hex":
            print(dump_hex_iso(file))
        else:
            print(dump_info_iso(file))
    else:
        print("No PATH given, please provide a valid PATH!")

if __name__ == "__main__":
    main()
