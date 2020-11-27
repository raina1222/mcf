#!/usr/bin/env python
# -*- coding: utf-8 -*
# hyeon code

#---------------------------------------------------------------------------------------------------------------
#                                   Auteur du présent code / Written by
#                                          Deregnaucourt Maxime
#                                            space.max@free.fr
#                                              Décember 2012
#                                                   
#
#                   In hommage at Nintendo who always made awesome games for little and big...
#                                   Don't forget the spirit of the game...
#-------------------------------------------------------------------------------------------------------------

import pygame,os,sys
from sys import exit
from random import  *
pygame.init() # 초기화
pygame.mixer.set_reserved(2)

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
ORANGE=(255,140,0)
WHITE=(255,255,255)
PINK=(255,0,255)
GREY=(128,128,128)
FPS=50

def environement():
	dir=os.getcwd()
	#print(dir,1)
	myscript=sys.argv[0] # sys.argv[0] < 실행파일의 경로
	#print(myscript)
	mydir=os.path.dirname(myscript)
	#print(mydir,2)
	try:
		os.chdir(mydir)
	except:
		os.chdir(dir)
		pass 
	exit
	
def events_handle():
    # ret=true면 게임 종료, false면 종료하지 않는다
    ret=False
    
    #for event in pygame.event.get():
    event=pygame.event.poll() # 대기열에서 하나의 단일 이벤트를 가져온다 
    if game.stop==False: # 게임이 실행중이라면
        ## change
        if event.type == pygame.MOUSEBUTTONDOWN: ## 마우스를 누르는 이벤트
                    mouse = pygame.mouse.get_pos() ## 마우스의 좌표를 가져온다
                    for obj in game.allBtns: ## 모든 버튼중에서
                        if obj.pressed(mouse): ## 클릭한 버튼을 찾는다
                            obj.action() ## 지정된 기능을 수행한다

        if event.type == pygame.KEYDOWN: # 키보드를 누르는 이벤트
            if event.key==pygame.K_ESCAPE: # esc
                ret=True # 종료를 알린다
                game.stop = True # 게임을 멈춘다
    
            # TEST BETA
            if event.key==pygame.K_SPACE: # 스페이스바
                '''
                for obj in game.allDrivers:
                    if obj.side>=0:
                            obj.state=1
                '''
                
                #-----------------------------------------------------------------------------
                # Put down the lever and open the tank
                # 레버를 내려 탱크를 연다
                #-----------------------------------------------------------------------------
                
                # Mario's arm is down
                # 마리오의 팔을 내린다
                mario.arm_down=True
                
                #---------------------------------------------------------------------------------
                # Mario is at stage 3 completely at left and opens the lever NO
                # 마리오가 3층 왼쪽 끝에 있으면 NO레버를 연다
                #---------------------------------------------------------------------------------
                if mario.rect.left==130 and mario.rect.top==200:
                    # Change the image of the Mario
                    # 마라오의 이미지를 바꾼다
                    mario.posx=0
                    for lever in game.allLevers:
                        # Open the NO lever
                        if lever.rect.left==95 and lever.rect.top==230: # NO레버
                            # Change the Image of the left lever at stage 3
                            # stage 3의 왼쪽 레버를 내려간 이미지로 바꾼다
                            lever.image=game.lever02 # 이미지 변경
                            lever.switch="down" # 레버를 내린다   

                    for trap in game.allTraps: # 트랩을 연다
                        if trap.side=="NO":
                            trap.switch="down"
                 
                #-----------------------------------------------------------------------------------           
                # Mario is at stage 3 completely at right and opens the lever NE
                #----------------------------------------------------------------------------------              
                elif mario.rect.left==440 and mario.rect.top==200: # 3층 맨 오른쪽
                    # Change the image of the Mario
                    mario.posx=7
                    for lever in game.allLevers:
                        if lever.rect.left==520 and lever.rect.top==230: # NE 레버
                            # Change the Image of the left lever at stage 3
                            lever.image=game.lever04 # 이미지 변경
                            lever.switch="down"

                    for trap in game.allTraps:
                        if trap.side=="NE":
                            trap.switch="down"

                #--------------------------------------------------------------------------------
                # Mario is at stage 2 completely at left and opens the lever SO
                #--------------------------------------------------------------------------------
                elif mario.rect.left==130 and mario.rect.top==275: # 2층 맨 왼쪽
                    # Change the image of the Mario
                    mario.posx=0 # 위치
                    for lever in game.allLevers:
                        if lever.rect.left==95 and lever.rect.top==300: # SO 레버
                            # Change the Image of the left lever at stage 2
                            lever.image=game.lever02
                            lever.switch="down"
                            
                    for trap in game.allTraps:
                        if trap.side=="SO":
                            trap.switch="down"     

                #---------------------------------------------------------------------------------           
                # Mario is at stage 2 completely at right and opens the lever SE
                #---------------------------------------------------------------------------------                           
                elif mario.rect.left==440 and mario.rect.top==275: # 2층 맨 오른쪽
                    # Change the image of the Mario
                    mario.posx=7
                    for lever in game.allLevers:
                        if lever.rect.left==520 and lever.rect.top==300: # SE 레버
                            # Change the Image of the left lever at stage 2
                            lever.image=game.lever04
                            lever.switch="down"
                    
                    for trap in game.allTraps:
                        if trap.side=="SE":
                            trap.switch="down"
                          
            if event.key == pygame.K_LEFT: # 왼쪽 화살표
                mario.update(0) # 왼쪽으로 이동
            elif  event.key == pygame.K_RIGHT: # 오른쪽 화살표
                mario.update(1) # 오른쪽으로 이동

    else: ## 게임이 멈춘경우
        ## 다시시작 버튼을 누르는 경우를 인식하기위한 코드
        if event.type == pygame.MOUSEBUTTONDOWN: ## 마우스를 누르는 이벤트
                        mouse = pygame.mouse.get_pos() ## 마우스의 좌표를 가져온다
                        for obj in game.allBtns: ## 모든 버튼중에서
                            if obj.pressed(mouse): ## 클릭한 버튼을 찾는다
                                obj.action() ## 지정된 기능을 수행한다

    #윈도우 창의 x버튼을 누르거나 esc를 누른경우 게임 종료
    if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
        ret=True

    return ret

def wait(time):
    # 전달받은 시간만큼 기다린다
    clock=pygame.time.Clock() #게임 루프를 작성하기 전에 게임 루프의 주기를 결정할 pygame.time.Clock 객체 생성
    laps_to_wait=0 # 시간 초기화
    while laps_to_wait<time: # time 만큼 시간이 흐르도록 한다
        clock.tick()
        laps_to_wait+=clock.get_time()
        #print(laps_to_wait)
    laps_to_wait=0

