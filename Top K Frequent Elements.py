nums = [1,1,1,1,1,1,1,2,3,3,3,5,5,6,6,6,6,6,6,6,6,6,6,6]
k = 3
# This is a naive solution:
# def topKFrequent(nums: list[int], k: int) -> list[int]:
#     final = {}
#     nums.sort()
#     freq = 0
#
#     for i in range(len(nums)):
#         if i == 0:
#             freq = 1
#             continue
#         else:
#             if nums[i] == nums[i - 1]:
#                 freq = freq + 1
#                 if i == len(nums) - 1:
#                     final.update({nums[i - 1]: freq})
#                 continue
#             else:
#                 final.update({nums[i - 1]: freq})
#                 if i == len(nums) - 1:
#                     final.update({nums[i]: 1})
#                 freq = 1
#                 continue
#     final_sorted_dic = dict(sorted(final.items(), key=lambda item:item[1],reverse=True))
#     print (list(final_sorted_dic.keys())[:k])
#     return list(final_sorted_dic.keys())[:k]
#
# his method gives us nlogn time
# topKFrequent(nums,k)

def topKFrequent(nums: list[int], k: int) -> list[int]:
        freq = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for key, value in freq.items():
            buckets[value].append(key)
        res = []
        for i in range(len(buckets) -1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res

print(topKFrequent(nums,k))