class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # from math import log, ceil
        next_power = 2 ** ceil(log(len(nums))/log(2))
        # print(next_power)
        min_value = min(nums)
        segment_tree = [min_value] * (2*next_power-1)
        # print(len(segment_tree))

        def construct_tree(low, high, position):
            if low == high:
                segment_tree[position] = nums[low]
                return
            else:
                mid = (low + high)//2
                construct_tree(low, mid, 2*position + 1)
                construct_tree(mid + 1, high, 2*position + 2)
                segment_tree[position] = max(segment_tree[2*position + 1], segment_tree[2*position + 2])
                return

        construct_tree(0, len(nums) - 1, 0)
        # print(segment_tree)
        def query_tree(q_low, q_high, low, high, pos):
            if q_high < low or q_low > high:
                # No overlap
                return min_value
            elif low >= q_low and high <= q_high:
                # Complete overlap
                return segment_tree[pos]
            else:
                # partial overlap look both sides
                mid = (low + high)//2
                return max(query_tree(q_low, q_high, low, mid, 2 * pos + 1), query_tree(q_low, q_high, mid+1, high, 2 * pos + 2))

        k -= 1
        res = []
        for i in range(len(nums)):
            if i + k >= len(nums):
                break
            else:
                # print(i, i + k)
                if i!=0 and res[-1] <= nums[i+k]:
                    res.append(nums[i+k])
                elif i!= 0 and res[-1] != nums[i-1]:
                    res.append(res[-1])
                else:
                    res.append(query_tree(i, i + k, 0, len(nums)-1, 0))
        return(res)