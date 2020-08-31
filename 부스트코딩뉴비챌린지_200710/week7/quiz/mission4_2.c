// 작성자 뉴비_team8-0 전원표
# include<stdio.h>
# include<stdlib.h>

// 해당 코드의 시간복잡도는 O(n^2)이다. 버블 정렬과 새로운 리스트의 길이를 구하는 과정에서 2중 for문이 들어갔기 때문이다.
int main(void){
    // 정수의 갯수 N을 입력 받고 N개 만큼의 int 메모리를 할당하여 입력받는다.
    int N;
    scanf("%d", &N);
    int *list = malloc(sizeof(int) * N);
    for (int i = 0; i < N; i++){
        int tmp;
        scanf("%d", &tmp);
        *(list+i) = tmp;
    }
    // 버블 정렬을 통해 리스트를 오름차순으로 정렬한다.
    for (int i = 2; i < N+1; i++){
        for (int j = N-i; j < N-1; j++){
            if (list[j] > list[j+1]){
                int tmp = list[j];
                list[j] = list[j+1];
                list[j+1] = tmp;
            }
        }
    }
    // 정렬된 리스트를 살펴보며 같은 값이 있으면 길이를 1씩 빼준다.
    int new_N = N;
    for (int i = 0; i < N; i++){
        for (int j = i+1; j < N; j++){
            if (list[i] == list[j]){
                new_N--;
                break;
            }
        }
    }
    // 새로 얻은 길이의 리스트에 메모리를 할당한다.
    // 배열된 리스트를 하나씩 살펴보며 이전 값보다 클 경우에만 새로운 리스트에 추가한다.
    int *new_list = malloc(sizeof(int) * new_N);
    int new_idx = 0;
    int min = list[0];
    new_list[0] = min;
    for (int i = 1; i < N; i++){
        if (list[i] > min){
            min = list[i];
            new_idx++;
            new_list[new_idx] = min;
        }
    }
    // 기존 리스트의 메모리를 해제하고 새로운 리스트를 출력한 후, 새로운 리스트의 메모리 역시 해제한다.
    free(list);
    for (int i = 0; i < new_N; i++){
        printf("%d ", *(new_list+i));
    }
    printf("\n");
    free(new_list);
}