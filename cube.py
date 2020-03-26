from solution import solution
from case_data import ladder1, ladder2, ladder3, snake1, snake2, snake3


map_size = 10 * 10

print('1번 게임 시작')
answer = solution(ladder1, snake1, map_size)
print('최소횟수: %d\n\n'%(answer))

print('2번 게임 시작')
answer = solution(ladder2, snake2, map_size)
print('최소횟수: %d\n\n'%(answer))

print('3번 게임 시작')
answer = solution(ladder3, snake3, map_size)
print('최소횟수: %d\n\n'%(answer))