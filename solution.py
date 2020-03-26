import time

'''
만약 뱀이 max_move 만큼 연속하고, 뒤에 사다리로 갈 수 있는 곳이 없다면 해당 게임은 끝나지 않는다.
'''

def solution(ladder, snake, map_size):
  turn = 0
  current_pos = 0
  max_move = 6

  snake_dict = snake_to_dict(snake)
  visited = {}
  
  while current_pos < map_size:
    print('======================')
    ladder_move_range = find_move_range(ladder, current_pos, max_move, True)
    snake_move_range = find_move_range(snake, current_pos, max_move, False)

    print('시작위치: %d'%(current_pos))
    print('해당 턴에 나올 수 있는 사다리 위치: %s'%(ladder_move_range))
    print('해당 턴에 나올 수 있는 뱀     위치: %s'%(snake_move_range))

    if len(ladder_move_range):# 사다리로 이동할 수 있을 때
      print('주사위 숫자: %d -> %d 이동'%(ladder_move_range[0][0], ladder_move_range[0][1]))
      current_pos = ladder_move_range[0][1]
      visited[ladder_move_range[0][1]] = True
      visited[ladder_move_range[0][0]] = True
    else:
      move_pos = max_move if not len(snake_move_range) else extract_snake_max_move(snake_move_range, snake_dict, current_pos, max_move, visited)
      current_pos += move_pos
      visited[move_pos] = True
    
    turn += 1

    print('현재위치: %d'%(current_pos))
    print('%d턴을 마칩니다. %s'%(turn, current_pos < map_size))
    print('======================\n')
    # time.sleep(1)
  
  return turn

def find_move_range(obstacle, current_pos, max_move, order=True): 
  '''
    order: 
      내림차순 True 
      오름차순 False
  '''
  move_range = [move for move in obstacle if move[0] <= current_pos + max_move and move[0] > current_pos]
  move_range.sort(key = lambda element : element[1], reverse=order)
  return move_range

def extract_snake_max_move(snake_range_move, snake_dict, current_pos, max_move, visited):
  for move in range(max_move, 0, -1):
    is_snake = snake_dict.get(current_pos + move, None)
    is_visited = visited.get(current_pos + move, None)
    if (not is_snake ) and (not is_visited) : return move

  # 모든 움직임이 뱀에 다 걸리는 경우
  # 뱀의 위치 좌표를 오름차순으로 정렬하여 0번째로 이동하기
  # for move in snake_range_move:
  #   is_visited = visited.get(current_pos + move[1], None)
  #   if not is_visited : return move[1]
  
  # return snake_range_move[0][0] - current_pos

def snake_to_dict(snake):
  return {v[0]: v[1] for v in snake}