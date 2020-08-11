#include <stdio.h>
#include <string.h>

int main(void)
{
    char input1[5] = "14258"; // 입력 1
    char input2[5] = "25431"; // 입력 2
    int correct[5] = {0, 0, 0, 0, 0}; // 입력 1의 모든 문자가 입력 2에 들어있는지 확인하기 위한 배열
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (input1[i] == input2[j])
            {
                correct[i] = 1; // 입력 1의 i번 째 문자가 입력 2에 있을 경우 배열 correct의 i번 째를 1로 변경
                input2[j] = 'a'; // 똑같은 문자롤 또 받을 수 있기 때문에 비교한 입력 2의 문자는 다른 문자로 변경
            }
        }
    }
    for (int i = 0; i < 5; i++)
    {
        if (correct[i] == 0)
        {
            printf("False\n"); // correct 배열을 확인하여 0이 있을 경우, 즉, 입력 1의 i번 째 문자가 입력 2에 없을 경우 False 출력
            return 1;
        }
    }
    printf("True\n");
    return 0;
}