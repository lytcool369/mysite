from django.test import TestCase
import board.models as boardModel


# result = boardModel.paging(5)
# print(result)
#
# print(int(result['pcontrol']['prev_p']))


# 더미 데이터 넣기
for i in range(1, 70):
    boardModel.insert_write(f'루프 {i}번째 글', f'루프 {i}번째 내용', 1)
