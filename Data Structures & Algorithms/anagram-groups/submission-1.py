class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charsMap = {}
        for string in strs:
            charList = [0] * 26
            for char in string:
                # index = ord(char) - 96 - 1 # 0 index
                index = ord(char) - ord('a')
                charList[index] = charList[index] + 1
            
            key = tuple(charList)
            if key in charsMap:
                # print(key)
                # print(charsMap[key])
                charsMap[key].append(string)
                # print(charsMap[key])
            else:
                charsMap[key] = [string]
        
        # print(list(charsMap.values()))
        return list(charsMap.values())

        # result = []
        # for key, value in charsMap.items():
        #     result.append(value)

        # return result