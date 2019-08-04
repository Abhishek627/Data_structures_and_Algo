#!/bin/python
'''
Problem from string interview track of hackerrrank
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&
playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
'''

from collections import Counter


# Complete the isValid function below.
def isValid(s):
    count = Counter(s)
    val_list = list(count.itervalues())
    val_count = Counter(val_list)
    if len(val_count) < 2:
        return "YES"

    if len(val_count) == 2:
        inverted_map = {v: k for k, v in val_count.iteritems()}
        if 1 in val_count and val_count[1] == 1:
            return "YES"

        key_list = list(val_count)

        if 1 in inverted_map and abs(key_list[0] - key_list[1]) == 1:
            return "YES"

    return "NO"


if __name__ == '__main__':
    assert isValid(
        "ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebf"
        "baieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd") == "YES"
    assert isValid("abcdefghhgfedecba") == "YES"
    assert isValid("aabbccddeefghi") == "NO"
    assert isValid("aabbcd") == "NO"

    assert isValid("aaaabbcc") == "NO"