class Game():
    
    def __init__(self,size=(640,480)):
        pygame.mixer.set_num_channels(20) # 채널을 20개로 변경
        self.sound=1 ## 음소거 여부 (1:사운드 재생, 0:음소거)
        self.size=size
        self.surface=pygame.display.set_mode(self.size,0) # 화면에 나타낼 창
        self.surface.fill(BLACK)
        self.clock=pygame.time.Clock() # 현재시간
        self.laps=0
        self.speed=1500 # The speed of the game 기본 플레이 속도
        self.speed_save=self.speed # a variable uses to remember the game speed
        self.stop=False # 게임의 멈춤 여부를 알려준다
        self.launchRight=False
        
        # SECTION LOAD
        
        # Font
        # 폰트 설정
        self.font=pygame.font.Font("./font/Digirtu_.ttf",44)
        self.font.set_bold(True)
        self.point=0
        
        # Background
        # 배경 설정
        self.bg=pygame.image.load("./graph/bg.png").convert_alpha() # 투명도 있음
        self.rect=self.bg.get_rect()
        
        # All the Mario per level
        # 마리오의 이미지
        self.mario=[]
        mario=[
                    # 맨 아래         
                    "./graph/mario00.png", #0 0
                    # 1층
                    "./graph/mario10.png", #1 1
                    "./graph/mario11.png", #1 2
                    "./graph/mario12.png", #1 3
                    # 2층
                    "./graph/mario20.png", #2 4
                    "./graph/mario21.png", #2 5
                    "./graph/mario22.png", #2 6
                    "./graph/mario23.png", #2 7
                    "./graph/mario24.png", #2 8
                    "./graph/mario25.png", #2 9
                    "./graph/mario26.png", #2 10
                    "./graph/mario27.png", #2 11
                    # 3층
                    "./graph/mario30.png", #3 12
                    "./graph/mario31.png", #3 13
                    "./graph/mario32.png", #3 14
                    "./graph/mario33.png", #3 15
                    "./graph/mario34.png", #3 16
                    "./graph/mario35.png", #3 17
                    "./graph/mario36.png", #3 18
                    "./graph/mario37.png", #3 19
                    # 4층
                    "./graph/mario40.png", #4 20
                    "./graph/mario41.png", #4 21
                     # 꼭대기
                    "./graph/mario00.png", #0 22
                   ]
        #-----------------------------------------------
        # Load all the image of the Mario
        # 마리오의 이미지를 모두 가져온다
        #-----------------------------------------------      
        for e in range(23):
            self.mario.append(pygame.image.load(mario[e]).convert_alpha())
        
        self.Mario=pygame.sprite.RenderUpdates()
        
        #-----------------------------------------------
        # Driver
        #-----------------------------------------------      
        self.driver=6*[0]
        
        # Left Driver
        self.driver[0]=pygame.image.load("./graph/driver10.png")
        self.driver[1]=pygame.image.load("./graph/driver11.png") # 시멘트 맞은 이미지
        self.driver[2]=pygame.image.load("./graph/driver12.png") # 떨어지는 이미지
        
        # Right driver: 읜쪽 운전자의 좌우반전 이미지
        self.driver[3]=pygame.transform.flip(self.driver[0],True,False)
        self.driver[4]=pygame.transform.flip(self.driver[1],True,False)
        self.driver[5]=pygame.transform.flip(self.driver[2],True,False)
        
        #-----------------------------------------------
        # Load Missed Mario
        # miss 마리오 이미지
        #-----------------------------------------------
        self.miss=4*[0]
        self.miss[0]=pygame.image.load("./graph/miss0.png")
        self.miss[1]=pygame.image.load("./graph/miss1.png")
        self.miss[2]=pygame.image.load("./graph/miss2.png")
        
        #-----------------------------------------------
        # Load bac
        #-----------------------------------------------
        ## change
        self.bac0=pygame.image.load("./graph/bac0.png") # empty bac
        self.bac1=pygame.image.load("./graph/bac1.png") # 열린 empty bac
        self.bac2=pygame.image.load("./graph/bac2.png") # ^ 좌우반전
        self.bac3=pygame.image.load("./graph/bac3.png") # full bac
        self.bac4=pygame.image.load("./graph/bac4.png") # 열린 full bac
        self.bac5=pygame.image.load("./graph/bac5.png") # ^ 좌우 반전
        # 보너스 시멘트가 들어있는 bac이미지
        self.bac6=pygame.image.load("./graph/bac6.png") # full bac
        self.bac7=pygame.image.load("./graph/bac7.png") # 열린 full bac
        self.bac8=pygame.image.load("./graph/bac8.png") # ^ 좌우 반전
        
        self.allBacs=pygame.sprite.RenderUpdates()
        
        #-----------------------------------------------
        # Load ciment
        #-----------------------------------------------
        ## change
        self.ciment0=pygame.image.load("./graph/ciment00.png") # 탱크로 떨어지는 시멘트
        self.ciment1=pygame.image.load("./graph/ciment01.png") # 탱크로 떨어지는 보너스 시멘트
        self.ciment2=pygame.image.load("./graph/ciment02.png") # 탱크안의 시멘트
        self.ciment3=pygame.image.load("./graph/ciment03.png") # 탱크안의 보너스 시멘트
        self.ciment4=pygame.image.load("./graph/ciment04.png") # 트럭에 떨어지는 시멘트
        self.ciment5=pygame.image.load("./graph/ciment05.png") # 트럭에 떨어지는 보너스 시멘트

        
        #-----------------------------------------------
        # Load  Levers
        #-----------------------------------------------
        
        # Left Levers 
        self.lever01=pygame.image.load("./graph/lever01.png") # 올라가있는 기본 레버
        self.lever02=pygame.image.load("./graph/lever02.png") # 내려간 레버
        # Right Levers
        self.lever03=pygame.transform.flip(self.lever01,True,False)
        self.lever04=pygame.transform.flip(self.lever02,True,False)

        #-----------------------------------------------
        # Load Heart
        #-----------------------------------------------
        ## change
        self.heart00=pygame.image.load("./graph/heart.png")
        self.heart01=pygame.transform.scale(self.heart00, (30,25))
        
        self.allHearts=pygame.sprite.RenderUpdates()

        #-----------------------------------------------
        # Load Button
        #-----------------------------------------------
        ## change
        self.btn=4*[0]
        self.b00=pygame.image.load("./graph/info.png") #3 게임설명 아이콘
        self.b01=pygame.image.load("./graph/on.png") ## 소리 on
        self.b02=pygame.image.load("./graph/mute.png") ## 음소거 아이콘
        self.b03=pygame.image.load("./graph/retry.png") ## 다시시작 아이콘

        ## resize해서 배열에 저장
        self.btn[0]=pygame.transform.scale(self.b00, (35,35))
        self.btn[1]=pygame.transform.scale(self.b01, (45,45))
        self.btn[2]=pygame.transform.scale(self.b02, (37,37))
        self.btn[3]=pygame.transform.scale(self.b03, (120,120))
        
        self.allBtns=pygame.sprite.RenderUpdates()

        #-----------------------------------------------
        # Load Informaion
        #-----------------------------------------------
        self.info=pygame.image.load("./graph/information.png")

        #-----------------------------------------------
        # Load the sounds
        #-----------------------------------------------
        self.mario_bip=pygame.mixer.Sound("./sound/mario_move.ogg")
        self.mario_fall=pygame.mixer.Sound("./sound/mario_fall.ogg")
        self.elevator_move=pygame.mixer.Sound("./sound/elevator_move.ogg")
        self.tank_full=pygame.mixer.Sound("./sound/tank_full.ogg")
        self.tank_fill=pygame.mixer.Sound("./sound/tank_fill.ogg")
        self.cement_fall=pygame.mixer.Sound("./sound/cement_fall.ogg")
        
        #-----------------------------------------------
        # Group for the Elevators
        #-----------------------------------------------
        self.allElevators=pygame.sprite.RenderUpdates()
        
        #-----------------------------------------------
        # Group for the Tanks
        #-----------------------------------------------
        self.allTanks=pygame.sprite.RenderUpdates()
        
        #-----------------------------------------------
        # Group for the Bars
        #-----------------------------------------------
        self.allBars=pygame.sprite.RenderUpdates()
        
        #-----------------------------------------------
        # Group for the Levers
        #-----------------------------------------------
        self.allLevers=pygame.sprite.RenderUpdates()
        
        #-----------------------------------------------
        # Group for the Traps
        #-----------------------------------------------
        self.allTraps=pygame.sprite.RenderUpdates()
        
        #-----------------------------------------------
        # Group for the Missed
        #----------------------------------------------
        self.allMiss=pygame.sprite.RenderUpdates()
        
        #-----------------------------------------------
        # Group for the Drivers
        #----------------------------------------------
        self.allDrivers=pygame.sprite.RenderUpdates()
        
        #-----------------------------------------------
        # Group for the Texts
        #----------------------------------------------
        self.allTexts=pygame.sprite.RenderUpdates()
        
        #-----------------------------------------------
        # Group for the Cements
        #----------------------------------------------
        self.allCements=pygame.sprite.RenderUpdates()
        

    def play_sound(self,sound,loop=0):
    # 음악을 전달받아 실행한다
        chanel=0
        canal=pygame.mixer.find_channel() # 사용중인 채널을 돌려준다
        while canal is None:
            chanel+=1
            canal=pygame.mixer.find_channel(chanel)
        
        if game.sound: ## 음소거를 설정하지 않았으면
            canal.play(sound,loop) ## 사운드 재생
            
    def reset(self): # 마리오의 모든 이미지를 그린다
        mario.beta(0)
        mario.beta(1)
        mario.beta(2)
        mario.beta(3)
        mario.beta(4)
        mario.beta(5)
        '''
        for driver in game.allDrivers:
            driver.state=1
            game.allDrivers.draw(game.surface)
            game.allDrivers.update()
            driver.state=2
            game.allDrivers.draw(game.surface)
            game.allDrivers.update()
        '''

