"""
A critical point in a linked list is defined as either a local maxima or a local minima.
A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

Example 1:
Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].

Example 2:
Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
Explanation: There are three critical points:
- [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.

Example 3:
Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
Explanation: There are two critical points:
- [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.

Constraints:
    The number of nodes in the list is in the range [2, 10^5].
    1 <= Node.val <= 10^5

Hint 1
The maximum distance must be the distance between the first and last critical point.

Hint 2
For each adjacent critical point, calculate the difference and check if it is the minimum distance.
"""
from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        crit_points = []
        ans = []
        i = 1
        while head.next.next is not None:
          prev = head 
          head = head.next
          i += 1

          if head.val > prev.val and head.val > head.next.val:
              crit_points.append(i)
          elif head.val < prev.val and head.val < head.next.val:
              crit_points.append(i)   

        if len(crit_points) > 1:
            minDistance = crit_points[-1] - crit_points[0]
            maxDistance = crit_points[-1] - crit_points[0]
            for i in range(1, len(crit_points)):
              distance = crit_points[i] - crit_points[i-1]
              minDistance = min(minDistance, distance)
            ans = [minDistance, maxDistance]
        else:
          ans = [-1, -1]
        
        return ans

# head = [3,1]
# head = [5,3,1,2,5,1,2]
head = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
solution = Solution()
print(solution.nodesBetweenCriticalPoints(head))
