'''
String matching algorithm based on longest proper suffix concept
resources:

http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/
https://www.youtube.com/watch?v=t4xUA-aHzy8
'''

#Todo: Handle overlapping cases
def lps_array(pattern):
    j = 0
    i = 1
    lps = [0] * len(pattern)
    while (i < len(pattern)):
        if pattern[i] == pattern[j]:
            lps[i] = lps[j] + 1
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp(text, pattern):
    '''

    :param text:
    :param pattern:
    :return: Number of occurrences and end indexes of the matches
    '''

    len_pattern = len(pattern)
    len_text = len(text)
    if len_text < len_pattern:
        return 0
    # Check for corner cases where len of either is zero
    lps = lps_array(pattern)

    # Start matching now. Use lps in case of mismatch
    i = j = 0

    num_matches = 0
    match_indices= []
    while (i < len_text and j < len_pattern):

        if text[i] == pattern[j]:
            i+=1
            j+=1

            if j == len_pattern:
                # Match found. reset j for finding more matches
                num_matches += 1
                j = lps[j - 1]
                match_indices.append(i-j)

        else:
            if j !=0 :
                j= lps[j-1]
            else:
                i+=1

    return num_matches, match_indices


if __name__ == '__main__':
    print kmp('babalabalabalatheend', 'alabala')

    print kmp('ABABDABACDABABCABAB','ABAB')

    print kmp('babalabalabalatheend','alabala')
    # Should give 2 as result but will give 1 as the patterns are overlapping