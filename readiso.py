import sys, dump

def indent_dump(dump: dump.Dump, offset: int, length: int, level: int = 1) -> None:
    print(("    " * level) + dump.dump(offset, length).replace("\n", "\n%s" % ("    " * level)))

def main() -> None:
    args = sys.argv

    if len(args) < 2:
        print("No PATH given, please provide a valid PATH!")
        exit(1)

    d = dump.Dump(sys.argv[1])

    i: int = 0
    
    print("real mode IVT (Interupt Vector Table): (1KiB)")
    indent_dump(d, i, 1024, 1)
    i += 1024
    
    print("BDA (BIOS Data Area): (256 B)")
    indent_dump(d, i, 256, 1)
    i += 256
    
    print("conventional memory: (29.75 KiB)")
    indent_dump(d, i, int(29.75 * 1024), 1)
    i += int(29.75 * 1024)

    print("boot sector: (512 B)")
    indent_dump(d, i, 512, 1)
    i += 512

    print("conventional memory: (480.5 KiB)")
    indent_dump(d, i, int(480.5 * 1024), 1)
    i += int(480.5 * 1024)

    print("EBDA (Extended BIOS Data Area): (128 KiB)")
    indent_dump(d, i, 128 * 1024, 1)
    i += 128 * 1024

    print("Video display memory: (128 KiB)")
    indent_dump(d, i, 128 * 1024, 1)
    i += 128 * 1024

    print("Video BIOS: (32 KiB)")
    indent_dump(d, i, 32 * 1024, 1)
    i += 32 * 1024

    print("BIOS Expansion: (160 KiB)")
    indent_dump(d, i, 160 * 1024, 1)
    i += 160 * 1024

    print("Motherboard BIOS: (64 KiB)")
    indent_dump(d, i, 64 * 1024, 1)
    i += 64 * 1024
	
if __name__ == "__main__":
    main()
