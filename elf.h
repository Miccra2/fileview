typedef unsigned char U8;
typedef unsigned short U16;
typedef unsigned long U32;
typedef unsigned long long U64;
typedef signed char S8;
typedef signed short S16;
typedef signed long S32;
typedef signed long long S64;

typedef _ELF_HEADER {
	U8	e_magic[4];
	U8	e_class;
	U8	e_data;
	U8	e_version;
	U8	e_osabi;
	U8	e_abiversion;
	U8	e_pad[7];
	U16	e_type;
	U16	e_machine;
	U32	e_version;
	U32	e_entry;
	U32	e_phoff;
	U32	e_shoff;
	U32	e_flags;
	U16	e_ehsize;
	U16	e_phentsize;
	U16	e_phnum;
	U16	e_shentsize;
	U16	e_shnum;
	u16	e_shstrndx;
} ELF_HEADER, *PELF_HEADER;

typedef struct _PROG_HEADER32 {
	U32	p_type;
	U32	p_offset;
	U32	p_vaddr;
	U32	p_paddr;
	U32	p_filesz;
	U32	p_memsz;
	U32	p_flags;
	U32	p_align;
} PROG_HEADER32, *PPROG_HEADER;

typedef struct _PROG_HEADER64 {
	U32	p_type;
	U32	p_flags;
	U64	p_offset;
	U64	p_vaddr;
	U64	p_paddr;
	U64	p_filesz;
	U64	p_memsz;
	U64	p_align;
} PROG_HEADER64, *PPROG_HEADER64;

typedef struct _SECTION_HEADER32 {
	U32	sh_name;
	U32	sh_type;
	U32	sh_flags;
	U32	sh_addr;
	U32	sh_offset;
	U32	sh_size;
	U32	sh_link;
	U32	sh_info;
	U32	sh_addralign;
	U32	sh_entsize;
} SECTION_HEADER32, *PSECTION_HEADER32;

typedef struct _SECTION_HEADER64 {
	U32	sh_name;
	U32	sh_type;
	U64	sh_flags;
	U64	sh_addr;
	U64	sh_offset;
	U64	sh_size;
	U32	sh_link;
	U32	sh_info;
	U64	sh_addralign;
	U64	sh_entsize;
} SECTION_HEADER64, *PSECTION_HEADER64;

typedef struct _SYMBOL_TABLE32 {
	U32	st_name;
	U32	st_value;
	U32	st_size;
	U8	st_info;
	U8	st_other;
	U16	st_shndx;
} SYMBOL_TABLE32, *PSYMBOL_TABLE32;

typedef struct _SYMBOL_TABLE64 {
	U32	st_name;
	U8	st_info;
	U8	st_other;
	U16	st_shndx;
	U64	st_value;
	U64	st_size;
} SYMBOL_TABLE64, *PSYMBOL_TABLE64;

typedef struct _REL32 {
	U32	r_offset;
	U32	r_info;
} REL32, *PREL32;

typedef struct _REL64 {
	U64	r_offset;
	U64	r_info;
} REL64, *PREL64;

typedef struct _RELA32 {
	U32	r_offset;
	U32	r_info;
	U32	r_addend;
} RELA32, *PRELA32;

typedef struct _RELA64 {
	U64	r_offset;
	U64	r_info;
	U64	r_addend;
} RELA64, *PRELA64;

typedef struct _NOTE_HEADER32 {
	U32	n_namesz;
	U32	n_descsz;
	U32	n_type;
} NOTE_HEADER32, *PNOTE_HEADER32;

typedef struct _NOTE_HEADER64 {
	U64	n_namesz;
	U64	n_descsz;
	U64	n_type;
} NOTE_HEADER64, *PNOTE_HEADER64;
