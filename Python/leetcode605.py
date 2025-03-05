from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    if not flowerbed:
        return False

    remaining_n = n
    flowerbed = [0] + flowerbed + [0]
    for i in range(1,len(flowerbed)-1):
        # print(flowerbed[i])
        if flowerbed[i] == 0:
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                print(flowerbed[i-1],flowerbed[i+1])
                remaining_n -= 1
                flowerbed[i] = 1

    if remaining_n <= 0:
        return True
    else:
        return False

flowerbed = [0,0,1,0,0]
n = 1
print(canPlaceFlowers(flowerbed,n))