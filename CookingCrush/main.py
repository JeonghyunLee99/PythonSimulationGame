import pygame #게임을 만들기 위한 pygame 라이브러리 
import random #랜덤 라이브러리

class Stage: 
    def __init__(self, width, height, foodlist):
        self.width = width # 가로 줄 음식의 개수 
        self.height = height # 세로 줄 음식의 개수
        self.x = (800-((width*60)+((width-1)*5)))//2  # 1행 1열에 올 음식의 초기 x값
        self.y = (800-((height*60)+((height-1)*5)))//2-45 # 1행 1열에 올 음식의 초기 y값
        self.foodlist = foodlist # 음식 종류의 리스트를 self.foodlist에 할당
        self.condition = True # self.condition = True 변수 선언

        self.stage = [] # 빈 리스트 생성
        tmp = [] # 빈 리스트 생성
        for j in range(height): # 인자로 넘겨받은 height만큼 반복
            for i in range(width): # 인자로 넘겨받은 width만큼 반복
                tmp.append(Grid(self.x+i*65,self.y+j*65,j,i,random.choice(self.foodlist))) # self.x(초기x) + i*65, self.y(초기y) i*65, j, i, random한 self.foodlist를 받은 Grid를 tmp에 추가
            self.stage.append(tmp) # self.stage에 tmp를 추가
            tmp = [] #tmp 초기화
         
    def update(self): # stage update 메소드
        li = [] # 빈 리스트li 생성
        for i in self.stage: # i에 self.stage의 요소를 넘겨 줌 (위에 의해 Grid를 담은 리스트를 넘겨줌)
            for j in i: # j에 Grid를 담은 리스트의 요소 하나하나를 넘겨 줌
                if j: # j가 존재하는지 검사
                    li.append(j.update()) # j는 Grid 객체이므로 j는 Grid객체의 update메소드를 수행하고 이를 li에 추가한다
        return li # li 반환

    def fallen(self):
        for j in range(len(self.stage[0])): # 0부터 (self.stage[0]의 길이-1)까지 오름차순으로 하나씩 j에 할당
            for i in range(len(self.stage)): # 0부터 (self.stage의 요소(리스트) 수-1)까지 오름차순으로 하나씩 i에 할당 (세로방향을 위한 2중 for문)
                if not self.stage[i][j] and i-1>=0 and self.stage[i-1][j]: # 2열~끝열 중, self.stage[i][j](음식)이 존재하지 않고, self.stage[i-1][j](음식)이 존재 할 때 
                    self.stage[i-1][j].fall() # self.stage[i-1][j](Grid 객체)은 fall메소드가 적용된다. (fall메소드는 class Grid의 메소드임)
                    self.stage[i][j],self.stage[i-1][j] = self.stage[i-1][j],self.stage[i][j] # self.stage[i][j],self.stage[i-1][j]를 서로 바꿔준다.
        for j in range(len(self.stage[0])): # 0부터 (self.stage[0]의 길이-1)까지 오름차순으로 하나씩 j에 할당 
            for i in range(len(self.stage)-1): # 0부터 (self.stage의 요소(리스트) 수-2)까지 오름차순으로 하나씩 i에 할당
                if self.stage[i][j] and not self.stage[i+1][j]: # self.stage[i][j]가 존재하고, self.stage[i+1][j]가 존재하지 않을 때
                    self.fallen() # 객체 자신은 fallen메소드를 호출한다
        return self.stage # self.stage를 리턴한다

    def check(self):
        for i in range(len(self.stage)): # 0부터 (self.stage의 요소(리스트) 수-1)까지 오름차순으로 하나씩 i에 할당
            for j in range(len(self.stage[0])): # 0부터 (self.stage[0]의 길이-1)까지 오름차순으로 하나씩 j에 할당 (가로방향을 위한 2중 for문)
                if type(self.stage[i][j])!=int and (self.stage[i][j].move_y or self.stage[i][j].move_x): # self.stage[i][j]의 타입이 int가 아니면서 self.stage[i][j].move_y 또는 self.stage[i][j].move_x가 0이 아닐 때
                    return "moving",0,0 # ('moving', 0, 0)을 반환
        dli = self.stage # dli에 self.stage 할당 (얕은 복사)
        result = [] # 빈 리스트 result생성
        for i in range(len(dli)): # 0부터 (dli(self.stage의 요소(리스트)) 수-1)까지 오름차순으로 하나씩 i에 할당
            for j in range(len(dli[0])): # 0부터 (dli[0](self.stage[0])의 길이-1)까지 오름차순으로 하나씩 j에 할당
                if i+2<len(dli) and (len(set(list(map(str,[dli[i][j],dli[i+1][j],dli[i+2][j]]))))==1)\
                     and dli[i][j]!= 0: # i+2<len(dil)을 통해 맨위 음식부터 맨아래에서 3번째 까지 검사, dli[i][j],dli[i+1][j],dli[i+2][j] 각각을 map을 통해 str로 변환 후 리스트로 변환, 그 후 집합으로 변환시키고, 집합의 길이가 1인지 검사(dli[i][j],dli[i+1][j],dli[i+2][j]이 모두 같은지 검사 즉, 3x1 모양이 같은지 검사)
                    if not [i,j] in result: # 리스트 result에 리스트 [i,j]가 없는지 검사(없으면 참)
                        result.append([i,j]) # 리스트 result에 리스트 [i,j]를 추가
                    if not [i+1,j] in result: # 리스트 result에 리스트 [i+1,j]가 없는지 검사(없으면 참)
                        result.append([i+1,j]) # 리스트 result에 리스트 [i+1,j]를 추가
                    if not [i+2,j] in result: # 리스트 result에 리스트 [i+2,j]가 없는지 검사(없으면 참)
                        result.append([i+2,j]) # 리스트 result에 리스트 [i+2,j]를 추가
                if i+1<len(dli) and j+1<len(dli[0])\
                    and(len(set(list(map(str,[dli[i][j],dli[i+1][j],dli[i][j+1],dli[i+1][j+1]]))))==1)\
                     and dli[i][j]!=0: # 위와 비슷한 원리로 2x2 모양의 같은 음식이 있는지 검사
                    if not [i,j] in result: # 리스트 result에 리스트 [i,j]가 없는지 검사(없으면 참)  
                        result.append([i,j]) # 리스트 result에 리스트 [i,j]를 추가
                    if not [i+1,j] in result: # 리스트 result에 리스트 [i+1,j]가 없는지 검사(없으면 참)
                        result.append([i+1,j]) # 리스트 result에 리스트 [i+1,j]를 추가
                    if not [i,j+1] in result: # 리스트 result에 리스트 [i,j+1]가 없는지 검사(없으면 참)
                        result.append([i,j+1]) # 리스트 result에 리스트 [i,j+1]를 추가
                    if not [i+1,j+1] in result: # 리스트 result에 리스트 [i+1,j+1]가 없는지 검사(없으면 참)
                        result.append([i+1,j+1]) # 리스트 result에 리스트 [i+1,j+1]를 추가
                if j+2<len(dli[0]) and (len(set(list(map(str,[dli[i][j],dli[i][j+1],dli[i][j+2]]))))==1)\
                     and dli[i][j]!=0: # 위와 비슷한 원리로 1x3모양이 같은지 검사
                    if not [i,j] in result: # 리스트 result에 리스트 [i,j]가 없는지 검사(없으면 참)  
                        result.append([i,j]) # 리스트 result에 리스트 [i,j]를 추가
                    if not [i,j+1] in result: # 리스트 result에 리스트 [i,j+1]가 없는지 검사(없으면 참)
                        result.append([i,j+1]) # 리스트 result에 리스트 [i,j+1]를 추가
                    if not [i,j+2] in result: # 리스트 result에 리스트 [i,j+2]가 없는지 검사(없으면 참)
                        result.append([i,j+2]) # 리스트 result에 리스트 [i,j+2]를 추가  
        for i,j in result: # result의 요소인 리스트 0번째 인덱스의 값과 1번째 인덱의 값을 i,j에 각각 할당
            dli[i][j] = 0 # dli[i][j]의 값을 0으로 바꿔 줌 (self.stage[i][j] = 0과 같음)
        score = len(result) # score에 result 안의 요소(리스트) 수를 score에 할당
        return (score, dli, result) # 튜플 형태로 score, dli, result의 값을 보내줌

    def fill(self): 
        for i in range(len(self.stage)): # 0부터 (self.stage의 요소(리스트) 수-1)까지 오름차순으로 하나씩 i에 할당
            for j in range(len(self.stage[0])):  # 0부터 (self.stage[0]의 길이-1)까지 오름차순으로 하나씩 j에 할당
                if self.stage[i][j]!=0 and self.stage[i][j].move_y: # self.stage[i][j]의 값이 0이 아니면서 sel.stage[i][j].move_y의 값이 0이 아닌지 검사
                    return # 종료? ~~
        for i in sorted(list(range(len(self.stage))),reverse=True): # (self.stage의 요소(리스트) 수-1)부터 0까지 내림차순으로 i에 할당
            for j in sorted(list(range(len(self.stage[0]))),reverse=True): # (self.stage[0]의 길이 -1)부터 0까지 내림차순으로 j에 할당
                if self.stage[i][j]==0: # 맨오른쪽 맨아래 요소부터 self.stage[i][j]의 값이 0인지 검사
                    self.stage[i][j] = Grid(self.x+j*65,self.y-65,i,j,random.choice(self.foodlist)) # self.x(초기x) + i*65, self.y(초기y) i*65, i, j, random한 self.foodlist를 받은 Grid를 tmp에 추가 (i, j가 아니라 j, i 순임)
                    self.stage[i][j].move_y += abs(self.y+(i+1)*65 - self.y) # self.stage[i][j]의 값은 Grid 객체이므로 그 객체의 인스턴스 변수 move_y의 값에 절댓값 self.y+(i+1)*65 - self.y의 값을 더한다. (거꾸로 검사하기에 절댓값을 이용한 계산)

    def test(self,pos): 
        x,y = pos # test메소드의 pos라는 인자의 0번째 인덱스, 1번째 인덱스 값을 각각 x,y에 할당
        for i in range(len(self.stage)): # 0부터 (self.stage의 요소(리스트) 수-1)까지 오름차순으로 하나씩 i에 할당
            for j in range(len(self.stage[0])): # 0부터 (self.stage[0]의 길이-1)까지 오름차순으로 하나씩 j에 할당
                if type(self.stage[i][j])==Grid and \
                    self.stage[i][j].rect.x <x< self.stage[i][j].rect.x+60 and \
                   self.stage[i][j].rect.y <y< self.stage[i][j].rect.y+60: # self.stage[i][j]의 타입이 class Grid인지, 인자로 받은 pos의 x,y가 모든 Grid객체 중 하나라도 내부에 속하는지 검사
                   return self.stage[i][j].pos_x,self.stage[i][j].pos_y # (self.stage[i][j].pos_x,self.stage[i][j].pos_y) 튜플 반환
        return (-10,-10) # 위 조건 불만족 시 (-10, -10) 튜플 반환

    def swap(self,i,j):
        if i[0]==j[0]: # 튜플i와 튜플j 각각의 0번째 인덱스가 같은지 검사
            value_x = self.stage[i[0]][i[1]].rect.x - self.stage[j[0]][j[1]].rect.x # self.stage[i[0]][i[1]].rect.x - self.stage[j[0]][j[1]].rect.x 의 값을 value_x에 할당
            self.stage[i[0]][i[1]].move_x = value_x*-1 # value_x*(-1)의 값을 self.stage[i[0]][i[1]](Grid 객체)의 move_x 변수에 할당
            self.stage[j[0]][j[1]].move_x = value_x # value_x의 값을 self.stage[j[0]][j[1]](Grid 객체)의 move_x 변수에 할당 (self.stage[i[0]][i[1]]가 아님에 유의)
            if value_x <0: # value_x의 값이 0보다 작은지 검사
                self.stage[i[0]][i[1]].pos_y += 1 # self.stage[i[0]][i[1]].pos_y에 1을 더해줌
                self.stage[j[0]][j[1]].pos_y -= 1 # self.stage[j[0]][j[1]].pos_y에 1을 빼줌 (i가 아님에 유의)
            else: # value_x의 값이 0보다 클 때
                self.stage[i[0]][i[1]].pos_y -= 1 # 위와 반대로 self.stage[i[0]][i[1]].pos_y에 1을 빼줌
                self.stage[j[0]][j[1]].pos_y += 1 # self.stage[j[0]][j[1]].pos_y에 1을 더해줌 (i가 아님에 유의)
            self.stage[i[0]][i[1]],self.stage[j[0]][j[1]] = self.stage[j[0]][j[1]],self.stage[i[0]][i[1]] # self.stage[i[0]][i[1]]과 self.stage[j[0]][j[1]]의 위치를 서로 바꿔줌
        elif i[1]==j[1]: # 튜플i와 튜플j 각각의 1번째 인덱스가 같은지 검사
            value_y = self.stage[i[0]][i[1]].rect.y - self.stage[j[0]][j[1]].rect.y # self.stage[i[0]][i[1]].rect.y - self.stage[j[0]][j[1]].rect.y 의 값을 value_y에 할당
            self.stage[i[0]][i[1]].move_y = value_y*-1 # value_y*(-1)의 값을 self.stage[i[0]][i[1]](Grid 객체)의 move_y 변수에 할당
            self.stage[j[0]][j[1]].move_y = value_y # value_x의 값을 self.stage[j[0]][j[1]](Grid 객체)의 move_y 변수에 할당 (self.stage[i[0]][i[1]]가 아님에 유의)
            if value_y <0: # value_y의 값이 0보다 작은지 검사
                self.stage[i[0]][i[1]].pos_x += 1 # self.stage[i[0]][i[1]].pos_x에 1을 더해줌
                self.stage[j[0]][j[1]].pos_x -= 1 # self.stage[j[0]][j[1]].pos_x에 1을 빼줌 (i가 아님에 유의)
            else: # value_y의 값이 0보다 클 때
                self.stage[i[0]][i[1]].pos_x -= 1 # 위와 반대로 self.stage[i[0]][i[1]].pos_x에 1을 빼줌
                self.stage[j[0]][j[1]].pos_x += 1 # self.stage[j[0]][j[1]].pos_x에 1을 더해줌 (i가 아님에 유의)
            self.stage[i[0]][i[1]],self.stage[j[0]][j[1]] = self.stage[j[0]][j[1]],self.stage[i[0]][i[1]] # self.stage[i[0]][i[1]]과 self.stage[j[0]][j[1]]의 위치를 서로 바꿔줌