## change
class Button(pygame.sprite.Sprite):
    def __init__(self,index,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=game.btn[index] ## 이미지 지정
        self.rect=self.image.get_rect()
        self.index=index ## 이미지 지정을 위한 인덱스
        self.x=x ## x좌표
        self.y=y ## y좌표
        self.rect.left=x ## x좌표 위치 설정
        self.rect.top=y ##y좌표 위치 설정
        self.w=self.image.get_width() ## 이미지 넓이
        self.h=self.image.get_height() ## 이미지 높이=

    def pressed(self,mouse): ## 버튼을 클릭했는지 알아보는 함수
        if self.x+self.w > mouse[0] > self.x and self.y+self.h > mouse[1] > self.y:
            return True

    def action(self):
        
        if self.index==0: ## info 버튼
            game.surface.blit(game.info,(140, 100)) ## 게임 설명을 띄운다
            pygame.display.update() ## 화면에 출력
            wait(3000) ## 4초 동안 띄운다
            game.surface.blit(game.bg,game.bg.get_rect()) ## 원래의 배경으로 되돌린다

        elif self.index==1: ## on 버튼
            self.index=2
            self.image=game.btn[self.index] ## 음소거 이미지로 변경
            self.rect.left=53 ## 위치 재설정
            self.rect.top=60
            self.w=self.image.get_width() ## 이미지 넓이
            self.h=self.image.get_height() ## 이미지 높이
            game.sound=0 ## 음소거 설정
        
        elif self.index==2: ## mute 버튼
            self.index=1
            self.image=game.btn[self.index] ## 사운드 재생 이미지로 변경
            self.rect.left=50 ## 위치 재설정
            self.rect.top=55
            self.w=self.image.get_width() ## 이미지 넓이
            self.h=self.image.get_height() ## 이미지 높이
            game.sound=1 ## 음소거 해제

        elif self.index==3: ## 다시시작 버튼
            print("hi")

class Mario(pygame.sprite.Sprite):
    
    def __init__(self,life=3):
        
        pygame.sprite.Sprite.__init__(self)
        
        #-------------------------------------------------------------------------
        # Table of all the Mario in each stage
        # A Mario is a tuple like (a,b,c) where 
        # a is the  index of the image to blit
        # b,c are x,y coordinates
        #-------------------------------------------------------------------------
        
        self.stage=6*[[]] # 크기 6의 이중리스트 
        
        self.stage[0]=[(0,260,420)] # 맨 아래
        self.stage[1]=[(1,185,354),(2,250,354),(3,335,354)] # 1층
        self.stage[2]=[(4,130,275),(5,130,275),(6,200, 275),(7,265,275),(8,335,275),(9,380,275),(10,440,275),(11,440,275)] # 2층
        self.stage[3]=[(12,130,200),(13,130,200),(14,200,200),(15,265,200),(16,335,200),(17,380,200),(18,440,200),(19,440,200)] # 3층
        self.stage[4]=[(20,260,130),(21,335,130)] # 4층
        self.stage[5]=[(22,260,80)] # 꼭대기
        
        self.life=life
        self.image=game.mario[13] # 시작 이미지
        self.rect=self.image.get_rect()
        self.posx=1 # 시작 위치
        self.posy=3 # 시작 층
        
        #------------------------------------------------------------------------------
        # Place the Mario with coordinates  stored.in stage table
        #------------------------------------------------------------------------------
        
        self.rect=self.rect.move(self.stage[self.posy][self.posx][1],self.stage[self.posy][self.posx][2]) # 위치 설정
        self.fall_left=None # none == null(값이 없음)
        self.fall_right=None
        self.ko=False # 마리오가 죽었으면 true
        self.clock=pygame.time.Clock()
        self.laps=0 # 마리오를 깜빡이는데 사용
        self.laps2=0 # 마리오의 팔을 움직이는데 사용
        self.blink_state=0 # 마리오가 깜빡인 수
        self.arm_down=False # 레버를 내리기 위해 팔을 내리면 true
        game.speed=game.speed_save # 1500으로 초기화

    def update(self,way=-1):
        '''
        Update Mario 
        Go left and right, up and down 
        Test whether Mario is falling
        '''
        
        self.clock.tick() #clock.tick(TARGET_FPS) FPS를 맞추기 위한 딜레이를 추가
        
        #----------------------------------------------------------------------------
        # Fix the limits start and end in terms of the current stage
        # stage 배열로부터 마리오를 움직일 수 있는 범위를 정한다
        # 이동할 때 posx의 인덱스값을 나타나는데에 사용
        #----------------------------------------------------------------------------
        
        if self.posy==2 or self.posy==3: # 2,3층의 경우 1~6 > 6개
            start=1
            end=len(self.stage[self.posy])-2
        elif self.posy==4: # 4층의 경우 0~1 > 2개
            start=0
            end=len(self.stage[self.posy])-1
        elif self.posy==1: # 1층의 경우 0~2 > 3개
            start=0
            end=len(self.stage[self.posy])-1
        else: # 맨 아래, 꼭대기 > 1개
            start=end=0
        
        #----------------------------------
        # Test if Mario is KO 
        # 마리오가 죽었는지 확인
        #----------------------------------
        # 마리오가 떨어졌거나 맨 아래, 꼭대기에 있는 경우 true
        if self.fall_left==True or self.fall_right==True or self.posy==0 or self.posy==5:
            self.ko=True
        else:
            self.ko=False
        
        #-----------------------------------
        # Test if Mario's arm is down
        # 마리오의 팔이 내려갔는지 확인
        #----------------------------------
        # 100ms동안 팔이 내려간 상태를 유지하고 100ms가 지나면 원래 상태로 돌린다
        if self.arm_down==True and self.laps2<100:
            self.laps2+=self.clock.get_time()
        else:
            self.laps2=0 # 시간 초기화
            self.arm_down=False # 팔을 올린다
            if self.rect.left==130: # 왼쪽
                self.posx=1
            elif self.rect.left==440: # 오른쪽
                self.posx=6
            
        #----------------
        # Go left
        # ---------------        
        if way==0 and self.ko==False:
            if self.posx>start: # 움직일 수 있는 범위 안에 있으면
                self.posx-=1 # 왼쪽으로 이동
                game.play_sound(game.mario_bip) # 마리오가 움직이는 효과음
        #-----------------       
        # Go right
        #-----------------      
        elif way==1 and self.ko==False:
            if self.posx<end: # 움직일 수 있는 범위 안에 있으면
             self.posx+=1 # 오른쪽으로 이동
             game.play_sound(game.mario_bip) # 마리오가 움직이는 효과음
         
        #-----------------------------------------
        # Tests whether Mario falls
        #-----------------------------------------
        #-----------------------------------------
        # Test for the left elevators  
        #-----------------------------------------
        # 마리오의 x좌표가 250이상, 330 미만이면 fall left
        if self.stage[self.posy][self.posx][1]>=250 and self.stage[self.posy][self.posx][1]<330 and self.ko==False:
            
            self.fall_left=True

            for e in game.allElevators:
                #------------------------------------------------------------------------------------------------------
                # For all elevator in the left column, we test if at least one have the same
                # stage than mario's stage
                #------------------------------------------------------------------------------------------------------
                # 마리오가 왼쪽 엘레베이터에 올라가있는지 확인
                if (e.stage[e.count]==self.posy  and e.side=="left"):
                    self.fall_left=False # 떨어지지 않도록 상태를 바꾼다
                    self.fall_right=None
                    break
           
        #----------------------------------------
        # Test for the right elevators  
        #----------------------------------------
        # 마리오의x좌표가 335이상, 380미만이면 fall right
        elif self.stage[self.posy][self.posx][1]>=335 and  self.stage[self.posy][self.posx][1]<380 and self.ko==False:
            
            self.fall_right=True
            
            for e in game.allElevators:
                #------------------------------------------------------------------------------------------------------
                # For all elevator in the rightcolumn, we test if at least one have the same
                # stage than mario's stage
                #------------------------------------------------------------------------------------------------------
                # 마리오가 오른쪽 엘레베이터에 올라가있는지 확인
                if (e.stage[e.count]==self.posy  and e.side=="right"):
                    self.fall_right=False
                    self.fall_left=None
                    break
        
        elif (self.posx<=250 or self.posx>=380) and self.ko==False: # 그 외의 범위는 떨어지지 않는다
            self.fall_left=None 
            self.fall_right=None
        
        if self.fall_left==True: # 왼쪽에서 떨어진다
                self.fall("left")
        
        if self.fall_right==True: # 오른쪽에서 떨어진다
                self.fall("right")

        if  self.ko==False:
            self.image=game.mario[self.stage[self.posy][self.posx][0]] # 이미지 설정
            self.rect=self.image.get_rect()
            self.rect=self.rect.move(self.stage[self.posy][self.posx][1],self.stage[self.posy][self.posx][2]) # 위치 설정
            
    def fall(self,side):
       '''
       The Fall of Mario...
       ''' 
       self.laps+=self.clock.get_time() # 경과 시간
       if side=="right": # 오른쪽이면 1
           x=1
       else: # 왼쪽이면 0
            x=0
            
       #-----------------------------------------------------------------
       # Every 1.5 second at the beginning of the game
       #-----------------------------------------------------------------
        
       game.speed=500
       #--------------------------------------------------------
       # Mario's stage is greater than 1
       # Decrease the stage and reset the timer
       # 마리오가 1층보다 높이 있을 때 아래로 떨어진다
       #--------------------------------------------------------
       if self.posy>=1 and self.posy<5: # 1~4층
           if self.laps>game.speed:
               self.posy-=1 # 1층 아래로
               self.laps=0 # 시간 초기화
               # Retrieve the index of the image in regard of the stage
               # 스테이지와 관련된 이미지의 인덱스 검색
               if self.posy==4: # 4층
                   self.posx=0 # 왼쪽에서만 떨어진다
               elif self.posy==2 or self.posy==3: # 2,3층
                    self.posx=3+x # 왼쪽은 3, 오른쪽은 4
               elif self.posy==1: # 1층
                    self.posx=1+x # 읜쪽은 1, 오른쪽은 2
               elif self.posy==0: # 맨 아래
                    self.posx=0

               self.image=game.mario[self.stage[self.posy][self.posx][0]] # 이미지 변경
               self.rect=self.image.get_rect()
               self.rect=self.rect.move(self.stage[self.posy][self.posx][1],self.stage[self.posy][self.posx][2]) # 위치 변경
       #----------------------------------
       # Mario is blinking
       # 마리오가 깜빡인다
       #----------------------------------
       else: # self.posy = 0 or 5 < 꼭대기 혹은 맨 아래에 있는 경우
           if self.blink_state==0: # 처음이면
            game.play_sound(game.mario_fall) # 마리오가 떨어지는 효과음
            self.blink_state+=1
            self.blink()
           elif self.blink_state<6: # 5번 깜빡인다
               self.blink()
           else:
               self.dead()
               self.__init__(self.life)
               
    def blink(self):

        if self.posy==0: # 맨 아래
            self.image=game.mario[self.stage[0][0][0]] # 이미지 변경
            t=(260,420) # 위치 설정
        else: # 꼭대기
            self.image=game.mario[self.stage[5][0][0]] # 이미지 변경
            t=(260,80) # 위치 설정
        
        # Erase Mario by moving it !
        # 마리오를 움직여 사라지게 한다
        if self.laps<500:
            self.rect=self.image.get_rect()
            self.rect=self.rect.move(t) # 위치 이동
        elif self.laps<1000: # 1초보다 적으면
             self.rect.left=-1000 # 사라진다
        else:
            self.laps=0 # 초기화
            self.blink_state+=1 # 깜빡인 수를 1 더한다
   
    def dead(self):
        
        if self.life==3: # 처음 죽으면 miss메세지 생성
            info=Information("Miss",575,105) # 화면에 출력
            game.allTexts.add(info)
            
        self.life-=1 # 생명이 줄어든다
        miss=Miss(self.life) # miss 아이콘 생성
        game.allMiss.add(miss)

    ## change
    def deleteMiss(self):
        if self.life<3: ## miss가 발생하지 않았으면 아이템을 먹어도 효과가 없다
            for obj in game.allMiss:
                if obj.index==self.life: ## 마지막에 발생한 miss
                    obj.kill() ## 삭제

            self.life+=1 ## 생명이 늘어난다
            
    def beta(self,level):
        for e in self.stage[level]:
            self.image=game.mario[e[0]] # 각 위치에 대한 마리오 이미지 설정
            self.rect=self.image.get_rect()
            self.rect=self.rect.move(e[1],e[2]) # 이미지의 위치 설정
            game.surface.blit(self.image,self.rect) # 그린다

class Miss(pygame.sprite.Sprite): # miss아이콘
    '''
    The missed Mario
    '''
    def __init__(self,index):
        pygame.sprite.Sprite.__init__(self)
        self.index=index
        self.image=game.miss[index] # miss 이미지 배열(line242) 
        self.rect=self.image.get_rect()
        if index==2: # 각 이미지에 대한 위치 설정
            self.rect=self.rect.move(595,70) # 1 miss
        elif index==1:
            self.rect=self.rect.move(555,70) # 2 miss
        else:
            self.rect=self.rect.move(515,70) # 3 miss

class Information(pygame.sprite.Sprite):
    # 문자열, 위치, 폰트 종류를 전달 받아 화면에 출력해준다
    def __init__(self,text1="",x=0,y=0,fontIndex=0,color=BLACK):
        pygame.sprite.Sprite.__init__(self)
        if fontIndex == 0: # 인덱스에 따라 폰트와 글자 크기를 설정한다
            self.font=pygame.font.Font("./font/DejaVuSansCondensed-Bold.ttf",24)
        elif fontIndex == 1:
            self.font=pygame.font.Font("./font/Digirtu_.ttf",18)
        elif fontIndex == 2:
            self.font=pygame.font.Font("./font/DejaVuSansCondensed-Bold.ttf",16)
        elif fontIndex == 3:
            self.font=pygame.font.Font("./font/DejaVuSansCondensed-Bold.ttf",45)   
        self.font.set_bold(True) # bold
        self.image=self.font.render(text1,1,color) # 화면에 출력
        self.rect=self.image.get_rect()
        self.rect=self.rect.move(x,y) # 위치 설정
            
class Bac(pygame.sprite.Sprite):
    '''
    Bac of ciment
    시멘트를 싣고 나와 탱크에 시멘트를 넣어주는 바구니
    '''
    def __init__(self,side="left"):
        pygame.sprite.Sprite.__init__(self)
        
        # full or empty ICI FAIRE UN TIRAGE EN FONCTION DU SCORE
        # sur = ~을 거쳐 ~에, 위에
        # 0-100 : 1 CHANCE SUR 3
        # 100-200 : 1 CHANCE SUR 2
        # 200-275 : 2 CHANCE SUR 3
        # 275-300 : 3 SUR 3
        
        #self.full=1
        self.full=randint(0,1) # 0또는 1 랜덤으로 발생(0: empty/ 1: full)       
        self.side=side # 오른쪽 왼쪽

        ## change
        if self.full==0: # 비어있는 경우
            self.image=game.bac0 # bac empty 이미지
         # 시멘트가 차있는 경우
        else: # 1/4 확율로 보너스 시멘트 생성
            if randint(0,3) == 1:
                self.bonus = 1 # 보너스 시멘트
                self.image=game.bac6 # 보너스 시멘트가 차있는 이미지
            else:
                self.bonus = 0 # 일반 시멘트
                self.image=game.bac3 # bac full 이미지

        self.rect=self.image.get_rect()
        
        # Determine the limits of the bacs for left and right       
        if self.side=="left": # 왼쪽
            self.rect=self.rect.move((165,135)) # 시작위치
            self.way=-60 # 한번에 60만큼 이동
            self.limit=-15 #한계
        else: # 오른쪽
             self.rect=self.rect.move((430,135)) # 시작위치
             self.way=60 # 한번에 60만큼 이동
             self.limit=610 # 한계
        self.clock=pygame.time.Clock() # 시간설정에 대한 선언
        self.laps=0 # 시간 초기화
        game.allBacs.add(self)
        
    def update(self):
        self.clock.tick()
        self.laps+=self.clock.get_time() # 경과 시간(시간의 흐름에 따라 laps 증가)
        
        if self.laps>game.speed: # game speed만큼 시간이 지나면
            if self.side=="left": # 왼쪽
                #--------------------------------------------------------------------------------------------------
                # Move for left Bac
                # 165에서 시작해서 60씩 3번 이동(165 -> 105 -> 45 -> -15)
                #--------------------------------------------------------------------------------------------------
                if self.rect.left>self.limit and self.rect.left!=45: # bac이 165 혹은 105에 있을 때
                    self.rect.left+=self.way # 60 이동
                    self.laps=0 # 시간 초기화
                elif self.rect.left==45: # bac이 45에 있으면 
                    #--------------------------------------
                    # bac 0: empty bac closed 닫혀있는 빈 bac
                    # bac 1: empty bac opened 열린 빈 bac
                    # bac 3: full bac closed 닫힌 채워진 bac
                    # bac 4: full bac opened 열린 채워진 bac
                    #--------------------------------------
                    if self.laps<game.speed*2: # game speed*2 동안
                        if self.full==0: # bac이 비어있으면
                            # Open the empty bac
                            self.image=game.bac1 # 열려있는 이미지로 변경
                        else: # bac이 차있으면
                            #-----------------------------------------------------------
                            # Open the full bac, so changing in empty bac
                            # 채워져있는 bac을 열어 빈 bac으로 변경
                            #-----------------------------------------------------------
                            self.image=game.bac1 # 열려있는 빈 bac 이미지로 변경
                            self.full=0 # 비어있다
                            if tank1.update_tank==False:
                                #--------------------------------
                                # Update Tank value
                                #--------------------------------
                                tank1.t[0]=1 # 탱크 맨 위에 시멘트를 내려보낸다
                                bar=Bar(175, self.bonus) # 왼쪽, 175에 위치한 시멘트 막대기 생성
                                tank1.update_tank=True
                                tank1.laps=0
                    else: # game speed*2 보다 시간이 지난 경우 bac이 열려야하는 위치(45)에 도착해도 열리지 않는다
                        if self.full==0: # 비어있으면
                            # Close the empty bac
                            self.image=game.bac0 # 비어있는 bac이미지
                        else: # 채워져있으면 
                            #close the full bac
                            self.image=game.bac3 # 채워져있는 이미지
                        self.rect.left+=self.way # 좌표 계산
                        self.laps=0 # 시간 초기화
                else: # limit에 위치하면 현재의 bac이 사라지고 새로운 bac을 생성한다
                    self.laps=0 # 시간 초기화
                    self.kill() # 기존의 bac을 없앤다
                    # Bac is at the limit : make a new one
                    bac=self.__init__(self.side) # 시작 위치에 새로운 bac을 생성한다
            else: # 오른쪽
            #--------------------------------------------------------------------------------------------------   
            # Move for right Bac
            # 430에서 시작해서 오른쪽으로 60만큼 3번 움직인다(430 -> 490 -> 550 -> 610) 
            #--------------------------------------------------------------------------------------------------
                if self.rect.left<self.limit and self.rect.left!=550: # bac이 490혹은 490에 있을 때
                    self.rect.left+=self.way # 오른쪽으로 60 이동
                    self.laps=0 # 시간 초기화
                elif self.rect.left==550: # bac이 550에 있으면
                        #--------------------------------------
                        # bac 0 : empty bac closed
                        # bac 2 : empty bac opened
                        # bac 3 : full bac closed
                        # bac 5 : full bac opened
                        #----------------------------------------
                        if self.laps<game.speed*2: # game speed*2 동안
                            if self.full==0: # 비어있으면
                                # Open the empty bac
                                self.image=game.bac2 # 열려있는 빈 bac 이미지
                            else: # 채워져있으면
                                #-----------------------------------------------------------
                                # Open the full bac, so changing in empty bac
                                # 채워져있는 bac을 열어 빈 bac으로 변경
                                #-----------------------------------------------------------
                                self.image=game.bac1 # 열려있는 빈 bac 이미지로 변경
                                self.full=0 # 비어있다
                                if tank2.update_tank==False:
                                    #--------------------------------
                                    # Update Tank value
                                    #--------------------------------
                                    tank2.t[0]=1 # 맨 아래 시멘트를 없앤다
                                    bar=Bar(175,self.bonus,"right") # 오른쪽 175위치에 시멘트 막대기 생성
                                    tank2.update_tank=True
                                    tank2.laps=0 # 시간 초기화
                        else: # game speed*2 보다 시간이 지난 경우 bac이 열려야하는 위치(550)에 도착해도 열리지 않는다
                            if self.full==0: # 비어있으면
                                # Close the empty bac
                                self.image=game.bac0 # 비어있는 bac이미지
                            else: # 채워져있으면
                                # Close the full bac
                                self.image=game.bac3 # 채워져있는 bac 이미지
                            self.rect.left+=self.way
                            self.laps=0 
                else: # limit에 위치하면 현재의 bac이 사라지고 새로운 bac을 생성한다
                    self.laps=0
                    self.kill() # 기존의 bac을 없앤다
                    bac=self.__init__(self.side) # 시작위치에 새로운 bac을 생성한다
            
        pass # python에서 pass는 if-else문에서 특정 기능을 기획하지 않음을 나타냄 

class Tank(pygame.sprite.Sprite):
# 4개의 tank에 cement가 내려와서 이동하는 과정을 보여주고
# cement가 꽉 채워져 있을 경우에 게임의 진행과 각 tank가 어떻게 바뀌는지 나타내는 class
# NO: 왼쪽 위, SO: 왼쪽 아래, NE: 오른쪽 위, SE: 오른쪽 아래

    def __init__(self,pos="NO"):
        pygame.sprite.Sprite.__init__(self) 
        
        self.image=pygame.Surface((1,1))
        self.rect=self.image.get_rect() # 이미지를 호출해서 가져온다
        self.clock=pygame.time.Clock()
        self.laps=0
        self.pos=pos # 위치
        self.open=False # 열림여부
        
        # Flag to determine if a tank is overflow   
        # 탱크 오버플로 여부를 확인하기 위한 플래그     
        #self.state=-1 ici
        
        self.t=[0]*4 # [0]*4 = [0,0,0,0]
        self.update_tank=None 
        if pos=="NO" or pos=="SO": # 왼쪽
            self.side="left"
        elif pos=="NE" or pos=="SE": # 오른쪽
            self.side="right"
    
    def update(self):
        
        self.clock.tick()
        self.laps+=self.clock.get_time()
        if self.laps>game.speed:
            #----------------------------------------------
            # Move the Bar at the downside   
            # First : create a new bar
            # Snd : delete the previous
            #----------------------------------------------
            '''
            The tank index : the third position is the bottom of the tank
            the bar in position 0 is created in the class Bac in the update method
            탱크 인덱스 : 세 번째 위치는 탱크 하단의 위치
		    위치 0의 막대는 Bac 클래스의 업데이트 함수에서 생성된다
            
            0 |    | 175 / 265
            1 |    | 200 / 285
            2 |    | 215 / 300
            3 |    | 230 / 315
               -----
            '''
           
            if self.t!=[1,1,1,1]: # the tank is full when [1,1,1,1]
                for i in range(3,0,-1): # 3부터 1까지 1씩 감소
                    #------------------------------------------
                    # Move the bars at the down side
                    # 막대를 아래로 이동
                    #------------------------------------------
                    if self.t[i]==0 and self.t[i-1]==1: # 아래가 비어있고 위에 시멘트가 있으면 아래로 이동한다
                        self.t[i]=1 # 아래로 이동
                        self.t[i-1]=0 # 왼래 있던 시멘트 삭제
                        if self.pos=="NO" or self.pos=="NE": # 위층 탱크
                            # the first step in the falling
                            if i==1: # 처음
                                # Delete the previous bar in the pos 0
                                # [0]위치의 바를 삭제
                               for obj in game.allBars:
                                    if obj.rect.top==175 and obj.side==self.side: # [0]위치
                                        self.bonus=obj.bonus ## 보너스 여부를 기록
                                        obj.kill() # 삭제
                               # Create the new bar in the pos 1 
                               bar=Bar(200,self.bonus,self.side) # [1]의 위치에 시멘트 바를 생성한다 

                            # the second step in the falling
                            elif i==2: # 두 번째
                                # Delete the previous bar in the pos 1
                                # [1]위치의 바를 삭제
                                for obj in game.allBars:
                                    if obj.rect.top==200 and obj.side==self.side:
                                        self.bonus=obj.bonus # 보너스 여부를 기록
                                        obj.kill()
                                # Create the new bar in the pos 2
                                bar=Bar(215,self.bonus,self.side) # [2]의 위치에 시멘트 바를 생성한다
                               
                            # the third step in the falling
                            elif i==3: # 세 번째
                                # Delete the previous bar in the pos 2
                                # [2]위치의 바를 삭제
                                for obj in game.allBars:
                                    if obj.rect.top==215 and obj.side==self.side:
                                        self.bonus=obj.bonus # 보너스 여부를 기록
                                        obj.kill()
                                # Create the new bar in the pos 3. This is the last pos of the tank
                                bar=Bar(230,self.bonus,self.side) # [3]의 위치에 시멘트 바를 생성한다
                                
                        #------------------------------------------
                        # Tank at the botton
                        #------------------------------------------
                        else: # 아래층 탱크
                            # the first step in the falling
                            if i==1:
                                # Delete the previous bar in the pos 0
                                # [0]위치의 바를 삭제
                                for obj in game.allBars:
                                    if obj.rect.top==265 and obj.side==self.side:
                                        self.bonus=obj.bonus # 보너스 여부를 기록
                                        obj.kill()
                                # Create the new bar in the pos 1 
                                bar=Bar(285,self.bonus,self.side) # [1]의 위치에 시멘트 바를 생성한다
                               
                            # the second step in the falling
                            elif i==2:
                                # Delete the previous bar in the pos 1
                                # [1]위치의 바를 삭제
                                for obj in game.allBars:
                                    if obj.rect.top==285 and obj.side==self.side:
                                        self.bonus=obj.bonus # 보너스 여부를 기록
                                        obj.kill()
                                # Create the new bar in the pos 2
                                bar=Bar(300,self.bonus,self.side) # [2]의 위치에 시멘트 바를 생성한다
                               
                            # the third step in the falling
                            elif i==3:
                                # Delete the previous bar in the pos 2
                                # [2]위치의 바를 삭제
                                for obj in game.allBars:
                                    if obj.rect.top==300 and obj.side==self.side:
                                        self.bonus=obj.bonus # 보너스 여부를 기록
                                        obj.kill()
                                # Create the new bar in the pos 3. This is the last pos of the tank
                                bar=Bar(315,self.bonus,self.side) # [3]의 위치에 시멘트 바를 생성한다
                               
                            #break # ici
                    elif self.t==[0,1,1,1]:
                        # Delete the  bar in the pos 0
                        # for obj in game.allBars:
                        #     if obj.rect.top==265 and obj.side==self.side:
                        #         obj.kill()
                        # 위층 탱크가 꽉 찬 경우 경고를 울린다
                        if  (self.pos=="NO" or self.pos=="NE") and not pygame.mixer.Channel(0).get_busy():
                            if game.sound:
                                pygame.mixer.Channel(0).play(game.tank_full)

            #---------------------------------------   
            # Here the tank is overflow
            # self.t = [1,1,1,1] < tank full && cement가 또 떨어지는 상황
            #---------------------------------------
            else:
                ## change
                if self.pos=="NO" or self.pos=="NE": ## 위층 탱크
                    for obj in game.allBars:
                        if obj.rect.top==175 and obj.side==self.side: ## 탱크로 떨어지는 시멘트
                            obj.kill() ## 삭제

                elif self.pos=="SO" or self.pos=="SE": ## 아래층 탱크
                    for obj in game.allBars:
                        if obj.rect.top==265 and obj.side==self.side: ## 탱크로 떨어지는 시멘트
                            obj.kill() ## 삭제

                game.stop=True # 게임을 멈춘다
               
                #---------------------------------------
                # Update the driver
                #---------------------------------------
                for obj in game.allDrivers:
                    if obj.side==self.side: # 탱크가 넘친 쪽의 운전자
                            obj.state=1 # 시멘트가 떨어진 상태로 바꿔준다

                for tank in game.allTanks:
                    # Tank at top is overflow, erase the two tanks at the top
                    # 탱크가 넘치면 위층 탱크의 시멘트는 사라진다
                    if (tank.pos=="NO" or tank.pos=="NE"):
                        tank.t=[0]*4 # 탱크를 비운다
                    # Tank at bottom is overflow, delete only the last cement
                    # 아래층 탱크가 넘치면 넘친 시멘트만 사라진다
                    elif (tank.pos=="SO" and tank.t==[1,1,1,1])  or  (tank.pos=="SE" and tank.t==[1,1,1,1]):
                        tank.t=[0,1,1,1]  # 차있는 상태로 유지된다
            self.laps=0 # 시간 초기화
            self.update_tank=False

class Bar(pygame.sprite.Sprite):
    '''
    The bars for the tanks
    '''
    #생성자 파라미터로 스프라이트에 사용될 이미지 경로와 스프라이트 초기 위치를 받는다
    def __init__(self,y=175,bonus=0,side="left"):
        pygame.sprite.Sprite.__init__(self)
        self.side=side
        self.bonus=bonus
        
        # Cement  is already in tank, so it is a bar
        # 탱크 안의 시멘트는 바 이미지
        if y!=175 and  y!=265:
            if self.bonus:
                self.image=game.ciment3
            else:
                self.image=game.ciment2
        else: # 탱크로 떨어지는 이미지
            if self.bonus:
                self.image=game.ciment1 # 보너스 시멘트
            else:
                self.image=game.ciment0 # 일반 시멘트
                    
        self.rect=self.image.get_rect()
        
        if self.side=="left": # 왼쪽
            self.rect.left=40 # x좌표
        else: # 오른쪽
            self.rect.left=565
        self.rect.top=y # y좌표
        game.allBars.add(self)
    
    def update(self):
        # 스프라이트 상태를 업데이트 하는 함수        
        '''
        Nothing to do here; The bars are handled in class Tank
        '''
        pass

## change
class Heart(pygame.sprite.Sprite): ## heart아이템

    def __init__(self,x=272,side="left",count=0):

        pygame.sprite.Sprite.__init__(self)
        self.image=game.heart01 ## 이미지 지정
        self.rect=self.image.get_rect()
        game.allHearts.add(self)

        self.y=[97,165,235,309,389] ## y좌표 배열
        self.rect.left=x+17 ## x좌표
        self.side=side ## 방향
        self.count=count ## y배열의 인덱스
        self.rect.top=self.y[self.count] ## y좌표 설정

class Elevator(pygame.sprite.Sprite): 
    '''
    The elevators and count variable for left or right elevaror
    Stage 5 self.count=0 || self.count=5
    Stage 4 self.count=1 || self.count=4
    Stage 3 self.count=2 || self.count=3
    Stage 2 self.count=3 || self.count=2
    Stage 1 self.count=4 || self.count=1
    Stage 0 self.count=5 || self.count=0
    '''
    def __init__(self,x=255,side="left",new=None):
        
        pygame.sprite.Sprite.__init__(self)        
        self.image=pygame.Surface((64,8)).convert_alpha() # 64x8 크기의 막대기
        self.image.fill(BLACK) # 검은색으로 채운다
        self.rect=self.image.get_rect()
        
        # Position from top to bottom
        # 각 층의 y좌표 
        # stage 5 4 3 2 1 
        self.y=[122,190,260,334,414]
        self.x = x ## x좌표
        self.side=side # 방향
        self.stage=[5,4,3,2,1] # 층
        self.new=new # 새로운 엘레베이터를 만드는 위치
        self.laps=0
        
        if self.side=="left": # 왼쪽
            self.count=0 # 5층
            #self.new=randint(2,4)
            if self.new!=2:
                self.new=2 # stage 3
            elif self.new==2:
                self.new=randint(2,4) # Stage 3|2|1
                
            self.rect.top=122 # y좌표 설정
            
        else: # 오른쪽
            self.count=4 # 1층
            self.new=randint(1,2) # Stage 4|3
            self.rect.top=414 # y좌표 설정
        
        self.rect.left=x # x좌표 설정
        
        self.clock=pygame.time.Clock() # 화면을 초당 몇 번 출력하는가를 설정하기 위해 선언되는 변수
        self.laps=0
        
        game.allElevators.add(self)
        game.play_sound(game.elevator_move) # 엘레베이터가 움직이는 효과음

        ## change
        #self.heart=1
        self.heart=randint(0,6) ## 1/7 확율로 heart 아이템 생성
        if self.heart==1:
            heart=Heart(self.x,self.side,self.count) ## heart 아이템 생성
        
    def update(self):
        
        '''
        for e in enumerate(game.allElevators):
            print (e,e[1].laps,mario.ko)
       '''
         
        self.clock.tick()    
        if mario.ko==False: # 마리오가 살아있으면
            
            self.laps+=self.clock.get_time() # 경과시간
            if self.laps>game.speed:
                
                #-----------------------
                # Left Elevator 
                #-----------------------               
                if self.side=="left": # 왼쪽

                    if self.count<4: # 2~5층
                        self.count+=1 # 내려간다
                        self.laps=0 # 시간 초기화
                        self.rect.top=self.y[self.count] # y좌표 설정
                        if game.stop==False:
                            game.play_sound(game.elevator_move) # 효과음

                        ## heart 아이템이 있으면 함께 이동한다
                        for obj in game.allHearts:
                                if obj.count==self.count-1 and obj.side==self.side: ## 동일한 위치에 있는 하트 아이템
                                    obj.kill() ## 삭제
                                    heart=Heart(self.x,self.side,self.count) ## 아래로 이동
                            
                        #------------------------------------------
                        # Move the Mario with elevator
                        # 마리오의 fall_left가 false면 엘레베이터 위에 있음을 의미하고
                        # none이면 엘레베이터 위에 있지 않고, 떨어지지 않음을 의미
                        #------------------------------------------
                        
                        if mario.fall_left==False: # 엘레베이터 위에 있으면

                            if self.heart == 1: ## 하트 아이템이 있으면
                                for obj in game.allHearts:
                                    if obj.count==self.count and obj.side==self.side: ## 동일한 위치에 있는 하트 아이템
                                        obj.kill() ## 삭제
                                        mario.deleteMiss() ## miss 삭제
                                
                            if mario.posy>1: # 2~5층에 있으면
                               mario.posy-=1 # 엘레베이터와 함께 내려간다
                               mario.fall_left=None
                            
                            # 마리오가 움직이는 층에 따른 x좌표를 설정해준다
                            if mario.posy==4: # 4층
                               mario.posx=0
                            elif mario.posy==2 or mario.posy==3: # 2, 3층
                               mario.posx=3
                            elif mario.posy==1: # 1층
                               mario.posx=1
                            elif mario.posy==0: # 맨 아래
                                mario.fall_left=True # 떨어진다
                        
                            
                        # Make a new elevator
                        # 엘레베이터가 new에 위치하면 새로운 엘레베이터를 만든다
                        if  self.count==self.new:
                            elevator=Elevator(255,"left",self.new)

                    else: # 1층이면
                        ## 하트 아이템 삭제
                        for obj in game.allHearts:
                                if obj.count==self.count and obj.side==self.side: ## 동일한 위치에 있는 하트 아이템
                                    obj.kill() ## 삭제

                        self.reset() # 사라진다
                
                if self.laps>game.speed+50: # game speed에 50ms가 지나면                    
                #-----------------------
                # Right Elevator
                #-----------------------
                
                    if self.count>0: # 1~4층이면
                        self.count-=1 # 올라간다
                        self.laps=0
                        self.rect.top=self.y[self.count] # y좌표 설정
                        if game.stop==False:
                            game.play_sound(game.elevator_move) # 효과음

                        ## heart 아이템이 있으면 함께 이동한다
                        for obj in game.allHearts:
                                if obj.count==self.count+1 and obj.side==self.side: ## 동일한 위치에 있는 하트 아이템
                                    obj.kill() ## 삭제
                                    heart=Heart(self.x,self.side,self.count) ## 위로 이동
                        
                        #------------------------------------------
                        # Move the Mario with elevator
                        #------------------------------------------                       
                        if mario.fall_right==False: # 마리오가 엘레베이터 위에 있으면

                            if self.heart == 1: ## 하트 아이템이 있으면
                                for obj in game.allHearts:
                                    if obj.count==self.count and obj.side==self.side: ## 동일한 위치에 있는 하트 아이템
                                        obj.kill() ## 삭제
                                        mario.deleteMiss() ## miss 삭제

                            if mario.posy<5: # 1~4층에 있으면
                                mario.posy+=1 # 엘레베이터와 함께 올라간다
                                mario.fall_right=None

                            # 마리오가 움직이는 층에 따른 x좌표를 설정   
                            if mario.posy==4: # 4층
                                mario.posx=1
                            elif mario.posy==2 or mario.posy==3: # 2, 3층
                               mario.posx=4
                            elif mario.posy==1: # 1층
                               mario.posx=2
                            elif mario.posy==5: # 5층
                                 mario.posx=0
                                 mario.fall_right=True
                                 mario.fall("right")
                               
                        # Make a new elevator
                        if  self.count==self.new:
                            elevator=Elevator(325,"right") # 새로운 엘레베이터를 만든다
                            
                    else: # 5층이면
                        ## 하트 아이템 삭제
                        for obj in game.allHearts:
                                if obj.count==self.count and obj.side==self.side: ## 동일한 위치에 있는 하트 아이템
                                    obj.kill() ## 삭제

                        self.reset() # 사라진다
            else:
                # Wait until game.SPEED 
                # game speed만큼의 시간이 흐르게 하는 부분
                pass
                
        else: # 마리오가 죽었으면
            pass
            
    def reset(self):
        self.kill() # 없어진다

class Driver(pygame.sprite.Sprite):
    '''
    The Drivers of the trucks
    '''
    def __init__(self,side="left"):
        
            pygame.sprite.Sprite.__init__(self)
            self.state=0 # 운전자의 머리 위에 시멘트가 떨어지면 1로 바뀐다
            self.clock=pygame.time.Clock()
            self.laps=0
            
            self.side=side
            
            if self.side=="left": # 왼쪽
                self.image=game.driver[0] # 이미지 설정
                self.rect=self.image.get_rect()
                self.rect=self.rect.move(93,360) # 위치 설정
            elif self.side=="right": # 오른쪽
                self.image=game.driver[3]
                self.rect=self.image.get_rect()
                self.rect=self.rect.move(500,360) 
            
            #self.blink=False # used for the blinking    
            game.allDrivers.add(self)
            
    def update(self):
        
        self.clock.tick()
        
        #-----------------------------------------------------------------------------------
        # Set the coordinates and the image for driver 
        # with cement over the head and driver ko for left and right
        # 운전자의 좌표 및 이미지 설정
        # 머리에 시멘트가 떨어지면 운전자 ko > miss 발생
        #-----------------------------------------------------------------------------------
        
        if self.side=="left": # 왼쪽
            self.coordinates=[(93,360),(105,420)] # 위치 배열
            self.image_index=[0,1,2] # 이미지
        elif self.side=="right": # 왼쪽
            self.coordinates=[(500,360),(435,420)] # 위치 배열
            self.image_index=[3,4,5] # 이미지
   
        if self.state!=0: # 탱크가 넘쳐서 시멘트가 운전자 위로 떨어진 경우
            self.laps+=self.clock.get_time() # 경과 시간
            if self.state==1 and self.laps<1000:
                # Driver with cement over the head
                # 탱크가 넘치고 1초동안 운전자의 머리에 시멘트가 떨어진 이미지를 보여준다
                self.image=game.driver[self.image_index[1]] # 머리에 시멘트가 떨어진 이미지
                self.rect=self.image.get_rect()
                self.rect=self.rect.move(self.coordinates[0]) # 위치 설정
                if  game.sound and not pygame.mixer.Channel(1).get_busy():
                            pygame.mixer.Channel(1).play(game.mario_fall) # 효과음
            elif self.state==1 and self.laps<game.speed:
                # Driver is Ko
                # 1초가 지난 후 화물차에서 떨어진 운전자의 이미지를 보여준다
                self.image=game.driver[self.image_index[2]] # 운전자가 화물차에서 떨어진 이미지
                self.rect=self.image.get_rect()
                self.rect=self.rect.move(self.coordinates[1]) # 위치 설정
            elif self.state<8: # 7번 깜빡인다
                    self.blink()
            else:
                # replace the Driver
                # 운전자를 원래 설정으로 돌려준다
                self.state=0
                self.image=game.driver[self.image_index[0]] # 이미지
                self.rect=self.image.get_rect()
                self.rect=self.rect.move(self.coordinates[0]) # 위치

                #------------------------
                # Erase the tank
                #------------------------
                # Remove the bars at the top
                # 위층 탱크에 들어있는 시멘트를 모두 삭제한다
                for b in game.allBars:
                    if b.rect.top<265: # 위층 탱크
                        game.allBars.remove(b) # 시멘트바를 삭제한다
                game.stop=False
                # Decrease a life
                mario.dead() # miss 발생

    def blink(self):
        if self.laps<500:
            self.rect.left=-1000 # 이미지를 이동시켜 화면밖으로 사라지게 한다
        elif self.laps<1000:
            self.image=game.driver[self.image_index[2]] # 이미지 설정
            self.rect=self.image.get_rect()
            self.rect=self.rect.move(self.coordinates[1]) # 화면에 보이도록 위치 설정
        else:
            self.laps=0
            self.state+=1 # 한 번 깜빡일 때 마다 state 한번씩 증가

class Lever(pygame.sprite.Sprite):
    '''
        The Levers used to make fall down  the cement
        Lever can be on left 
        each lever is up or down
    '''
    def __init__(self,pos,switch):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.pos=pos # 위치(NO: 왼쪽 위, SO: 왼쪽 아래, NE: 오른쪽 위, SE: 오른쪽 아래)
        self.switch=switch # 레버의 열림 여부 (up: 열림, down: 닫힘)
        self.clock=pygame.time.Clock() # use to move up
        self.laps=0 # 경과시간
        
        self.init()
        
    def init(self):
        
        # Determines the positions and the image  of the levers
        # 이미지를 설정한다
        # Left Levers
        if (self.pos=="NO" or self.pos=="SO") and  self.switch=="up":
            self.image=game.lever01 #레버가 올라가있는 기본 이미지
        # Right levers    
        elif (self.pos=="NE" or self.pos=="SE")  and  self.switch=="up":
            self.image=game.lever03 # lever01의 좌우반전 이미지
             
        # 레버의 위치를 설정한다     
        if self.pos=="NO": # 왼쪽 위
            self.rect=self.image.get_rect().move(95,230)
        elif self.pos=="SO": # 왼쪽 아래
            self.rect=self.image.get_rect().move(95,300)
        elif self.pos=="NE": # 오른쪽 위
            self.rect=self.image.get_rect().move(520,230)
        elif self.pos=="SE": # 오른쪽 아래
            self.rect=self.image.get_rect().move(520,300) 
    
    def update(self):
        
        self.clock.tick()
        
        #------------------------------------------------------------  
        # Tank is open for 100 milliseconds
        # 마리오가 스위치를 내리면 탱크를 100ms동안 연다
        #------------------------------------------------------------  
        if self.switch=="down" and self.laps<100:
            self.laps+=self.clock.get_time()
            
        #------------------------------------------------------------   
        # Close the tank and test cements and point
        # 100ms가 지나면 탱크를 닫고 
        # 윗층일 경우 increment를 1로, 아래층일 경우 2로 지정한다
        #------------------------------------------------------------
        else:
            # Only once time at the exit after 100 milliseconds
            if self.switch=="down": 
                    
                # Test used to fill the tank above
                if self.pos=="NO": # 왼쪽 위
                    for tank in game.allTanks:
                        if tank.pos=="NO" and tank.t[3]==1: # 왼쪽 위 탱크에 시멘트가 있으면
                            # Remove the bar in the tank NO
                            tank.t[3]=0 # 시멘트를 없앤다
                            for bar in game.allBars:
                                if bar.side=="left" and bar.rect.top==230: # 탱크 맨 아래의 시멘트 바를 없앤다
                                    self.bonus=bar.bonus ## 보너스 여부 기록
                                    game.allBars.remove(bar)  
                            ## change
                            if self.bonus: ## 보너스 시멘트면
                                score.increment=2 ## 2점 증가
                            else: ## 일반 시멘트면
                                score.increment=1 ## 1점 증가
                            # Fill the tank above
                            game.play_sound(game.cement_fall) # 시멘트가 떨어지는 효과음을 낸다
                            for tank in game.allTanks:
                                if tank.pos=="SO": # 왼쪽 아래 탱크
                                    tank.t[0]=1 # 맨 위에 시멘트 추가
                                    bar=Bar(265,self.bonus,"left") # 바 생성
                                
                elif self.pos=="NE": # 오른쪽 위
                    for tank in game.allTanks:
                        if tank.pos=="NE" and tank.t[3]==1: # 오른쪽 위 탱크에 시멘트가 있으면
                            # Remove the bar in the tank NE
                            tank.t[3]=0 # 시멘트를 없앤다
                            for bar in game.allBars:
                                if bar.side=="right" and bar.rect.top==230: # 탱크 맨 아래의 시멘트 바를 없앤다
                                    self.bonus=bar.bonus ## 보너스 여부 기록
                                    game.allBars.remove(bar)   
                            ## change
                            if self.bonus: ## 보너스 시멘트면
                                score.increment=2 ## 2점 증가
                            else: ## 일반 시멘트면
                                score.increment=1 ## 1점 증가
                            # Fill the tank above
                            game.play_sound(game.cement_fall) # 시멘트가 떨어지는 효과음
                            for tank in game.allTanks:
                                if tank.pos=="SE": # 오른쪽 아래 탱크
                                    tank.t[0]=1 # 맨 위에 시멘트 추가
                                    bar=Bar(265,self.bonus,"right") # 바 생성
                                
                elif self.pos=="SO": # 왼쪽 아래
                    for tank in game.allTanks:
                        if tank.pos=="SO" and tank.t[3]==1: # 왼쪽 아래 탱크에 시멘트가 있으면
                            # Remove the bar in the tank SO
                            tank.t[3]=0 # 시멘트를 없앤다
                            for bar in game.allBars:
                                if bar.side=="left" and bar.rect.top==315: # 탱크 맨 아래의 시멘트 바를 없앤다
                                    self.bonus=bar.bonus ## 보너스 여부 기록
                                    game.allBars.remove(bar)   
                            ## change
                            if self.bonus: ## 보너스 시멘트면
                                score.increment=4 ## 4점 증가
                            else: ## 일반 시멘트면
                                score.increment=2 ## 2점 증가
                            game.play_sound(game.cement_fall) # 시멘트가 떨어지는 효과음
                            # Cement over the left truck
                            cement=Cement(7,self.bonus) # 아래로 내려보낸다
                            game.allCements.add(cement) # 그룹에 추가
                            
                elif self.pos=="SE": # 오른쪽 아래
                    for tank in game.allTanks:
                        if tank.pos=="SE" and tank.t[3]==1: # 오른쪽 아래 탱크에 시멘트가 있으면
                            # Remove the bar in the tank SE
                            tank.t[3]=0 # 시멘트를 없앤다
                            for bar in game.allBars:
                                if bar.side=="right" and bar.rect.top==315: # 탱크 맨 아래의 시멘트 바를 없앤다
                                    self.bonus=bar.bonus ## 보너스 여부 기록
                                    game.allBars.remove(bar)   
                            ## change
                            if self.bonus: ## 보너스 시멘트면
                                score.increment=4 ## 4점 증가
                            else: ## 일반 시멘트면
                                score.increment=2 ## 2점 증가
                            game.play_sound(game.cement_fall) # 시멘트가 떨어지는 효과음
                            # Cement over the truck
                            cement=Cement(8,self.bonus) # 아래로 내려보낸다
                            game.allCements.add(cement) # 그룹에 추가
                                                 
            self.switch="up" # 스위치를 올려준다
            self.laps=0 # 시간 초기화
        self.init()
            
class Cement(pygame.sprite.Sprite):

    def  __init__(self,num=None,bonus=0):
        pygame.sprite.Sprite.__init__(self)
        
        self.clock=pygame.time.Clock()
        self.laps=0 # 경과 시간
        self.num=num
        self.bonus=bonus
        
        ## change
        # Cement over the left Truck
        # 왼쪽 화물차에 시멘트가 떨어진다
        if self.num==7:
            if bonus: ## 보너스 시멘트
                self.image=game.ciment5 ## 이미지 설정
            else: ## 일반 시멘트
                self.image=game.ciment4 ## 이미지 설정
            self.rect=self.image.get_rect()
            self.rect.left=45 # 위치 설정
            self.rect.top=350
            
        ## change
        # Cement over the right Truck
        # 오른쪽 화물차에 시멘트가 떨어진다
        elif self.num==8:
            if bonus: ## 보너스 시멘트
                self.image=game.ciment5 ## 이미지 설정
            else: ## 일반 시멘트
                self.image=game.ciment4 ## 이미지 설정
            self.rect=self.image.get_rect()
            self.rect.left=565 # 위치 설정
            self.rect.top=350   
                    
    def update(self):
    
        self.clock.tick()

        if self.laps<game.speed: # game speed만큼 시간을 보낸다
            self.laps+=self.clock.get_time()
        else:
            self.laps=0 # 시간 초기화
            self.kill()


class Trap(pygame.sprite.Sprite):
    # 탱크의 입구를 막는 막대기를 생성하고 레버의 열림 여부에 따라 열고 닫는다
    def __init__(self,side=None):
        
        pygame.sprite.Sprite.__init__(self)
        self.side=side # 트랩의 위치
        self.clock=pygame.time.Clock()
        self.laps=0 # 경과 시간
        self.switch="up" # 레버가 올라가 있도록 초기화
        self.init()
        
    def init(self):
        
        self.image=pygame.Surface((25,6)).convert_alpha() # 25x6의 막대로 탱크의 입구를 막는다
        self.image.fill(BLACK) # 검은색으로 채운다
        self.rect=self.image.get_rect()
        
        if self.switch=="up": # 위치 설정
            if self.side=="NO":
                self.rect=self.rect.move(52,260)
            elif self.side=="SO":
                self.rect=self.rect.move(52,340)
            elif self.side=="NE":
                self.rect=self.rect.move(572,260)
            elif self.side=="SE":
                self.rect=self.rect.move(572,340)
        else:
            self.image=pygame.transform.rotate(self.image,260) # 레버가 내려가 있으면 260도 회전해서 트랩을 연다
            if self.side=="NE":
                self.rect=self.rect.move(572,260)
            elif self.side=="SE":
                self.rect=self.rect.move(572,340)
            elif self.side=="NO":
                self.rect=self.rect.move(52,260)
            elif self.side=="SO":
                self.rect=self.rect.move(52,340)
        
    def update(self):
    
        self.clock.tick()
        # The trap is opened during one second
        if self.switch=="down" and self.laps<300: # 300ms동안 트랩을 열어둔다
            self.laps+=self.clock.get_time()
        # The trap is closed
        else: # 300ms가 지나면 트랩을 닫는다
            self.laps=0 # 시간 초기화
            self.switch="up" # up으로 바꿔준다
        self.init()

class Score:
    
    def __init__(self):
        self.point=0 # 점수(0점부터 시작)
        self.font=pygame.font.Font("./font/Digirtu_.ttf",44) # 폰트 설정
        self.font.set_bold(True) # bold
        self.score=self.font.render(str(self.point),1,BLACK) # 점수를 화면에 출력할 수 있도록 변경
        self.rect=self.score.get_rect()
        self.rect=self.rect.move(200,70) # 위치 설정
        self.inc = 1 # 보너스 점수
        self.laps=0 # 경과 시간
        self.clock=pygame.time.Clock()
        self.increment=0 # 추가할 점수
        self.fix1 = 0 ## change
        self.fix2 = 0 ## change
        
    def update(self):
    # laver에서 설정한 increment에 따라서 점수를 증가시킨다
    # increment가 1이면 점수를 1 증가시킨다
    # increment가 2면 먼저 점수를 1 증가시키고 200밀리초동안 기다린 다음 점수를 1 더 증가시킨다  
    # increment가 4면 150ms간격을 두고 총 4점 증가시킨다 
            self.clock.tick()
            
            if self.increment==1: # 1점 증가
                self.point+=1*self.inc # 1점 증가
                self.compute() # 위치를 계산해 화면으로 출력
                self.increment=0 # increment를 0으로 변경
                self.fix1 = 1 ## change
                self.fix2 = 1 ## change
                
            elif self.increment==2: # 2점 증가.1
                # Addint point immediat
                self.point+=1*self.inc # 먼저 1점 증가
                self.compute() # 위치를 계산해 화면으로 출력
                self.laps=0 # 시간 초기화
                self.increment=3 # increment를 3으로 변경
                self.fix1 = 1 ## change
                self.fix2 = 1 ## change

            elif self.increment==3: # 2점 증가.2
                # Wait 200 msecond before adding the next point
                self.laps+=self.clock.get_time()
                if self.laps>200: # 200ms후에 점수 증가
                     self.point+=1*self.inc # 1점 다시 증가 >> 총 2점 증가
                     self.compute() # 위치를 계산해 화면으로 출력
                     self.increment=0 # increment를 0으로 변경
                     self.fix1 = 1 ## change
                     self.fix2 = 1 ## change

            ## change
            elif self.increment==4: # 4점 증가.1
                # Addint point immediat
                self.point+=1*self.inc # 먼저 1점 증가
                self.compute() # 위치를 계산해 화면으로 출력
                self.laps=0 # 시간 초기화
                self.increment=5 # increment를 5로 변경
                self.fix1 = 1 ## change
                self.fix2 = 1 ## change

            ## change
            elif self.increment==5: # 4점 증가.2
                self.laps+=self.clock.get_time()
                if self.laps>150: # 150ms후에 점수 증가
                     self.point+=1*self.inc # 1점 다시 증가 >> 총 2점 증가
                     self.compute() # 위치를 계산해 화면으로 출력
                     self.increment=6 # increment를 6으로 변경
                     self.fix1 = 1 ## change
                     self.fix2 = 1 ## change

            ## changecl
            elif self.increment==6: # 4점 증가.3
                self.laps+=self.clock.get_time()
                if self.laps>300: # 300ms후에 점수 증가
                     self.point+=1*self.inc # 1점 다시 증가 >> 총 3점 증가
                     self.compute() # 위치를 계산해 화면으로 출력
                     self.increment=7 # increment를 7로 변경
                     self.fix1 = 1 ## change
                     self.fix2 = 1 ## change
            ## change
            elif self.increment==7: # 4점 증가.4
                self.laps+=self.clock.get_time()
                if self.laps>450: # 450ms후에 점수 증가
                     self.point+=1*self.inc # 1점 다시 증가 >> 총 4점 증가
                     self.compute() # 위치를 계산해 화면으로 출력
                     self.increment=0 # increment를 0으로 변경
                     self.fix1 = 1 ## change
                     self.fix2 = 1 ## change
                     
            elif self.increment==0: # increment가 0이면
                self.laps=0 # 시간 초기화

           ## change
            if self.point % 5 == 0 and self.fix1: ## 5점을 얻을 때 마다 속도가 빨라진다  
                game.speed -= 250 ## 250씩 증가
                self.fix1 = 0 ## change

            ## change
            if self.point % 10 == 0 and self.fix2: ## 10점을 얻을 때 마다 축하 메세지를 출력한다
                self.celebrate() ## 축하메세지 출력
                self.fix2 = 0 ## change

            # Double point if 200 points is reached without lose a life
            # miss를 발생시키지 않고 200점을 넘으면 점수를 두배로 얻는다
            if self.point >= 200 and mario.life == 3:
               self.inc = 2 # 보너스로 점수를 2배로 얻는다
            elif mario.life != 3: # 생명을 잃으면 보너스는 사라진다
                self.inc = 1

    def compute(self): 
    # 점수의 자릿수에 따라 달라지는 점수의 화면상의 위치를 계산한다        
            self.score=self.font.render(str(self.point),1,BLACK)
            self.rect=self.score.get_rect()
            if self.point <10: # 한자릿수인 경우
                self.rect=self.rect.move(200,70)
            elif self.point<100: # 두자릿수인 경우
                self.rect=self.rect.move(180,70)
            elif self.point<1000: # 세자릿수인 경우
                self.rect=self.rect.move(160,70)
            else: # 네자릿수 이상인 경우
                self.point=game.point-999
                self.rect=self.rect.move(-200,70)
                game.surface.blit(game.bg,game.bg.get_rect())

    ## change
    def celebrate(self): ## 축하 메세지를 출력하는 클래스

        info=Information("congratulations!",100,200,3,RED) ## 축하 메세지
        game.allTexts.add(info) # 축하 메세지
        game.allTexts.clear(game.surface,game.bg) ## 메세지 그리기
        game.allTexts.draw(game.surface) ## 화면에 출력
        pygame.display.update() ## 화면 업데이트 
        pygame.time.wait(300) ## 300ms동안 출력
        info.kill()

        info=Information("congratulations!",100,200,3,ORANGE) # 축하 메세지
        game.allTexts.add(info) # 축하 메세지
        game.allTexts.clear(game.surface,game.bg) # 메세지 그리기
        game.allTexts.draw(game.surface) # 화면에 출력
        pygame.display.update() # 화면 업데이트 
        pygame.time.wait(300) ## 300ms동안 출력
        info.kill()

        info=Information("congratulations!",100,200,3,YELLOW) # 축하 메세지
        game.allTexts.add(info) # 축하 메세지
        game.allTexts.clear(game.surface,game.bg) # 메세지 그리기
        game.allTexts.draw(game.surface) # 화면에 출력
        pygame.display.update() # 화면 업데이트 
        pygame.time.wait(300) ## 300ms동안 출력
        info.kill()

        info=Information("you get the score " + str(self.point),100,200,3,GREEN) # 축하 메세지
        game.allTexts.add(info) # 축하 메세지
        game.allTexts.clear(game.surface,game.bg) # 메세지 그리기
        game.allTexts.draw(game.surface) # 화면에 출력
        pygame.display.update() # 화면 업데이트 
        pygame.time.wait(300) ## 300ms동안 출력
        info.kill()

        info=Information("you get the score " + str(self.point),100,200,3,BLUE) # 축하 메세지
        game.allTexts.add(info) # 축하 메세지
        game.allTexts.clear(game.surface,game.bg) # 메세지 그리기
        game.allTexts.draw(game.surface) # 화면에 출력
        pygame.display.update() # 화면 업데이트 
        pygame.time.wait(300) ## 300ms동안 출력
        info.kill()

        info=Information("you get the score " + str(self.point),100,200,3,BLACK) # 축하 메세지
        game.allTexts.add(info) # 축하 메세지
        game.allTexts.clear(game.surface,game.bg) # 메세지 그리기
        game.allTexts.draw(game.surface) # 화면에 출력
        pygame.display.update() # 화면 업데이트 
        pygame.time.wait(300) ## 300ms동안 출력
        info.kill()

        info=Information("you get the score " + str(self.point),100,200,3,GREY) # 축하 메세지
        game.allTexts.add(info) # 축하 메세지
        game.allTexts.clear(game.surface,game.bg) # 메세지 그리기
        game.allTexts.draw(game.surface) # 화면에 출력
        pygame.display.update() # 화면 업데이트 
        pygame.time.wait(300) ## 300ms동안 출력
        info.kill()

 
if __name__ == '__main__':
    environement()
    game=Game()
    score=Score()

    ## change
    btn1=Button(0,10,60) ## 게임설명
    btn2=Button(1,50,55) ## 음소거
    btn3=Button(3,260,200) ## 게임 다시시작
    game.allBtns.add(btn1)
    game.allBtns.add(btn2)
    
    # Mario
    mario=Mario()
    game.Mario.add(mario)
    
    # The two drivers
    driver=Driver("left") # 왼쪽 운전자 
    driver=Driver("right") # 오른쪽 운전자
    
    # Elevator left
    elevator_left=Elevator() # 왼쪽 엘레베이터 생성
    
    # The left bac
    bac=Bac("left") # 왼쪽 bac
    
    # The four tank
    tank1=Tank() # 왼쪽 위(NO)가 default 
    game.allTanks.add(tank1)
    tank2=Tank("NE") # 오른쪽 위 탱크
    game.allTanks.add(tank2)
    tank3=Tank("SO") # 왼쪽 아래 탱크
    game.allTanks.add(tank3)
    tank4=Tank("SE") # 오른쪽 아래 탱크
    game.allTanks.add(tank4)
    
    # The four levers
    lever01=Lever("NE","up") # 오른쪽 위 레버
    lever02=Lever("NO","up") # 왼쪽 위 레버
    lever03=Lever("SE","up") # 오른쪽 아래 레버
    lever04=Lever("SO","up") # 왼쪽 아래 레버
    game.allLevers.add(lever01)
    game.allLevers.add(lever02)
    game.allLevers.add(lever03)
    game.allLevers.add(lever04)

    # The four Trap
    trap01=Trap("NE") # 오른쪽 위 트랩
    trap02=Trap("NO") # 왼쪽 위 트랩
    trap03=Trap("SE") # 오른쪽 아래 트랩
    trap04=Trap("SO") # 왼쪽 아래 트랩
    game.allTraps.add(trap01)
    game.allTraps.add(trap02)
    game.allTraps.add(trap03)
    game.allTraps.add(trap04)

    #매개변수로 surface객체를 자신에게 그려넣는다
    # 첫 번째 매개변수가 그려넣을 객체, 두 번째 매개변수가 그려넣을 좌표
    game.surface.blit(game.bg,game.bg.get_rect()) # 배경을 그려넣는다
    
    info=Information("Game A",420,70,1) # 문자열 화면에 출력
    game.allTexts.add(info)
    info=Information("Mario Cement Factory by space.max@free.fr",150,5,2,WHITE) # 문자열 화면에 출력
    game.allTexts.add(info)
    
    while not events_handle(): # 이벤트가 발생하는 동안
        while not events_handle() and mario.life!=0: # 생명이 남아있는 동안 
            # print (game.speed)
            if game.stop==False: # 멈추지 않는다
                                
                # Elevator at right is created afer 800 milliseconds
                # 오른쪽 엘레베이터는 800ms뒤에 생성된다
                if game.laps>800 and game.launchRight==False:
                    game.launchRight=True
                    elevator_right=Elevator(325,"right") # 오른쪽 엘레베이터
                    bac=Bac("right") # 오른쪽 bac
              
                #game.surface.blit(info.text,info.rect)
                game.allTexts.clear(game.surface,game.bg) # sprite에 해당하는 부분만 blit한다
                game.allTexts.draw(game.surface) # 화면에 출력
                
                score.update() # 점수의 변화 감지
                game.surface.blit(game.bg,score.rect,score.rect)
                game.surface.blit(score.score,score.rect) # 점수를 그린다
                
                game.allLevers.clear(game.surface,game.bg) # 레버를 그린다
                game.allLevers.draw(game.surface) # 레버를 화면에 출력
                game.allLevers.update() # 레버의 상태 변화
                
                game.allHearts.clear(game.surface,game.bg) ## heart 아이템을 그린다
                game.allHearts.draw(game.surface) ## 화면에 출력
                game.allHearts.update() ## heart 아이템의 상태변화
                
                game.Mario.clear(game.surface,game.bg) # 마리오를 그린다
                game.Mario.draw(game.surface) # 마리오를 화면에 출력
                game.Mario.update() # 마리오의 상태 변화
                
                game.allElevators.clear(game.surface,game.bg) # 엘레베이터를 그린다
                game.allElevators.draw(game.surface) # 엘레베이터 출력
                game.allElevators.update() # 엘레베이터의 상태 변화
                
                game.allCements.clear(game.surface,game.bg) # 시멘트를 그린다
                game.allCements.draw(game.surface) # 시멘트 출력
                game.allCements.update() # 시멘트의 상태 변화
                
                game.allBtns.clear(game.surface,game.bg) ## 버튼을 그린다
                game.allBtns.draw(game.surface) ## 버튼을 화면에 출력
                
                game.allBacs.clear(game.surface,game.bg) # bac을 그린다
                game.allBacs.draw(game.surface) # bac을 화면에 출력
                
                game.allTanks.clear(game.surface,game.bg) # 탱크를 그린다
                game.allTanks.draw(game.surface) # 화면에 출력
                
                game.allBars.clear(game.surface,game.bg) # 시멘트 바를 그린다
                game.allBars.draw(game.surface) # 화면에 출력
                
                game.allTraps.clear(game.surface,game.bg) # 트랩을 그린다
                game.allTraps.draw(game.surface) # 트랩 화면에 출력
                
                game.allMiss.clear(game.surface,game.bg) # miss를 그린다
                game.allMiss.draw(game.surface) # 화면에 출력

                
                # Moves all the  objects only if Mario is not falling down
                # 모든 물체는 마리오가 떨어지지 않았을때만 움직인다
                if mario.fall_left!=True and mario.fall_right!=True:
                    game.clock.tick(FPS)
                    game.laps+=game.clock.get_time()
                    game.allBacs.update() # bac의 상태 변화
                    
                    game.allTanks.update() # 탱크 상태 변화
                    #game.allBars.update() # 시멘트 바의 상태 변화
                    game.allTraps.update() # 트랩 상태 변화
                else:
                    game.clock.tick(0)
                    #----------------------------------------------------------------------
                    # Gerer les 2 derniers  ciments sur Game.stop=True
                    # ciment3,4,5 et 6
                    #----------------------------------------------------------------------
                    
    
            game.allDrivers.clear(game.surface,game.bg) # 운전자 그리기
            game.allDrivers.draw(game.surface) # 화면에 출력
            game.allDrivers.update() # 상태 변화
            game.allBars.clear(game.surface,game.bg) # 시멘트 바를 그린다
            game.allBars.draw(game.surface) # 화면에 출력
            # Elevators are updated but they are not moving in order to preserve theirs life time...
            game.allElevators.update() # 엘레베이터의 상태 변화
            pygame.display.update() # 화면 업데이트

         # miss가 세번 발생하거나 esc를 누른 경우 game over  
        info=Information("Game Over. Press Esc",185,20,0,GREEN) # 게임오버 메세지
        while not events_handle(): # 게임이 끝났다
            game.allTexts.add(info) # 게임오버 메세지
            game.allTexts.clear(game.surface,game.bg) # 메세지 그리기
            game.allTexts.draw(game.surface) # 화면에 출력
            game.allBtns.add(btn3) ## retry 버튼
            game.allBtns.clear(game.surface,game.bg) ## 버튼을 그린다
            game.allBtns.draw(game.surface) ## 버튼을 화면에 출력
            pygame.display.update() # 화면 업데이트 
            pygame.time.wait(150) # 150ms동안 기다린다
        exit() # 종료
