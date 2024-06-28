// unsigned big endian
typedef unsigned char UB8;
typedef unsigned short UB16;
typedef unsigned long UB32;
typedef unsigned long long UB64;

// unsigned little endian
typedef unsigned char UL8;
typedef unsigned short UL16;
typedef unsigned long UL32;
typedef unsigned long long UL64;

// signed big endian
typedef signed char SB8;
typedef signed short SB16;
typedef signed long SB32;
typedef signed long long SB64;

// signed little endian
typedef signed char SL8;
typedef signed short SL16;
typedef signed long SL32;
typedef signed long long SL64;

// unsigned
typedef union { UB8 big; UL8 little; } U8;
typedef union { UB16 big; UL16 little; } U16;
typedef union { UB32 big; UL32 little; } U32;
typedef union { UB64 big; UL64 little; } U64;

// unsigned big endian followed by unsigned little endian
typedef struct { UB8 big; UL8 little; } UBL8;
typedef struct { UB16 big; UL16 little; } UBL16;
typedef struct { UB32 big; UL32 little; } UBL32;
typedef struct { UB64 big; UL64 little; } UBL64;

// unsigned little endian followed by unsigned big endian
typedef struct { UL8 little; UB8 big; } ULB8;
typedef struct { UL16 little; UB16 big; } ULB16;
typedef struct { UL32 little; UB32 big; } ULB32;
typedef struct { UL64 little; UB64 big; } ULB64;

// signed big endian followed by signed little endian
typedef struct { SB8 big; SL8 little; } SBL8;
typedef struct { SB16 big; SB16 little; } SBL16;
typedef struct { SB32 big; SB32 little; } SBL32;
typedef struct { SB64 big; SB64 little; } SBL64;

// signed little endian followed by signed big endian
typedef struct { SL8 little; SB8 big; } SLB8;
typedef struct { SL16 little; SB16 big; } SLB16;
typedef struct { SL32 little; SB32 big; } SLB32;
typedef struct { SL64 little; SB64 big; } SLB64;

// signed
typedef union { SB8 big; SL8 little; } S8;
typedef union { SB16 big; SL16 little; } S16;
typedef union { SB32 big; SL32 little; } S32;
typedef union { SB64 big; SL64 little; } S64;

typedef struct {
    U8  year[4];
    U8  month[2];
    U8  day[2];
    U8  hour[2];
    U8  minute[2];
    U8  second[2];
    U8  hunderths_second[2];
    U8  time_zone_offset;   // -48 (west) through 52 (east)
} DATE_AND_TIME;

typedef struct {
    U8      type;
    U8      identifier[5];              // "CD001"
    U8      version;
    U8      data[2041];
} ISO_VOLUME_DESCRIPTOR;

typedef struct {
    U8      type;
    U8      identifier[5];              // "CD001"
    U8      version;
    U8      boot_system_identifier[32];
    U8      boot_identifier[32];
    U8      boot_system_use[1977];
} ISO_BOOT_RECORD;

typedef struct {
    U8      type_code;
    U8      standard_identifier[5];     // "CD001"
    U8      version;
    U8      unused_0;
    U8      system_identifier[32];
    U8      volume_identifier[32];
    U8      unused_1[8];
    ULB32   volume_space_size;
    U8      unused_2[32];
    ULB16   volume_set_size;
    ULB16   volume_sequence_number;
    ULB16   logical_block_size;
    ULB32   path_table_size;
    UL32    location_type_L_path_table;
    UL32    location_optional_type_L_path_table;
    UB32    location_type_M_path_table;
    UB32    location_optional_type_M_path_table;
    U8      directory_entry_root_directory[34];
    U8      volume_set_identifier[128];
    U8      publisher_identifier[128];
    U8      data_preparer_identifier[128];
    U8      application_identifier[128];
    U8      copyright_file_identifier[37];
    U8      abstract_file_identifier[37];
    U8      bilbliographic_file_identifier[37];
    DATE_AND_TIME   volume_creation_date_and_time;
    DATE_AND_TIME   volume_modification_date_and_time;
    DATE_AND_TIME   volume_expiration_date_and_time;
    DATE_AND_TIME   volume_effective_date_and_time;
    U8      file_structure_version;
    U8      unused_3;
    U8      application_used[512];
    U8      reserved[653];
} ISO_PRIMARY_VOLUME_DESCRIPTOR;

typedef struct {
    U8      type;
    U8      identifier[5];              // "CD001"
    U8      version;
} ISO_VOLUME_DESCRIPTOR_SET_TERMINATOR;

U8 ISO_DIRECTORY_IDENTIFIER_LENGTH;

typedef struct {
    U8      directory_identifier_length;
    U8      extended_attribute_record_length;
    U32     location_of_extent;         // "LBA" different format depending on L- or M-Table
    U16     directory_number_of_parent_directory;
    U8      directory_identntifier[ISO_DIRECTORY_IDENTIFIER_LENGTH];
    U8      padding;
} ISO_PATH_TABLE;

typedef struct {
    U8      years;
    U8      month;
    U8      day;
    U8      hour;
    U8      minute;
    U8      second;
    U8      gmt_offset;     // from -48 (west) through +52 (east)
} ISO_BIN_TIME_DATE;

typedef struct {
    char    hidden : 1;
    char    sub_directory : 1;
    char    associated_file : 1;
    char    format_information_in_extended : 1;
    char    owner_and_group_permissions_in_extended : 1;
    char    reserved : 2;
    char    no_final_directory_record : 1;
} ISO_DIRECTORY_FLAGS;

typedef struct {
    U8      directory_record_length;
    U8      extended_attribute_record_length;
    ULB32   extent_location;
    ULB32   data_length;
    ISO_BIN_TIME_DATE   date_and_time;
    ISO_DIRECTORY_FLAGS directory_flags;
} ISO_DIRECTORY;
