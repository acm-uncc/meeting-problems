//Author: bobjrsenior
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){
	if (argc != 2){
		printf("Please enter input files as a command line argument\n");
		return EXIT_SUCCESS;
	}

	//Open input file
	FILE* fptr;
	if ((fptr = fopen(argv[1], "r")) == NULL){
		perror("Error readin file");
		return EXIT_FAILURE;
	}

	//Variables
	int cases, length, cur, e = 1;
	
	//Get the number of cases
	fscanf(fptr, "%d", &cases);

	//Loop for every case
	for (; e <= cases; ++e){
		//Read the number of different shyness levels
		fscanf(fptr, "%d", &length);

		//Number of current clappers
		int clappers = 0;
		//How many friends added
		int added = 0;
		//The number of clappers at the current shyness level
		int temp;

		//Go through every shyness level
		for (cur = 0; cur <= length; ++cur){

			//Get the number of clappers
			fscanf(fptr, " %1d", &temp);

			//If we don't have enough clappers to reach here, add them
			if (clappers < cur){
				added += (cur - clappers);
				clappers += cur - clappers;
			}

			//Add this level's clappers
			clappers += temp;
		}

		//Output the number of friends we added
		printf("Case #%d: %d\n", e, added);
	}

	fclose(fptr);
}