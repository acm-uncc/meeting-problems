#include <stdlib.h>
#include <stdio.h>

int main(int argc, char* argv[]){
	if (argc != 2){
		printf("Please use file to open as a command line param\n");
		return 1;
	}

	FILE* fptr;
	
	//Access rights to file we are opening (read only)
	char type[2] = "r";

	//Open the file as read only
	if ((fptr = fopen(argv[1], type)) == NULL){
		perror("Error opening file");
		return 1;
	}

	char found = 0;
	int cases, credit, itemCount, e, a, c;

	//Read in the number of cases
	fscanf(fptr, "%d", &cases);

	//For each case
	for (c = 1; c <= cases; ++c){
		
		//We have not found the answer yet
		found = 0;

		//Read in the persons credit and number of list items
		fscanf(fptr, "%d %d", &credit, &itemCount);
		int* items = (int*)malloc(itemCount * sizeof(int));

		//For each item
		for (e = 1; e < itemCount; ++e){

			//Read in the item
			fscanf(fptr, "%d", &items[e]);
			int first = items[e];

			//For every previous item
			for (a = e - 1; a >= 0; --a){
				
				//See if it this and the other item add to the persons credit
				if (first + items[a] == credit){
					//If it does, print and break
					printf("Case #%d: %d %d\n", c, a + 1, e + 1);
					found = 1;
					break;
				}

				//Break if we found the asnwer
				if (found){
					break;
				}
			}
		}
	}
}
