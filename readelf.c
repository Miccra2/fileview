#include <stdio.h>
#include "elf.h"

typedef unsigned long long U64;

U64 elf_file_test(PELF_HEADER pelf_header, FILE *pf) {
	result = 0;
	fread(pelf_header, sizeof(*pelf_header), 1, pf);
	
}

int main(int argc, char argv[][]) {
	// argument test
	if (argc < 2) {
		printf("No PATH given, please provide a valid PATH!");
		return 0;
	}

	// open file
	FILE *pf = fopen(argv[1], "rb");

	if (pf == NULL) {
		printf("No valid PATH given, please provide a valid PATH!");
		return 0;
	}
	
	// get file size
	fseek(pf, 0, SEEK_END);
	U64 file_size = ftell(pf);
	fseek(pf, 0, SEEK_SET);
	
	ELF_HEADER elf_header;	
	U64 test = elf_file_test(&elf_header, pf);
	if (test == 32) {
		
	} else if (test == 64) {
	
	} else {
		printf("not ELF file, please provide a valid ELF file!");
		return 0;
	}

	fcolse(pf);
	return 0;
}
