def solution(s):
   answer = 0
   cnt_same, cnt_diff = 0, 0
    
   for i in s:
       if cnt_same == cnt_diff:
           answer+=1
           k = i
       if k == i:
           cnt_same += 1
       else:
           cnt_diff += 1
       
   return answer