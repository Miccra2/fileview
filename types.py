# base types
type BYTES = ByteType
type ARRAY[T] = Array[T]
type UNION[T] = Union[T]
type STRUCT[T] = Struct[T]
type TYPES[T] = BYTES | ARRAY[T] | UNION[T] | STRUCT[T]

# BYTES types
# unsigned little endian
type UL8 = ByteType(1, False, "little")
type UL16 = ByteType(2, False, "little")
type UL32 = ByteType(4, False, "little")
type UL64 = ByteType(8, False, "little")

# unsigned big endian
type UB8 = ByteType(1, False, "big")
type UB16 = ByteType(2, False, "big")
type UB32 = ByteType(4, False, "big")
type UB64 = ByteType(8, False, "big")

# signed little endian
type SL8 = ByteType(1, True, "little")
type SL16 = ByteType(2, True, "little")
type SL32 = ByteType(4, True, "little")
type SL64 = ByteType(8, True, "little")

# signed big endian
type SB8 = ByteType(1, True, "big")
type SB16 = ByteType(2, True, "big")
type SB32 = ByteType(4, True, "big")
type SB64 = ByteType(8, True, "big")

# unsigned == unsigned little || unsigned big
type U8 = UL8 | UB8
type U16 = UL16 | UB16
type U32 = UL32 | UB32
type U64 = UL64 | UB64

# signed == signed little || signed big
type S8 = SL8 | SB8
type S16 = SL16 | SB16
type S32 = SL32 | SB32
type S64 = SL64 | SB64


class ByteType:
    size: int = 1       # in bytes
    signed: bool = True
    byteorder: str = "big"

    def __init__(self, size: int = 1, signed: bool = True, byteorder: str = "big") -> None:
        self.size = size
        self.signed = signed
        self.byteorder = byteorder

    def __len__(self) -> int:
        return self.size


class Array:
    size: int = 0       # in bytes
    byte_type: TYPES
    data: bytes = b""

    def __init__(self, size: int, byte_type: TYPES = U8) -> None:
        self.byte_type = byte_type
        self.size = size * len(self.byte_type)

    def __len__(self) -> int:
        return self.size


class Union:

