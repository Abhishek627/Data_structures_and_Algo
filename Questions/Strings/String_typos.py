'''
https://www.hiredintech.com/classrooms/algorithm-design/lesson/27/task/25
'''


def is_diff2(w,W):
    if len(w) == len(W) and sum(a != b for a, b in zip(w, W)) <= 2:
        return True
    return False


def can_add_remove(w, W):
    # Beautiful
    if len(w) == len(W) + 1:
        return any(w[:i] + w[i + 1:] == W for i in range(len(w)))
    elif len(w) == len(W) - 1:
        return any(W[:i] + W[i + 1:] == w for i in range(len(W)))
    else:
        return False

def check_string(W,T):
    cnt = 0
    for word in T.split():
        if is_diff2(word,W) or can_add_remove(word,W):
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    W= 'banana'
    T= 'there are three bananas on the tree and one banano on the ground and a banana'
    check_string(W,T)