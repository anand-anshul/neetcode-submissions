class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            email = email.split("@")
            local = email[0]
            domain = email[1]
            local = local.split('+')[0]
            local = local.split('.')
            local = "".join(local)
            email = local + '@' + domain
            seen.add(email)

        return len(seen)