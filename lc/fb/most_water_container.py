def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    water = 0
    head = 0
    n = len(height)
    tail = n - 1

    for cnt in range(n):

        width = abs(head - tail)

        if height[head] < height[tail]:   
            res = width * height[head]
            head += 1
        else:
            res = width * height[tail]
            tail -= 1

        if res > water:
            water = res

    return water

height = [1,8,6,2,5,4,8,3,7,1]
print(height)
print(maxArea(height))

height = [1,1]
print(height)
print(maxArea(height))
