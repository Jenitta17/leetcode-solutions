class Solution(object):
    def simplifyPath(self, path):
        parts = path.split("/")
        stack = []
        for p in parts:
            if p == "" or p == ".":
                continue
            elif p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)
