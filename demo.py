# 导入模块
#import random
import pygame,sys

import demo
import ult
import drawbar
import button
import player
import select
import darts
import course
import timing
import hinder
import about
import resetting
import gas
  # 引入time模块
# 视频编辑模块
# from moviepy.editor import VideoFileClip

# 窗口宽度，高度
display_width = 1920
display_height = 1080

# 帧数
fps = 24
fclock = pygame.time.Clock()

# 自定义颜色RGB代码
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 菜单背景图片路径
bg_location = 'images/主菜单.png'
# 选角色背景图片路径
bg_location2 = 'images/角色头像/bgdz.png'
# 载入菜单背景图片
bg = pygame.image.load(bg_location)
# 载入选角色背景图片
bg2 = pygame.image.load(bg_location2)
bg2 = pygame.transform.scale(bg2, [1920, 1080])
# 背景动图图片路径
dtbg = []
count = 0

# 飞镖图片列表
dart_img = []
# 终极技能列表
ultimate_skill_img = []  # 龙
gas_img = []  # 爆气

# 初始化
pygame.init()

# 定义一个pause变量，若为True则弹出菜单否则关闭
pause = False

# 创建一个全屏的窗口并赋值给变量screen
screen = pygame.display.set_mode([display_width, display_height],pygame.FULLSCREEN)# , pygame.FULLSCREEN 表示全屏幕

# 定义一个mainbool变量，若为True则开始游戏，否则暂停游戏
mainbool = False
timeoverbool = False
# 角色一的全局变量
# 角色初始x位置
one_person_x = 100
# 角色初始y位置
one_person_y = 800
# 角色宽度
one_person_width = 90
# 角色高度
one_person_height = 125


# 角色二的全局变量
# 角色初始x位置
two_person_x = 1500
# 角色初始y位置
two_person_y = 800
# 角色宽度
two_person_width = 90
# 角色高度
two_person_height = 125

# # 创建存入角色动作图片的列表
# one_person_stand_img = []
# one_person_walk_img = []
# one_person_attack_img = []
# one_person_hurt_img = []
# # one_jump_start_img = []
# two_person_stand_img = []
# two_person_walk_img = []
# two_person_attack_img = []
# two_person_hurt_img = []
# # two_jump_start_img = []


