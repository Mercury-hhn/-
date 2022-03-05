import demo

# 重置游戏
class Reset():
    def __init__(self, screen):
        self.screen = screen
    def main(self , type = 0):
        if demo.Role.time_type == 1:
            demo.Role.time = 60
        demo.Role.one_person_controlled_number = 0
        demo.Role.two_person_controlled_number = 0
        demo.Role.one_person_blood = 100 * demo.Role.life
        demo.Role.two_person_blood = 100 * demo.Role.life
        demo.Role.one_person_blue = 100 * demo.Role.energy
        demo.Role.two_person_blue = 100 * demo.Role.energy
        demo.dart_img = []
        demo.ultkulou_img = []
        demo.ultimate_skill_img = []
        if type == 1:
            demo.player_one_jump.obstacle = []
            demo.player_two_jump.obstacle = []
            demo.Role.one_person_name = 'golem_1'
            demo.Role.two_person_name = 'golem_2'
            demo.Role.one_person_stand_img = []
            demo.Role.one_person_walk_img = []
            demo.Role.one_person_attack_img = []
            demo.Role.one_person_hurt_img = []
            demo.Role.two_person_stand_img = []
            demo.Role.two_person_walk_img = []
            demo.Role.two_person_attack_img = []
            demo.Role.two_person_hurt_img = []
            demo.Role.orange_img = []
        # 默认移动速度
        demo.Role.speed = 15
        demo.Role.one_person_skill = False  # 被动技能
        demo.Role.two_person_skill = False
        # 大招状态True释放，False不释放
        demo.Role.one_person_ultimate_skill = False
        demo.Role.two_person_ultimate_skill = False
        demo.Role.deduct_dart_blue = 5  # 飞镖扣除蓝条
        demo.Role.deduct_dart_blood = 5  # 飞镖扣除血条
        demo.Role.deduct_attack_blood = 5  # 普攻扣除血条
        demo.Role.deduct_attack_blue = 5  # 普攻回复蓝条
        # 大招扣除血量
        demo.Role.deduct_ultimate_skill_blood = 1
        # 大招扣除蓝量
        demo.Role.deduct_ultimate_skill_blue = 50

        demo.Role.deduct_orange = 0.5  # 按键回复爆气条的值
        demo.Role.deduct_white = 40  # 加减爆气格

        # 角色一
        # 角色x位置
        demo.Role.one_person_x = demo.one_person_x
        # 角色y位置
        demo.Role.one_person_y = demo.one_person_y
        # 角色宽度
        demo.Role.one_person_width = demo.one_person_width
        # 角色高度
        demo.Role.one_person_height = demo.one_person_height
        # 角色朝左
        demo.Role.one_person_left = False
        # 角色朝右，True即默认为朝右
        demo.Role.one_person_right = True
        # 角色站立状态，True即默认战立
        demo.Role.one_person_stand = True
        # 角色跳跃状态
        demo.Role.one_person_jump = False
        # 角色攻击状态
        demo.Role.one_person_attack = False
        # 角色扔飞镖状态
        demo.Role.one_person_dart = False
        # 角色防御状态
        demo.Role.one_person_defense = False
        # 角色攒爆气状态
        demo.Role.one_person_bring_orange = False

        # 角色1跳跃高度
        demo.Role.one_person_jump_t = 10

        # 角色读取列表默认第一张图片   读取走动图片
        demo.Role.one_person_walk_num = 0
        demo.Role.one_person_walk_allnum = 24
        # 读取静止图片
        demo.Role.one_person_stand_num = 0
        demo.Role.one_person_stand_allnum = 18
        # 读取攻击图片
        demo.Role.one_person_attack_num = 0
        demo.Role.one_person_attack_allnum = 7
        # 受到伤害图片
        demo.Role.one_person_hurt_num = 0
        demo.Role.one_person_hurt_allnum = 12
        # 攒爆气图片
        demo.Role.one_person_orange_num = 0
        demo.Role.one_person_orange_allnum = 6
        # # 起跳图片
        # demo.Role.one_jump = 0

        # 角色一爆气量
        demo.Role.one_person_orange = 0
        demo.Role.one_person_white = 40  # 角色一爆气格
        # 角色被控制状态
        demo.Role.one_person_controlled = False
        demo.Role.one_person_attack_attacknum = 0  # 普攻次数

        # 角色二
        demo.Role.two_person_x = demo.two_person_x
        demo.Role.two_person_y = demo.two_person_y
        demo.Role.two_person_width = demo.two_person_width
        demo.Role.two_person_height = demo.two_person_height
        demo.Role.two_person_left = True
        demo.Role.two_person_right = False
        demo.Role.two_person_stand = True
        demo.Role.two_person_jump = False
        demo.Role.two_person_attack = False
        demo.Role.two_person_dart = False
        demo.Role.two_person_defense = False
        demo.Role.two_person_bring_orange = False
        demo.Role.two_person_jump_t = 10
        demo.Role.two_person_img = 1
        # 角色二爆气量
        demo.Role.two_person_orange = 0
        demo.Role.two_person_white = 40  # 角色二爆气格
        demo.Role.two_person_controlled = False
        # 角色读取列表默认第一张图片
        # 读取走动图片
        demo.Role.two_person_walk_num = 0
        demo.Role.two_person_walk_allnum = 24
        # 读取静止图片
        demo.Role.two_person_stand_num = 0
        demo.Role.two_person_stand_allnum = 18
        # 读取攻击图片
        demo.Role.two_person_attack_num = 0
        demo.Role.two_person_attack_allnum = 7
        # 受到伤害图片
        demo.Role.two_person_hurt_num = 0
        demo.Role.two_person_hurt_allnum = 12
        # 攒爆气图片
        demo.Role.two_person_orange_num = 0
        demo.Role.two_person_orange_allnum = 6
        self.screen.fill((0,0,0))