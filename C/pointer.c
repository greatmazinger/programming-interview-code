/*
 * Raoul/Bing's pointer pop quiz
 *   15 June 2017
 */
#include <stdio.h>
#include <stdlib.h>

void foo( int *inptr )
{
    int * bar;
    // I don't care about the memory leak.
    bar = (int *) malloc(sizeof(int));
    *bar = 100;
    inptr = bar;
}

int main()
{
    int number = 21;
    foo( &number );
    // Question: What is printed out?
    printf("Number is %d\n", number );
    return 0;
}
