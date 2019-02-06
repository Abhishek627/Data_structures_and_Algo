'''
String matching algorithm based on rolling hash concept


'''

def get_mod(a,p):
    return (a %p + p ) % p

def rabin_karp(text, pattern , prime=101 , base= 256):
    '''

    :param text:
    :param pattern:
    :return: Number of occurrences and start indexes of the matches
    '''


    h_pat = 0
    h_txt=0
    for i in range(len(pattern)):
        h_pat = get_mod(h_pat * base + ord(pattern[i]) ,prime)
        h_txt = get_mod(h_txt * base + ord(text[i]), prime)

    # Now slide over the text, use rolling hash and compare character by character only in case of hash match

    i=0
    N= len(text)
    M = len(pattern)
    E = get_mod(base**(M-1),prime)
    while (i <= N-M):
        if h_pat == h_txt:
            for j in range(M):
                if text[i+j] != pattern[j]:
                    break
                if j == M-1:
                    print "Match found at index ", i
        else:
            if i< N-M:
                # Update hash value here
                h_txt = get_mod(h_txt- get_mod(ord(text[i-M])*E,prime),prime)
                h_txt = get_mod(h_txt* base, prime)
                h_txt = get_mod(h_txt+ ord(text[i]),prime)
        i+=1


if __name__ == '__main__':
    # rabin_karp('GEEKS FOR GEEKS', 'GEEKS')
    rabin_karp('babalabalabalatheend', 'alabala')

    print "*****************************"
    rabin_karp('ABABDABACDABABCABAB','ABAB')


