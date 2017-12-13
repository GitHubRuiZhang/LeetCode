# python3
# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# click to show corner cases.

# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".


# My solution
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        cur = []
        direct = [p for p in path.split('/') if p != '.' and p != '']
        for p in direct:
            if p == '..':
                if len(cur) > 0:
                    cur.pop()
            else:
                cur.append(p)
        return "/" + "/".join(cur)