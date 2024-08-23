def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    len_s = 0
    len_t = 0

    while (len_s < len(s) and len_t < len(t)):
        if s[len_s] == t[len_t]:
            len_s += 1
        len_t += 1
    
    if len(s) == len_s:
        return True
    return False

#isSubsequence("abc", "ahbgdc")
isSubsequence("axc", "ahbgdc")