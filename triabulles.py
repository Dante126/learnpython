

liste = [7, 5, 8, -1, 12, 3, 5]

def echange(l, pos1, pos2):
    temp = l[pos1]
    l[pos1] = l[pos2]
    l[pos2] = temp

def tri(l):
    pas_trie = True
    while pas_trie:
        pas_trie = False
        for i in range(0, len(l)-1):
            print(i, liste)
            if l[i] > l[i+1]:
                echange(l, i, i+1)
                pas_trie = True

tri(liste)