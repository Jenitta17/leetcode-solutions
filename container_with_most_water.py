class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        best = 0
        while left < right:
            width = right - left
            if height[left] < height[right]:
                h = height[left]
            else:
                h = height[right]
            area = width * h
            if area > best:
                best = area
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return best
