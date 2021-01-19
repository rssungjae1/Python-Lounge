# https://programmers.co.kr/learn/courses/30/lessons/64061

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
def solution(board, moves):
    answer = 0
    stack = [0]
    for i in moves:
        for bo in range(0, len(board)):
            if board[bo][i-1] != 0:
                if stack[len(stack)-1] == board[bo][i]:
                    stack.pop()
                    answer += 2
                    pass
                else:
                    stack.append(board[bo][i])
                board[bo][i-1] = 0
                break
    return answer
# print(solution(board, moves))

def solution2(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
print(solution2(board, moves))
