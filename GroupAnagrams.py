def groupAnagrams(strs):
    output = []
    dict  = {}
    for str in strs: # Complexity of O(m)
        sorted_str = sorted(str) # Complexity of O(nlogn)
        sorted_str = ''.join(sorted_str)
        if sorted_str in dict:
            dict[sorted_str].append(str)
        else:
            dict[sorted_str]=[str]

    for key in dict:
        output.append(dict[key])

    return output



groupAnagrams(['a'])

#     output = []
#     flag_1 = flag_2 = None
#     i = 0
#
#
#     for str in strs:
#         flag_2 = False
#         for j in range(len(output)):
#             if str in output[j]:
#                 flag_2 = True
#         if flag_2:
#             continue
#         output.append([str])
#         strs.pop(0)
#         for str1 in strs:
#             flag_1 = True
#             if str1 == str:
#                 continue
#             for char in str:
#                 if char not in str1:
#                     flag_1 = False
#             if flag_1:
#                  output[i].append(str1)
#         i  = i + 1
#
#     return output
# print(groupAnagrams(["",""]))

