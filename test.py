def check(r, c):
    # 위, 오른쪽, 아래, 왼쪽으로 탐색
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    # 확인한 곳은 0으로 처리
    lake[r][c] = 0
    # 반복문을 사용하여
    for i in range(4):
        # 인덱스 범위 내에서 해당 좌표의 값이 1일 경우에
        if 0<=r+dr[i]<N and 0<=c+dc[i]<M and lake[r+dr[i]][c+dc[i]]:
            # 재귀 함수를 써서 값이 1인 좌표로 계속 이동한다.
            return check(r+dr[i], c+dc[i])

# 테스트 케이스를 입력 받음
T = int(input())
# 테스트 케이스 실행
for tc in range(1, T+1):
    # 가로 M, 세로 N, 연못 좌표 개수 K를 입력받음
    M, N, K = map(int, input().split())
    # 좌표를 입력 받아 2차원 배열 생성
    arr = [list(map(int, input().split())) for _ in range(K)]
    # 0으로 이루어진 2차원 배열을 생성하여
    lake = [[0]*M for _ in range(N)]
    # 입력 받은 좌표에 1을 넣는다.
    for i in range(K):
        lake[arr[i][1]][arr[i][0]] = 1
    # 물고기 마리 수를 나타내기 위한 변수를 생성하여
    cnt = 0
    # 좌표가 1일 때 함수를 실행한다.
    for r in range(N):
        for c in range(M):
            if lake[r][c]:
                # 1로 이루어진 그룹이 형성되므로 마리수를 1 더한다.
                cnt += 1
                check(r, c)
    print("#{} {}".format(tc, cnt))


'''
3
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 3
5 5
4 4
6 6
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0

'''