### quiz1

```c
#include <stdio.h>



int main (void)
{
    int stock = 5;
    int money = 1000;
    int sales = 0;
    int order;

    printf("Enter the number of order : ");
    scanf("%i", &order);
    stock -= order;
    sales += money * order * 1.1;
    printf("Current stock : %i, sales : %d\n", stock, sales);

}
```



### quiz2

```c
#include <stdio.h>

int main (void)
{
    int save;
    printf("Enter the target amount : ");
    scanf("%i", &save);
    printf("The amount you will receive at the expiration date is %.2fWon.\n", save * 1.012);
}
```



### quiz3

```c
#include <stdio.h>
#include <cs50.h>
#include <string.h>


int main(void){    
    string day_input = get_string("요일을 입력하세요: ");
    if (strcmp(day_input, "월요일") == 0)
    {
        printf("청국장\n");

    }
    else if (strcmp(day_input, "화요일") == 0)
    {
        printf("비빔밥\n");
    }
    else if (strcmp(day_input, "수요일") == 0)
    {
        printf("된장찌개\n");
    }
    else if (strcmp(day_input, "목요일") == 0)
    {
        printf("칼국수\n");
    }
    else if (strcmp(day_input, "금요일") == 0)
    {
        printf("냉면\n");
    }
    else if (strcmp(day_input, "토요일") == 0)
    {
        printf("소불고기\n");
    }
    else if (strcmp(day_input, "일요일") == 0)
    {
        printf("오삼불고기\n");
    }
    
}
```

