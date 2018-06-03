def trim(s):
    n = 0
    p = 0
    for x in s:
        if x != ' ':
            break
        n = n + 1
    m = s[n:]
    for x in m:
        if x == ' ':
            break
        p = p + 1
    s = s[n:n+p]
    return s
#去除字符串首为两端的空格
