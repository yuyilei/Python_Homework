s = 'abcdef'
i = -1
for i in [None] + range( -1 ,-len(s) ,-1):
    print s[:i]
