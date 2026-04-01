from typing import List
from collections import deque, defaultdict

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        def bfs(curr):
            q = deque()
            q.append(curr)
            island = []  # add every square of the island into a list
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            while q:
                m, n = q.pop()
                if grid[m][n] == 0:
                    continue

                grid[m][n] = 0
                island.append([m, n])

                for direction in directions:
                    new_m = m + direction[0]
                    new_n = n + direction[1]
                    if new_m >= 0 and new_m < len(grid) and new_n >= 0 and new_n < len(grid[0]) and grid[new_m][new_n] == 1:
                        q.append([new_m, new_n])

            # once q goes through everything, check for other matching islands and 0 them out
            origin_m, origin_n = curr[0], curr[1]
            offsets = []
            for m, n in island:
                if m == origin_m and n == origin_n:
                    continue
                offsets.append([m - origin_m, n - origin_n])

            # check every possible one around the grid
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] != 1:
                        continue

                    valid = True
                    for dm, dn in offsets:
                        check_m = i + dm
                        check_n = j + dn
                        if check_m >= 0 and check_m < len(grid) and check_n >= 0 and check_n < len(grid[0]) and grid[check_m][check_n] == 1:
                            continue
                        else:
                            valid = False
                            break

                    if valid:
                        # incorporate another queue at the end to see if there are any surrounding 1s
                        # to the translated island, if there are then DO NOT 0 out

                        check_q = deque()
                        translated = set()
                        translated.add((i, j))
                        for dm, dn in offsets:
                            translated.add((i + dm, j + dn))

                        check_q.append([i, j])
                        for dm, dn in offsets:
                            check_q.append([i + dm, j + dn])

                        surrounding_one = False
                        while check_q:
                            cm, cn = check_q.pop()
                            for direction in directions:
                                nm = cm + direction[0]
                                nn = cn + direction[1]
                                if nm >= 0 and nm < len(grid) and nn >= 0 and nn < len(grid[0]):
                                    if (nm, nn) not in translated and grid[nm][nn] == 1:
                                        surrounding_one = True
                                        break
                            if surrounding_one:
                                break

                        if surrounding_one:
                            continue

                        grid[i][j] = 0
                        for dm, dn in offsets:
                            grid[i + dm][j + dn] = 0

        res = 0

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    res += 1
                    bfs([x, y])

        return res