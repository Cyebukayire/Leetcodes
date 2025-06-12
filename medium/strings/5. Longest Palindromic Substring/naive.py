
def allSubstrings(s:str) -> list[str]:  # time: O(n^3), space: O(n^3)
    res = []
    for i in range(len(s)):
        j = len(s)
        while j > i:
            res.append(s[i:j])
            j -= 1
    print(res)
    return list(set(res))

def isPalindrome(s:str) -> bool: # Time: O(n^2), space: O(n)
    if len(s) <= 1:
        return True

    reversed = ''
    s = s.lower()
    
    for i in range(len(s) - 1, -1, -1):
        reversed += s[i]
    
    return reversed == s

def longestPalindrome(s:str):
    # First check if s is already a palindrome
    if(isPalindrome(s) or len(s) < 2):
        return s
    
    allsubstr = allSubstrings(s)

    # Collect all palindromes
    palindromes = []
    for substr in allsubstr:
        if(isPalindrome(substr)):
            palindromes.append(substr)
    print("Palindromes: ",palindromes)
    
    # Find and return longest palindrome
    size = 0
    res = ''
    for pal in palindromes:
        if len(pal) > size:
            size = len(pal)
            res = pal
    return res

# res = allSubstrings("banana")
# s = "ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"
# print(longestPalindrome(s))
s = "ana"
print(allSubstrings(s))

