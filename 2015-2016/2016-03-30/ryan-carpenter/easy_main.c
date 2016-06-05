#include <stdio.h>
#include <stdlib.h>

#define size 4

int main(void){
	int arr[size][6] = { { 5, 6, 7 }, { 3, 9, 4 }, { 1, 8, 4, 6, 8, 2 }, { 2 } };

	int product = 1;
	int e = 0;

	for (; e < size * 5; ++e){
		int temp = *((int*)arr + e);
		product *= (temp == 0 ? 1 : temp);
	}

	printf("Answer: %d\n", product);
}