class Grid(pygame.sprite.Sprite):
    def __init__(self,x,y,pos_x,pos_y,t): # 인자로 x, y, pos_x, pos_y, t를 받음
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.image.load('img/{}.png'.format(t)) # 스프라이트에 이미지 t를 지정한다. (위의 코드에서 알 수 있듯이, t는 random.choice(self.foodlist)이다.)
        self.type = t # t라는 음식의 이름을 self.type에 할당
        self.rect = self.surface.get_rect() # surface의 초기x, 초기y, 가로,세로 길이를 담은 객체를 self.rect에 할당
        self.pos_x = pos_x # 인자로 받은 pos_x를 self.pos_x에 할당
        self.pos_y = pos_y # 인자로 받은 pos_y를 self.pos_y에 할당 
        self.rect.x = x # 인자로 받은 x를 self.rect.x에 할당 (self.rect.x == self.rect[0])
        self.rect[1] = y # 인자로 받은 y를 self.rect.y에 할당 (self.rect.x == self.rect[1])
        self.move_x = 0 # self.move_x의 값을 0으로 초기화 및 선언
        self.move_y = 0 # self.move_y의 값을 0으로 초기화 및 선언
    
    def fall(self): 
        self.move_y += 65 # self.move_y의 값에 65를 더해줌
        self.pos_x += 1 # self.pos_x에 1을 더해줌

    def update(self):
        if self.move_x: # self.move_x 가 0이 아닌지 검사
            if self.move_x > 0: # self.move.x 값이 0보다 큰지 검사
                self.rect.x += 5 # self.rect.x의 값을 5 더해줌 
                self.move_x -= 5 # self.move_x의 값을 5 빼줌
            else: # self.move.x 값이 0보다 작을 때
                self.rect.x -= 5 # self.rect.x의 값을 5 빼줌
                self.move_x += 5 # self.move_x의 값을 5 더해줌
        if self.move_y: # self.move_y가 0이 아닌지 검사
            if self.move_y > 0: # self.move_y 값이 0보다 큰지 검사
                self.rect.y += 5 # self.rect.y의 값을 5 더해줌
                self.move_y -= 5 # self.move_y의 값을 5 빼줌
            else: # self.move.y 값이 0보다 작을 때
                self.rect.y -= 5 # self.rect.y의 값을 5 빼줌
                self.move_y += 5 # self.move_y의 값을 5 더해줌

        return self.surface, (self.rect.x, self.rect.y) # (self.surface, (self.rect.x, self.rect.y)) 튜플을 반환

    def __repr__(self):
        return self.type #  객체를 인간이 이해할 수 있는 평문으로 '표현'

    def __str__(self):
        return self.type # 서로 다른 자료형 간에 인터페이스를 제공하기 위함

