// 작성자 뉴비_team8-0 전원표
#include <stdio.h>
#include <stdlib.h>


int *divisor;

int compare(const void * a, const void * b)
{
    return (*(int*)a - *(int*)b);
}

int
main()
{
    int N;
    scanf("%d", &N);
    
    divisor = malloc(sizeof(int) * N);

    for(int i = 0; i < N; i++){
        int tmp;
        scanf("%d", &tmp);
        divisor[i] = tmp;
    }

    qsort(divisor, N, sizeof(int), compare);
    // 정렬된 약수 리스트의 처음과 끝의 수를 곱하면 해당 리스트의 수들을 약수로 하는 수를 구할 수 있다.
    int answer = divisor[0] * divisor[N-1];
    printf("%d\n", answer);

    return 0;
}