'''
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.
'''

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        dic = {}
        for item in items:
            if item[0] in dic:
                dic[item[0]].append(item[1])
            else:
                dic[item[0]] = [item[1]]

        res = []
        for k in dic.keys():
            res.append([k, int(sum(sorted(dic[k])[-5:])/5)])
        return res





