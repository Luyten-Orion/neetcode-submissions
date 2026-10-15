class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid_chars = "abcdefghijklmnopqrstuvwxyz.+"
        emails = list(map(lambda x: x.split('@'), emails))
        print(emails)
        for eidx in range(len(emails)):
            emails[eidx][0] = emails[eidx][0].split('+', maxsplit=2)[0].replace('.', '')
        emails = set(map(lambda x: "@".join(x), emails))
        return len(emails)