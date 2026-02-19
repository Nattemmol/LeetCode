class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            l = 0
            r = len(image[0])-1
            while l < r:
                image[i][r], image[i][l] = image[i][l], image[i][r]
                l += 1
                r -= 1

        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 1:
                    image[i][j] = 0
                elif image[i][j] == 0:
                    image[i][j] = 1
        return image
        