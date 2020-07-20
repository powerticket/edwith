#include <cs50.h>
#include <stdio.h>

void cough(void);

int  main(void)
{
    // printf("cough\n");
    // printf("cough\n");
    // printf("cough\n");

    for (int i = 0; i < 3; i++)
    {
        cough();
    }


}

void cough(void)
{
    printf("cough\n");
}