# 加载角色初始化位置，高度
Role = player.Role(screen,one_person_x,one_person_y,one_person_width,one_person_height,two_person_x,two_person_y,two_person_width,two_person_height)
# 导入音乐
# 1.背景
pygame.mixer.init()
pygame.mixer.music.load("sound/背景音效.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1,0)
# 2.音效的函数
def Sound(src):
    sound = pygame.mixer.Sound(src)
    sound.set_volume(2.5)
    sound.play()

bg_location3 = pygame.image.load('images/背景/1-min.png')
# 定义一个游戏里界面的背景函数
def backgroundimg():
    bg = bg_location3
    # 填充
    bg = pygame.transform.scale(bg,[1920,1080])
    screen.blit(bg, (0, 0))

# 定义一个开始菜单函数
def starting_screen(game_start=False,type=0):
    # 引入全局变量mainbool
    global mainbool
    global timeoverbool
    # 修改全局变量mainbool的值为False，则暂停游戏显示菜单
    mainbool = False
    # 绘制菜单背景
    volume = True
    # 从系统字体库创建一个 Font 对象
    font = pygame.font.Font('other/字魂4550号-芝麻体.TTF', 50)

    # score_str为菜单头部显示文字
    # 如果type值为1
    if type == 1:
        # 菜单头部显示的
        score_str = '玩家二获胜'
        game_title = font.render(score_str, True, WHITE)
    # 如果type值为2
    elif type == 2:
        score_str = '玩家一获胜'
        game_title = font.render(score_str, True, WHITE)
    # 否则
    else:
        game_title = font.render('', True, WHITE)

    # 绘制菜单标题文字，文字居中距头部150px


    # 初始化按钮类
    if game_start:
        play_button = button.Button(screen,'Play', 1, display_width, display_height, None, 700, centered_x=True)
        doc_button = button.Button(screen, 'Doc', 1, display_width, display_height, None, 800, centered_x=True)
        about_button = button.Button(screen, 'About', 1, display_width, display_height, None, 900, centered_x=True)
    else:
        play_button = button.Button(screen, 'Continue', 1, display_width, display_height, None, 700, centered_x=True)
        menu_button = button.Button(screen, 'Menu', 1, display_width, display_height, None, 800, centered_x=True)
    exit_button = button.Button(screen,'Exit', 1, display_width, display_height, None, 900, centered_x=True)
    volume_button = button.Button(screen,'Volume', 1, display_width, display_height, None, 1000, centered_x=True)

    # 调用绘制按钮类里的display方法，使按钮显示出来
    play_button.display()
    if game_start == False:
        menu_button.display()
    else:
        doc_button.display()
        about_button.display()
    exit_button.display()
    volume_button.display()

    # 更新显示
    pygame.display.update()

    # 循环j
    while True:
        screen.blit(bg, (0, 0))
        screen.blit(game_title, (display_width // 2 - game_title.get_width() // 2, 150))
        # 判断鼠标是否指向play按钮，改变按钮颜色
        if play_button.check_click(pygame.mouse.get_pos()):
            if game_start:
                play_button = button.Button(screen, 'Play', 2, display_width, display_height, None, 700,centered_x=True)
            else:
                play_button = button.Button(screen, 'Continue', 2, display_width, display_height, None, 700,centered_x=True)
        else:
            if game_start:
                play_button = button.Button(screen, 'Play', 1, display_width, display_height, None, 700,centered_x=True)
            else:
                play_button = button.Button(screen, 'Continue', 1, display_width, display_height, None, 700,centered_x=True)

        if game_start == False:
            if menu_button.check_click(pygame.mouse.get_pos()):
                menu_button = button.Button(screen, 'Menu', 2, display_width, display_height, None, 800,centered_x=True)
            else:
                menu_button = button.Button(screen, 'Menu', 1, display_width, display_height, None, 800,centered_x=True)
        else:
            if doc_button.check_click(pygame.mouse.get_pos()):
                doc_button = button.Button(screen, 'Doc', 2, display_width, display_height, None, 800, centered_x=True)
            else:
                doc_button = button.Button(screen, 'Doc', 1, display_width, display_height, None, 800, centered_x=True)
            if about_button.check_click(pygame.mouse.get_pos()):
                about_button = button.Button(screen, 'About', 2, display_width, display_height, None, 900,centered_x=True)
            else:
                about_button = button.Button(screen, 'About', 1, display_width, display_height, None, 900,centered_x=True)


        # 判断鼠标是否指向exit按钮，改变按钮颜色
        if exit_button.check_click(pygame.mouse.get_pos()):
            exit_button = button.Button(screen,'Exit', 2, display_width, display_height, None, 900, centered_x=True)
        else:
            exit_button = button.Button(screen,'Exit', 1, display_width, display_height, None, 900, centered_x=True)

        if volume:
            if volume_button.check_click(pygame.mouse.get_pos()):
                volume_button = button.Button(screen, 'Volume', 2, display_width, display_height, None, 900,centered_x=True)
            else:
                volume_button = button.Button(screen, 'Volume', 1, display_width, display_height, None, 900,centered_x=True)
        else:
            if volume_button.check_click(pygame.mouse.get_pos()):
                volume_button = button.Button(screen, 'Volume', 4, display_width, display_height, None, 900,centered_x=True)
            else:
                volume_button = button.Button(screen, 'Volume', 3, display_width, display_height, None, 900,centered_x=True)

        # 更新按钮
        play_button.display()
        if game_start == False:
            menu_button.display()
        else:
            doc_button.display()
            about_button.display()
        exit_button.display()
        volume_button.display()

        pygame.display.update()

        # 循环所有事件
        for event in pygame.event.get():
            # 如果事件类型为退出
            if event.type == pygame.QUIT:
                # 执行退出
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if game_start == False:
                        if menu_button.check_click(pygame.mouse.get_pos()):
                            resetting.Reset(screen).main(1)
                            starting_screen(True)
                            break
                    else:
                        if doc_button.check_click(pygame.mouse.get_pos()):
                            doc = course.Doc(screen)
                            doc.main()
                            break
                        if about_button.check_click(pygame.mouse.get_pos()):
                            about.Team(screen).main()
                            break

                    if volume_button.check_click(pygame.mouse.get_pos()):
                        if volume:
                            volume = False
                            pygame.mixer.music.stop()
                        else:
                            volume = True
                            pygame.mixer.music.play()

                    if exit_button.check_click(pygame.mouse.get_pos()):
                        sys.exit()
        # 如果鼠标左键被按下
            # 判断鼠标是否点击
        if pygame.mouse.get_pressed()[0]:
            if play_button.check_click(pygame.mouse.get_pos()):
                if game_start:
                    select.Choose(screen, bg2).draw()
                    break
                else:
                    if type == 0:
                        mainbool = True
                        break
                    else:
                        resetting.Reset(screen).main()
                        main(True)
                        break

# 碰撞检测角色1
def collision_check(role,a,b):
    if role == 1:
        temp1 = b.x <= a.two_person_x + a.two_person_width <= b.x + b.width
        temp2 = b.y <= a.two_person_y + a.two_person_height <= b.y + b.height

    else:
        temp1 = b.x <= a.one_person_x + a.one_person_width <= b.x + b.width
        temp2 = b.y <= a.one_person_y + a.one_person_height <= b.y + b.height

    return temp1 and temp2

# 碰撞检测角色2
def collision_check2(role,a,b):
    if role == 1:
        temp1 = b.two_person_x <= a.x + a.width <= b.two_person_x + b.two_person_width
        temp2 = b.two_person_y <= a.y + a.height <= b.two_person_y + b.two_person_height
    else:
        temp1 = b.one_person_x <= a.x + a.width <= b.one_person_x + b.one_person_width
        temp2 = b.one_person_y <= a.y + a.height <= b.one_person_y + b.one_person_height
    return temp1 and temp2


# 绘制血条，蓝条，背景，大招
def draw():
    role1 = drawbar.Drawbar(screen, 1, Role.one_person_blood, Role.one_person_blue, Role.one_person_orange,Role.one_person_white)
    role2 = drawbar.Drawbar(screen, 2, Role.two_person_blood, Role.two_person_blue, Role.two_person_orange,Role.two_person_white)
    role1.blood()
    role2.blood()
    role1.blue()
    role2.blue()
    role1.orange()
    role2.orange()
    role1.white()
    role2.white()

    # TODO 修改血量ui
    state = pygame.image.load("./images/新角色/state/带颜色第一版.png")
    srarefan = pygame.transform.flip(state, True, False)  # 水平翻转血条蓝条ui图片
    screen.blit(state, (10, 20))
    screen.blit(srarefan, (1330, 20))

    # TODO 角色头像图片
    juese1 = pygame.image.load("./images/新角色/" + Role.one_person_name + "/head/1.png")
    juese2 = pygame.image.load("./images/新角色/" + Role.two_person_name + "/head/1.png")

    # 水平翻转图片
    juese2fan = pygame.transform.flip(juese2, True, False)  # 水平翻转角色2头像
    screen.blit(juese1, (22, 33))
    screen.blit(juese2fan, (1760, 33))

    hinder.Obstacles().draw(screen)
    Role.draw(screen)
    for dart in dart_img:
        dart.judge(dart)
    # 绘制召唤类大招

    for ultimate_skill in ultimate_skill_img:
        ultimate_skill.judge(ultimate_skill)
    for gas in gas_img:
        gas.judge(gas)
    if Role.one_person_controlled_number > 0:
        Role.one_person_controlled = True
    if Role.two_person_controlled_number > 0:
        Role.two_person_controlled = True




# 游戏结束
def gameover(type = False):
    if type == False:
        if Role.one_person_blood <= 0:
            Sound("sound/男性死亡音效.mp3")
            return 1
        elif Role.two_person_blood <= 0:
            Sound("sound/男性死亡音效.mp3")
            return 2
        else:
            return False
    else:
        if Role.one_person_blood > Role.two_person_blood:
            return 1
        elif Role.one_person_blood < Role.two_person_blood:
            return 2
        else:
            return False
player_one_jump = hinder.Obstacles(1)
player_two_jump = hinder.Obstacles(2)
def main(bool, timeoverbool = False):
    global mainbool

    mainbool = bool
    # 窗口标题改为梦之起源
    pygame.display.set_caption('梦之起源')
    # while循环
    gametime = timing.Time(screen)
    while timeoverbool:
        for event in pygame.event.get():
            # 如果窗口操作类型为QUIT
            if event.type == pygame.QUIT:
                # 执行关闭窗口操作
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainbool = False
                    starting_screen(False,1)
                    break
            starting_screen(False, 1)
    while mainbool:
        screen.fill((0, 0, 0))
        # pygame.time.delay(20)  # 限制帧率2

        for event in pygame.event.get():
            # 如果窗口操作类型为QUIT
            if event.type == pygame.QUIT:
                # 执行关闭窗口操作
                sys.exit()
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_i:
            #         Role.one_person_bring_orange = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainbool = False
                    starting_screen()
                    break
                if event.key == pygame.K_l and Role.one_person_dodge == False and Role.one_person_controlled == False:
                    if demo.Role.one_person_blue >= demo.Role.deduct_dodge_blue:
                        demo.Role.one_person_blue -= demo.Role.deduct_dodge_blue
                        Role.one_person_dodge = True

                if event.key == pygame.K_KP3 and Role.two_person_dodge == False and Role.two_person_controlled == False:
                    if demo.Role.two_person_blue >= demo.Role.deduct_dodge_blue:
                        demo.Role.two_person_blue -= demo.Role.deduct_dodge_blue
                        Role.two_person_dodge = True

                if event.key == pygame.K_k and Role.one_person_dodge == False:
                    Role.one_person_bring_orange = False
                    Role.one_person_defense = False
                    player_one_jump.jump()
                if event.key == pygame.K_KP2 and Role.two_person_dodge == False :
                    Role.two_person_bring_orange = False
                    Role.two_person_defense = False
                    player_two_jump.jump()
                if event.key == pygame.K_s and Role.one_person_stand and not Role.one_person_jump and Role.one_person_controlled == False:
                    Role.one_person_defense = True
                if event.key == pygame.K_DOWN and not Role.two_person_jump and Role.one_person_controlled == False:
                    Role.two_person_defense = True
                if event.key == pygame.K_j and Role.one_person_attack == False and Role.one_person_controlled == False:
                    Role.one_person_bring_orange = False
                    Sound("sound/挥剑音效.mp3")
                    Role.one_person_attack = True
                    Role.one_person_stand = True
                elif event.key == pygame.K_u:
                    if Role.one_person_blue >= Role.deduct_dart_blue:
                        Role.one_person_bring_orange = False
                        Role.one_person_dart = True
                        Role.one_person_stand = True
                        if Role.one_person_left:
                            dart = darts.Dart(screen, int(Role.one_person_x + Role.one_person_width // 2),int(Role.one_person_y + Role.one_person_height // 2), 1, -1)
                        else:
                            dart = darts.Dart(screen, int(Role.one_person_x + Role.one_person_width // 2),int(Role.one_person_y + Role.one_person_height // 2), 1, 1)
                        dart_img.append(dart)
                elif event.key == pygame.K_i:
                    if Role.one_person_blue >= Role.deduct_ultimate_skill_blue:
                        Role.one_person_bring_orange = False
                        Role.one_person_ultimate_skill = True
                        Role.one_person_stand = True
                        if Role.one_person_left:
                            ultimate_skill = ult.UltimateSkill(screen, 1920, Role.one_person_y, 1, -1)
                        else:
                            ultimate_skill = ult.UltimateSkill(screen, 0, Role.one_person_y, 1, 1)
                        ultimate_skill_img.append(ultimate_skill)
                elif event.key == pygame.K_n:
                    if Role.one_person_white >= Role.deduct_white:
                        Role.one_person_bring_orange = False
                        Role.one_person_stand = True
                        if Role.one_person_left:
                            aura = gas.Gas(screen, Role.one_person_x, Role.one_person_y, 1, -1)
                        else:
                            aura = gas.Gas(screen, Role.one_person_x, Role.one_person_y, 1, 1)
                        gas_img.append(aura)
                elif event.key == pygame.K_KP0:
                    if Role.two_person_white >= Role.deduct_white:
                        Role.two_person_bring_orange = False
                        Role.two_person_stand = True
                        if Role.two_person_left:
                            aura = gas.Gas(screen, Role.two_person_x, Role.two_person_y, 2, -1)
                        else:
                            aura = gas.Gas(screen, Role.two_person_x, Role.two_person_y, 2, 1)
                        gas_img.append(aura)
                if event.key == pygame.K_KP1 and Role.two_person_attack == False and Role.two_person_controlled == False:
                    Role.two_person_bring_orange = False
                    Sound("sound/挥剑音效.mp3")
                    Role.two_person_attack = True
                    Role.two_person_stand = True
                elif event.key == pygame.K_KP4:
                    if Role.two_person_blue >= Role.deduct_dart_blue:
                        Role.two_person_bring_orange = False
                        Role.two_person_dart = True
                        Role.two_person_stand = True
                        if Role.two_person_left:
                            dart = darts.Dart(screen, int(Role.two_person_x + Role.two_person_width // 2),int(Role.two_person_y + Role.two_person_height // 2), 2, -1)
                        else:
                            dart = darts.Dart(screen, int(Role.two_person_x + Role.two_person_width // 2), int(Role.two_person_y + Role.two_person_height // 2), 2, 1)
                        dart_img.append(dart)
                elif event.key == pygame.K_KP5:
                    if Role.two_person_blue >= Role.deduct_ultimate_skill_blue:
                        Role.two_person_bring_orange = False
                        Role.two_person_ultimate_skill = True
                        Role.two_person_stand = True
                        if Role.two_person_left:
                            ultimate_skill = ult.UltimateSkill(screen, 1920, Role.two_person_y, 2, -1)
                        else:
                            ultimate_skill = ult.UltimateSkill(screen, 0, Role.two_person_y, 2, 1)
                        ultimate_skill_img.append(ultimate_skill)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    Role.one_person_defense = False
                if event.key == pygame.K_DOWN:
                    Role.two_person_defense = False

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_j] and Role.one_person_attack == False and Role.one_person_controlled == False:
            event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_j)
            pygame.event.post(event)
        if pressed_keys[pygame.K_KP1] and Role.two_person_attack == False and Role.two_person_controlled == False:
            event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_KP1)
            pygame.event.post(event)

        # 如果按键为右箭头
        if not pressed_keys[pygame.K_j]:
            if pressed_keys[pygame.K_d] and Role.one_person_dodge == False and Role.one_person_attack == False and Role.one_person_controlled == False:
                Role.one_person_bring_orange = False
                Role.one_person_right = True
                Role.one_person_left = False
                Role.one_person_stand = False
                Role.one_person_x += Role.speed

                player_one_jump.out()
            elif pressed_keys[pygame.K_a] and Role.one_person_dodge == False and Role.one_person_attack == False and Role.one_person_controlled == False:
                Role.one_person_bring_orange = False
                Role.one_person_right = False
                Role.one_person_left = True
                Role.one_person_stand = False
                Role.one_person_x -= Role.speed

                player_one_jump.out()
            else:
                Role.one_person_stand = True
        else:
            pass
        if Role.one_person_jump:
            player_one_jump.judge()

        if not pressed_keys[pygame.K_KP1]:
            if pressed_keys[pygame.K_RIGHT] and Role.two_person_dodge == False and Role.two_person_attack == False and Role.two_person_controlled == False:
                Role.two_person_bring_orange = False
                Role.two_person_right = True
                Role.two_person_left = False
                Role.two_person_stand = False
                Role.two_person_x += Role.speed

                player_two_jump.out()
            elif pressed_keys[pygame.K_LEFT] and Role.two_person_dodge == False and Role.two_person_attack == False and Role.two_person_controlled == False:
                Role.two_person_bring_orange = False
                Role.two_person_right = False
                Role.two_person_left = True
                Role.two_person_stand = False
                Role.two_person_x -= Role.speed

                player_two_jump.out()
            else:
                Role.two_person_stand = True
        else:
            pass
        if Role.two_person_jump:
            player_two_jump.judge()

        if pressed_keys[pygame.K_o] and not Role.one_person_jump:
            Role.one_person_bring_orange = True
        if pressed_keys[pygame.K_KP6] and not Role.two_person_jump:
            Role.two_person_bring_orange = True

        
        # 游戏内部背景
        backgroundimg()
        # 血条，蓝条
        gametime.draw()
        draw()
        if Role.time_type == 1:
            if Role.time == 0:
                gametime.timeover()

        pygame.display.update()

        if gameover():
            mainbool = False
            starting_screen(False,gameover())
        
        fclock.tick(fps)
        
        
if __name__ == '__main__':
    # 运行菜单
    starting_screen(True)


