def find(s, substring):
    index = 0

    if substring in s:
        i = substring[0]
        for sub in s:
            if sub == i:
                if s[index:index+len(substring)] == substring:
                    return index
            index += 1
    return -1

def find_multi(s,substring):
    index=0
    indices=[]

    if substring in s:
        i = substring[0]
        for sub in s:
            if sub == i:
                if s[index:index+len(substring)] == substring:
                    indices.append(index)
            index += 1
    return indices

