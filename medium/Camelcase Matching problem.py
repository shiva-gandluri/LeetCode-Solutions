class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        flag = 1
        answer = []
        for query in queries:
            i, j = 0,0
            while(i < len(query)):
                if(j < len(pattern) and query[i] == pattern[j]):
                    i+=1
                    j+=1
                elif(ord('Z')>=ord(query[i])>=ord('A')):
                    flag = 0
                    break
                else:
                    i+=1
            if(flag==1 and j==len(pattern)):
                answer.append(True)
            else:
                answer.append(False)
            flag = 1
        return(answer)