class Button(pygame.sprite.Sprite):
    def __init__(self,x,y,width=80,height=50,color=(0,0,0),text='',textcolor=(255,255,255),func=None):
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.Surface([width,height]) #width = 80, height = 50인 surface 생성
        self.width,self.height,self.color = width,height,color # 객체의 width,height,color을 설정. 각각은 80,50,(0,0,0) (참고로 (0,0,0)은 검정이다.)
        self.surface.fill(color) # color로 surface를 채운다
        self.rect = self.surface.get_rect() # 객체의 (가로길이,세로길이) 튜플을 self.rect에 할당한다
        self.rect.x = x # surface의 초기 x위치를 지정한다
        self.rect.y = y # surface의 초기 y위치를 지정한다
        self.font = pygame.font.Font('font/cabin.ttf',20) # cabin.ttf폰트를 지정한다
        self.text = self.font.render(text,True,textcolor) # text의 속성을 설정한다 인수 각각은 text, antialias, color을 의미한다
        self.func = func # func를 self.func에 할당한다 default of func는 None이다

    def update(self):
        return self.surface, (self.rect.x,self.rect.y),\
            self.text, (self.rect.x+10,((self.rect.y*2+self.height)//2)-12) # (self.surface, (self.rect.x,self.rect.y), self.text, (self.rect.x+10,((self.rect.y*2+self.height)//2)-12))를 반환한다
    
    def over(self):
        pass

    def isClick(self,pos):
        if self.rect.x < pos[0] < self.rect.x+self.width: # 마우스로부터 받은 x위치가 self.rect.x와 self.rect.x+self.width 사이에 있는지 검사
            if self.rect.y < pos[1] < self.rect.y+self.height: # 마우스로부터 받은 y위치가 self.rect.y와 self.rect.y+self.width 사이에 있는지 검사
                if self.func: # self.func가 None이 아닌지 검사
                    self.func() # self.func 메소드 실행
                return True # 두 조건문이 모두 만족되면 True를 반환
        return False # 두 조건문 중 하나라도 만족되지 않으면 False를 반환

class Game:
    def __init__(self):
        pygame.init() # pygame 초기화
        pygame.mixer.init() # pygame mixer (사운드 관련) 초기화
        pygame.display.set_caption("CookingCrush!") # 실행창 이름을 설정
        self.screen = pygame.display.set_mode((800, 960)) # 게임 화면의 크기를 800x960으로 설정
        self.clock = pygame.time.Clock() # self.clock.tick과 같이 시간 관련 메소드를 편리하게 사용할 수 있도록 함
        self.stage = Stage(8,9,['h','c','p','o','t','s']) # Stage 객체 생성. 인자는 각각 가로의 음식 개수, 세로의 음식 개수, 음식 객체들의 이름을 모은 리스트 이다.
        self.first = () #첫번째 클릭 상자 좌표 
        self.second = () #두번째 클릭 상자 좌표
        self.score = 0 # 처음 score = 0 으로 초기화
        self.resetbutton = Button(280,692,text="RESET",func=self.reset) # resetbutton 객체 생성. 인자는 각각  x좌표, y좌표, text, func 이다 
        self.quitbutton = Button(600,692,text="QUIT") # quitbutton 객체 생성. 인자는 각각 x좌표, y좌표, text, func 이다
        self.font = pygame.font.Font('font/cabin.ttf',20) # font 설정
        self.zone = pygame.image.load("img/check.png") # 클릭시 빨간 네모테두리 이미지 설정
        self.sound = [pygame.mixer.Sound('sound/click.wav'),pygame.mixer.Sound('sound/score.wav')] # 사운드 2가지를 묶은 리스트 생성
        pygame.mixer.music.load('sound/b.wav') # main bgm을 로드한다
        pygame.mixer.music.set_volume(1) # 소리 크기 1로 설정 (1이 최대)
        pygame.mixer.Sound.set_volume(self.sound[0],10) # 클릭 소리 크기 1로 설정 (1보다 커도 최대가 1이므로 1로 설정) 
        pygame.mixer.music.play(-1) # 무한 반복
        pygame.time.delay(1300) # 로딩시간 설정
        
    def update(self):
        self.board = pygame.Surface([550,620]) # 가로 550, 세로 620 크기의 surface 생성
        self.score_board = pygame.Surface([130,50]) # 가로 130, 세로 50 크기의 surface 생성
        self.board.fill((140,75,10)) # (140, 75, 10) 의 색깔로 self.board를 채움 (괄호 안은 R,G,B 순이다)
        self.score_board.fill([140,75,10]) # (140, 75, 10)의 색깔로 score_board를 채움 
        self.screen.fill((255,255,255)) # 메인화면 screen의 색을 흰색으로 채움

        self.screen.blit(pygame.Surface([564,634]),(113,48)) # surface(겉 테두리) 그리기
        self.screen.blit(self.board,(120,55)) # self.board 그리기
        self.screen.blit(self.score_board,(113,692)) # self.score_board 그리기

        tmp = self.stage.update() # [Grid 객체, (x좌표, y좌표)]들이 요소로 들어있는 리스트를 tmp에 할당
        for i in tmp: # tmp의 요소(리스트)를 i에 하나씩 줌
            self.screen.blit(i[0],i[1]) # i[0](Grid 객체), i[1](x좌표,y좌표)임을 이용하여 screen에 Grid객체를 그림

        tmp = self.resetbutton.update() # resetbutton의 (테두리 객체, (x좌표, y좌표), 텍스트 객체, (x좌표, y좌표))의 튜플을 tmp에 넘겨 줌
        self.screen.blit(tmp[0],tmp[1]) # resetbutton 테두리 그리기
        self.screen.blit(tmp[2],tmp[3]) # resetbutton 텍스트 그리기
        tmp = self.quitbutton.update() # quitbutton의 (테두리 객체, (x좌표, y좌표), 텍스트 객체, (x좌표, y좌표))의 튜플을 tmp에 넘겨 줌
        self.screen.blit(tmp[0],tmp[1]) # quitbutton 테두리 그리기
        self.screen.blit(tmp[2],tmp[3]) # quitbutton 텍스트 그리기

        if self.first: # self.first이 빈튜플이 아닌지 검사
            self.screen.blit(self.zone,(self.first[0],self.first[1])) # self.zone을 x좌표: self.first[0], y좌표: self.first[1]에 그리기
        if self.second: # self.second가 빈튜플이 아닌지 검사
            self.screen.blit(self.zone,(self.second[0],self.second[1])) # self.zone을 x좌표: self.second[0], y좌표: self.second[1]에 그리기 
        self.screen.blit(self.font.render("SCORE : {}".format(self.score),True,(255,255,255)),(120,705)) # self.score을 검정색글씨로 antialias를 적용하여 (x: 120, y: 705)에 그린다
        pygame.display.update() # 파이게임 화면을 업데이트해준다

    def reset(self):
        for i in range(len(self.stage.stage)): # 0부터 (self.stage.stage의 요소(리스트) 수-1)까지 오름차순으로 하나씩 i에 할당
            for j in range(len(self.stage.stage[0])): # 0부터 (self.stage.stage[0]의 길이-1)까지 오름차순으로 하나씩 j에 할당
                self.stage.stage[i][j] = 0 # self.stage.stage[i][j]를 0으로 초기화
        self.score = 0 # self.score을 0으로 초기화

    def main(self):
        run = True # run을 True로 초기화
        self.score = 0 # self.score을 0으로 초기화
        firstc, secondc = (-10,-10),(-10,-10) # firstc와 secondc를 각각 (-10,-10)으로 초기화
        con = False # con을 False로 초기화
        while run: # 처음 초기화 된 run이 True이므로 특별한 일이 생기기 전까지 무한반복
            for event in pygame.event.get(): # 파이게임의 이벤트기능을 쓸 수 있도록 event를 받는다 
                if event.type == pygame.QUIT: # 종료버튼을 누르는지 검사
                    run = False # run의 값을 False로 바꿔준다 즉, 무한루프 탈출
                if event.type == pygame.KEYDOWN: # 키보드의 버튼을 누른 상태인지 검사
                    
                    pass
                if event.type == pygame.MOUSEBUTTONDOWN: # 마우스 버튼이 눌려진 상태인지 검사
                    self.resetbutton.isClick(pygame.mouse.get_pos()) # reset 버튼활성화로, 마우스 버튼의 (x좌표: pygame.mouse.get_pos()[0], y좌표: pygame.mouse.get_pos()[1])의 튜플을 isClick의 pos인자로 전달한다 그리고 isClick의 self.func()에 의해 reset 메소드가 실행된다
                    if self.quitbutton.isClick(pygame.mouse.get_pos()): # 마우스 버튼의 (x좌표: pygame.mouse.get_pos()[0], y좌표: pygame.mouse.get_pos()[1])의 튜플을 isClick의 pos인자로 전달한다
                        run = False # run 값을 False로 바꿔준다 즉, 무한루프 탈출
                    firstc = (-10,-10) # firstc를 (-10, -10)으로 초기화
                    firstc = self.stage.test(pygame.mouse.get_pos()) # 마우스 버튼의 (x좌표: pygame.mouse.get_pos()[0], y좌표: pygame.mouse.get_pos()[1])의 튜플을 test의 pos인자로 전달한다 그 후 self.stage.test의 반환값을 firstc에 할당한다 
                    if firstc!=(-10,-10): # firstc가 (-10, -10)이 아닐 때 즉, 마우스가 어떤 Grid객체 내부 좌표에 속할 때
                        tmp = self.stage.stage[firstc[0]][firstc[1]] # self.stage.stage[firstc[0]][firstc[1]]을 tmp에 할당
                        self.first = (tmp.rect.x,tmp.rect.y) # (tmp.rect.x,tmp.rect.y)의 튜플을 self.first에 할당 (클릭한 곳의 Grid객체의 x, y좌표)
                        pygame.mixer.Sound.play(self.sound[0]) # 클릭 소리 재생
                if event.type == pygame.MOUSEMOTION and firstc != (-10,-10) : # 마우스가 움직이고 firstc가 (-10, -10)이 아닌지 검사
                    pos = self.stage.test(pygame.mouse.get_pos()) # 마우스 버튼의 (x좌표: pygame.mouse.get_pos()[0], y좌표: pygame.mouse.get_pos()[1])의 튜플을 test의 pos인자로 전달한다 그 후 self.stage.test의 반환값을 pos에 할당한다
                    if pos!=(-10,-10): #pos가 (-10, -10)이 아닌지 검사
                        tmp = self.stage.stage[pos[0]][pos[1]] # self.stage.stage[pos[0]][pos[1]]을 tmp에 할당
                        self.second = (tmp.rect.x,tmp.rect.y) # (tmp.rect.x,tmp.rect.y)의 튜플을 self.second에 할당 (클릭한 곳의 Grid객체의 x, y좌표) 
                if event.type == pygame.MOUSEBUTTONUP: # 누른 마우스 버튼이 올라갈 때를 검사
                    secondc = (-10,-10) # secondc를 (-10, -10)으로 초기화
                    secondc = self.stage.test(pygame.mouse.get_pos()) # 마우스 버튼의 (x좌표: pygame.mouse.get_pos()[0], y좌표: pygame.mouse.get_pos()[1])의 튜플을 test의 pos인자로 전달한다 그 후 self.stage.test의 반환값을 secondc에 할당한다 

            #교체
            if abs(firstc[0]-secondc[0] + firstc[1]-secondc[1])==1 and self.first and self.second: # 십자가 모양으로 한칸 차이의 Grid객체를 선택했는지 검사 후 first 체크박스와 second 체크박스가 있는지 검사
                pygame.mixer.Sound.play(self.sound[0]) # 클릭 소리 재생
                self.stage.condition = True # self.stage.condition을 True로 초기화
                self.stage.swap(firstc,secondc) # swap함수의 인자 i, j에 각각 firstc, secondc를 할당
                a,b = firstc,secondc # a, b에 각각 firstc, secondc 할당
                con = True # con을 True로 초기화
                firstc, secondc = (-10,-10),(-10,-10) # firstc, secondc를 각각 (-10,-10), (-10,-10)로 초기화
                self.first , self.second = (),() # self.first , self.second를 각각 (), ()로 초기화

            check = self.stage.check() #점수 체크

            #교체후 점수가 획득되면 다시 교체 안함
            if check[0]!=0 and check[0]!="moving": # check[0]가 0이 아닌지 검사하고 "moving"이 아닌지 검사
                if check[0] > 6: # check[0]이 6보다 큰지 검사
                    pygame.mixer.Sound.play(self.sound[1]) # 득점 소리 재생
                elif check[0] > 4: # check[0]이 4보다 큰지 검사 
                    pygame.mixer.Sound.play(self.sound[1]) # 득점 소리 재생
                else: # check[0]이 4이하일 때
                    pygame.mixer.Sound.play(self.sound[1]) # 득점 소리 재생
                self.score += check[0] # self.score에 check[0]의 값을 더한다
                con = False # con 값을 False로 바꾼다

            #교체후 점수가 획득되지 않으면 다시 원래자리로
            if con and check[0]==0: # con이 True이고 check[0]가 0인지 검사
                con = False # con의 값을 False로 바꾼다
                self.stage.swap(a,b) # self.stage.swap함수의 인자 i, j에 a, b를 각각 대입한다

            self.stage.fallen() # stage의 fallen메소드 실행
            self.stage.fill() # 스테이지의 fill메소드 실행
            self.update() # update메소드 실행
            self.clock.tick(80) # 프레임 80
        pygame.quit() # pygame 종료

if __name__ == '__main__': # main 스크립트 파일일 때
    game = Game() # game이름의 Game 객체 생성
    game.main() # game 객체를 통한 main 메소드 실행

#swap  
#self.stage.stage
#reset  
