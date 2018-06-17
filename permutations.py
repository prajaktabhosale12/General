import os

class Examples(object):
    def __init__(self):
        self.string_list = set()

    def permute(self, s, l, r):
        if s not in self.string_list:
            self.string_list.add(s)

        for i in range(l, r):
            s = self.swap_chars(l, i, s)
            self.permute(s, l+1, r)
            s = self.swap_chars(l, i, s) #BACKTRACKING

        return s 

    def swap_chars(self, i, j, s):
        s = list(s)
        s[j], s[i] = s[i], s[j]
        return "".join(s)
        #O(n*n!)








def main():
    ex = Examples()
    s = "abcd"
    ex.permute(s, 0, len(s))
    for a in ex.string_list:
        print(a)


if __name__ == "__main__":
    main()