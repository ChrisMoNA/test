# 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：

# -2：向左转 90 度
# -1：向右转 90 度
# 1 <= x <= 9：向前移动 x 个单位长度
# 在网格上有一些格子被视为障碍物。

# 第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])

# 机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。

# 返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。

# 示例 1：

# 输入: commands = [4,-1,3], obstacles = []
# 输出: 25
# 解释: 机器人将会到达 (3, 4)
# 示例 2：

# 输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# 输出: 65
# 解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/walking-robot-simulation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def robotSim01(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        
        # 建立方向字典
        location = {
            'up': {0:[0,1],-1:'right',-2:'left'}, #向上走一步，后面可以转方向，
            'down': {0:[0,-1],-1:'left',-2:'right'}, #向下走一步，后面可以转方向，向下的左转是往右
            'left': {0:[-1,0],-1:'up',-2:'down'}, #向左走一步，后面可以转方向,左转的左转即往下
            'right': {0:[1,0],-1:'down',-2:'up'} #向右走一步，后面可以转方向，右转的右转即往下
        }

        # 默认方向
        loc = 'up'
 
        # 初始坐标轴
        loc_xy = [0,0] 

        # 距离最大值
        res = 0

        # 障碍物坐标
        obstacles = set(map(tuple, obstacles))

        print(set(map(tuple, obstacles)))

        for command in commands:
            if command < 0:
               loc = location[loc][command]
            else:
                # 一步一步地走
                # range不包括最末尾的那一个，所以+1
                for i in range(1, command + 1):
                    loc_x, loc_y = loc_xy[0], loc_xy[1]
                    loc_x += location[loc][0][0]
                    loc_y += location[loc][0][1]

                    # 遇见障碍物
                    if (loc_x, loc_y) in obstacles:
                        break
                    loc_xy = [loc_x, loc_y]
                    # print(loc_xy)

                res = max(res, loc_xy[0]**2 + loc_xy[1]**2)

        return res

    def robotSim02(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """

        x_y = ((0, 1), (1, 0), (0, -1), (-1, 0))
        di, x, y = 0, 0, 0
        distance = 0
        obs_dict = {}
        # 这一步很重要，因为后面有很多次需要进行判断是否存在
        # list的查找的复杂度明显高于dict的O(1)，提前转，节省很多消耗
        for obs in obstacles:
            obs_dict[tuple(obs)] = 0
        for com in commands:
            if com == -2:
                di = (di + 3)%4 # 左转，画闭环图
            elif com == -1:
                di = (di + 1)%4 # 右转，画闭环图
            else:
                for j in range(com):
                    dx, dy = x_y[di]
                    next_x = x + dx
                    next_y = y + dy
                    if (next_x, next_y) in obs_dict:
                        break
                    x, y = next_x, next_y
                    distance = max(distance, x*x + y*y)
        return distance


    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """

        x,y = 0, 0 # 坐标轴起始点
        dx, dy = 0, 1 # 速度，因为开始时方向向上，dy初始速度为1

        distance = 0 # 计算距离
        obs_dict = {} # 字典，存储障碍

        for obs in obstacles:
            obs_dict[tuple(obs)] = 0
        for com in commands:
            if com == -2:
                dx, dy = -dy, dx # 左转，画坐标图可以理解
            elif com == -1:
                dx, dy = dy,-dx # 右转，
            else:
                for i in range(com):
                    next_x = x + dx
                    next_y = y + dy
                    if (next_x, next_y) in obs_dict:
                        break
                    x = next_x
                    y = next_y
                    distance = max(distance, x**2 + y**2)

        return distance
            


        
commands = [8,-1,8,-1,4,-1,5] #[4,-1,3] #[4,-1,4,-2,4]
obstacles = [[2,8]] #[[2,4]]


test = Solution()

print(test.robotSim(commands,obstacles))

