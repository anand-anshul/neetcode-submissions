class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        mail2acc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in mail2acc:
                    union(i, mail2acc[e])
                else: 
                    mail2acc[e] = i

        mailGroup = defaultdict(list)
        for e, i in mail2acc.items():
            leader = find(i)
            mailGroup[leader].append(e)

        res = []
        for i, emails in mailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(mailGroup[i]))

        return res
        
        



