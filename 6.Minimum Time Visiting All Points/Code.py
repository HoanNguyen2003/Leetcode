class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        # count = 0

        # # Giả sử points là một danh sách chứa các điểm (x, y)
        # for i in range(len(points) - 1):
        #     x = points[i][0]
        #     y = points[i][1]
        #     x_next = points[i+1][0]
        #     y_next = points[i+1][1]

        #     while x != x_next or y != y_next:  # Sửa lại điều kiện vòng lặp
        #         new1 = (((x_next - (x + 1)) ** 2 + (y_next - y) ** 2) ** 0.5)
        #         new2 = (((x_next - x) ** 2 + (y_next - (y + 1)) ** 2) ** 0.5)
        #         new3 = (((x_next - (x + 1)) ** 2 + (y_next - (y + 1)) ** 2) ** 0.5)
        #         new4 = (((x_next - (x - 1)) ** 2 + (y_next - (y + 1)) ** 2) ** 0.5)
        #         new5 = (((x_next - (x - 1)) ** 2 + (y_next - (y - 1)) ** 2) ** 0.5)
        #         new6 = (((x_next - (x + 1)) ** 2 + (y_next - (y - 1)) ** 2) ** 0.5)
        #         new7 = (((x_next - (x - 1)) ** 2 + (y_next - y) ** 2) ** 0.5)
        #         new8 = (((x_next - x) ** 2 + (y_next - (y - 1)) ** 2) ** 0.5)

        #         # Tìm giá trị nhỏ nhất và thay đổi tọa độ
        #         min_value = min(new1, new2, new3, new4, new5, new6, new7, new8)
                
        #         if min_value == new1:
        #             x = x + 1
        #             count += 1
        #         elif min_value == new2:
        #             y = y + 1
        #             count += 1
        #         elif min_value == new3:
        #             x = x + 1
        #             y = y + 1
        #             count += 1
        #         elif min_value == new4:
        #             x = x - 1
        #             y = y + 1
        #             count += 1
        #         elif min_value == new5:
        #             x = x - 1
        #             y = y - 1
        #             count += 1
        #         elif min_value == new6:
        #             x = x + 1
        #             y = y - 1
        #             count += 1
        #         elif min_value == new7:
        #             x = x - 1
        #             count += 1
        #         elif min_value == new8:
        #             y = y - 1
        #             count += 1

        # return count

        total_time = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            
            # Tính thời gian di chuyển giữa 2 điểm
            x_diff = abs(x2 - x1)
            y_diff = abs(y2 - y1)
            
            # Thời gian di chuyển tối thiểu là max(x_diff, y_diff)
            total_time += max(x_diff, y_diff)
        
        return total_time

        
points = [[1,1],[3,4],[-1,0]]
run = Solution()
print(run.minTimeToVisitAllPoints(points))