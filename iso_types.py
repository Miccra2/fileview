from types import *


# iso structures
type ISO_VOLUME_DESCRIPTOR = STRUCT({
    "type": U8,
    "identifier": ARRAY(5, U8),
    "version": U8,
    "data": ARRAY(2041, U8),
})

type ISO_BOOT_RECORD = STRUCT({
    "type": U8,
    "identifier": ARRAY(5, U8),
    "version": U8,
    "boot_system_identifier": ARRAY(32, U8),
    "boot_identifier": ARRAY(32, U8),
    "boot_system_use": ARRAY(1977),
})

type ISO_PRIMARY_VOLUME_DESCRIPTOR = STRUCT({
    "type_code": U8,
    "standard_identifier": ARRAY(5, U8),
    "version": U8,
    "unused_0": U8,
    "": ARRAY(5, U8),
})
