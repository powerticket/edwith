#include <cs50.h>
#include <stdio.h>

int main(void)
{
    float x = get_float("x : ");
    float y = get_float("y : ");
    printf("x / y = %f.10\n", x / y);
}
