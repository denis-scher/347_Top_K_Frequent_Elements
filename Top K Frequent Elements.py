

nums = [1,2]
k = 2

def topKFrequent(nums: list[int], k: int) -> list[int]:
    final = {}
    nums.sort()
    freq = 0

    for i in range(len(nums)):
        if i == 0:
            freq = 1
            continue
        else:
            if nums[i] == nums[i - 1]:
                freq = freq + 1
                if i == len(nums) - 1:
                    final.update({nums[i - 1]: freq})
                continue
            else:
                final.update({nums[i - 1]: freq})
                if i == len(nums) - 1:
                    final.update({nums[i]: 1})
                freq = 1
                continue
    final_sorted_dic = dict(sorted(final.items(), key=lambda item:item[1],reverse=True))
    print (list(final_sorted_dic.keys())[:k])
    return list(final_sorted_dic.keys())[:k]


topKFrequent(nums,k)