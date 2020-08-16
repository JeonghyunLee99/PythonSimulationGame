import random

# 우승시그널 프로그램 developed by 이정현

# 기존 월드컵은 조별리그 1, 2위 팀이 본선에 진출하지만,
# 본 프로그램에서는 조별리그 1위 한 팀만이 본선에 진출할 수 있습니다.

menu = 0
randNum = random.randint(0, 3)
randNum_final = random.randint(0, 7)
forecast_point = 0


class Group :
    group = []

    def __init__(self, group) :
        self.group = group

    def getGroup(self) :
        return self.group


groupA = Group(["러시아", "우루과이", "이집트", "사우디아라비아"])
groupB = Group(["이란", "포르투갈", "스페인", "모로코"])
groupC = Group(["프랑스", "덴마크", "호주", "페루"])
groupD = Group(["크로아티아", "아이슬란드", "아르헨티나", "나이지리아"])
groupE = Group(["브라질", "스위스", "코스타리카", "세르비아"])
groupF = Group(["독일", "멕시코", "스웨덴", "대한민국"])
groupG = Group(["벨기에", "파나마", "튀니지", "잉글랜드"])
groupH = Group(["폴란드", "세네갈", "콜롬비아", "일본"])

teamA = Group(["엑소", "방탄소년단", "워너원", "세븐틴"])
teamB = Group(["갓세븐", "아스트로", "뉴이스트", "비투비"])
teamC = Group(["하이라이트", "빅뱅", "동방신기", "슈퍼주니어"])
teamD = Group(["인피니트", "빅스", "위너", "아이콘"])
teamE = Group(["블락비", "몬스타엑스", "NCT", "2PM"])
teamF = Group(["틴탑", "더보이즈", "MXM", "샤이니"])
teamG = Group(["B1A4", "2AM", "씨엔블루", "BAP"])
teamH = Group(["펜타곤", "JBJ", "FT아일랜드", "골든차일드"])


def forecastResult(group, randNum, forecast) :
    print("\n본선진출 결과를 발표합니다.")
    print("1위:", group[randNum])
    groupWin = group[randNum]
    if (groupWin == forecast) :
        global forecast_point
        forecast_point += 1
        print(groupWin, "예상적중!! 예측하신 국가가 본선에 진출했습니다. \n당신은 진정한 축잘알!")
        print(forecast_point, "번 예측 성공하셨습니다.")
    else :
        print(forecast, "국가는 본선진출에 실패했습니다..\n축잘알이 되기 위한 길은 쉽지 않습니다. 한 번 더 도전해보세요!")
        print(forecast_point, "번 예측 성공하셨습니다.")
    return groupWin


def forecastVictory(group, groupName, groupExample) :
    print("-------------------------------------------------------------------")
    print("\n다음은 " + groupName + "조 승부예측을 할 차례입니다.")
    print("\n", group)
    forecast = checkName("\n본선 진출 할 조별리그 1위 예측 국가를 적어주세요. 예) " + groupExample + "\n예측 국가: ", group)
    groupWin = forecastResult(group, randNum, forecast)
    return groupWin


def pickGroup4(team, groupName) :
    print("\n", team)
    forecast = checkName("\n네 그룹 중에 가장 좋아하시는 남자 아이돌 그룹을 적어주세요. 예) " + groupName + "\n그룹명: ", team)
    print("\n'", forecast, "' 그룹을 선택하셨습니다.")
    return forecast


def pickGroup2(forecast1, forecast2) :
    print("-------------------------------------------------------------------")
    team = [forecast1, forecast2]
    print("\n", team)
    forecast = checkName("\n두 그룹 중에 더 좋아하시는 그룹을 적어주세요. 예) " + forecast1 + "\n그룹명: ", team)
    print("'", forecast, "' 그룹을 선택하셨습니다.")
    return forecast


def checkName(message, group) :
    while 1 :
        forecast = input(message)
        if forecast in group :
            break
        print("※※※※※리스트 내에서 입력해주세요※※※※※")
    return forecast


while menu != 3 :
    print("◈◈◈◈◈◈◈◈◈ 우승시그널에 오신 것을 환영합니다 ◈◈◈◈◈◈◈◈◈\n")
    print("1. (남성 선호)러시아 월드컵 우승 시뮬레이션")
    print("2. (여성 선호)남자 아이돌 그룹 월드컵 우승 시뮬레이션")
    print("3. 종료\n")

    menu = int(input("메뉴 선택: "))

    # 1번 메뉴 선택 시
    if menu == 1 :
        # 러시아 월드컵 우승 시뮬레이션
        groupA_win = forecastVictory(groupA.getGroup(), "A", "러시아")
        groupB_win = forecastVictory(groupB.getGroup(), "B", "스페인")
        groupC_win = forecastVictory(groupC.getGroup(), "C", "프랑스")
        groupD_win = forecastVictory(groupD.getGroup(), "D", "아르헨티나")
        groupE_win = forecastVictory(groupE.getGroup(), "E", "브라질")
        groupF_win = forecastVictory(groupF.getGroup(), "F", "대한민국")
        groupG_win = forecastVictory(groupG.getGroup(), "G", "잉글랜드")
        groupH_win = forecastVictory(groupH.getGroup(), "H", "폴란드")

        print("-------------------------------------------------------------------")
        groupFinal = [groupA_win, groupB_win, groupC_win, groupD_win, groupE_win, groupF_win, groupG_win, groupH_win]
        print("\n다음은 본선에 진출한 8팀 중 월드컵 우승국을 예측 할 차례입니다.")
        print("\n", groupFinal)
        forecast_Final = input("\n월드컵 우승 예측 국가를 적어주세요. 예) 스페인\n예측 국가: ")
        print("\n월드컵 우승국을 발표합니다.")
        print("2018 러시아 월드컵 우승국:", groupFinal[randNum_final])
        groupFinal_win = groupFinal[randNum_final]
        if (groupFinal_win == forecast_Final) :
            forecast_point += 1
            print(groupFinal_win, "예상적중!! 예측하신 국가가 월드컵 우승을 차지했습니다. \n당신은 진정한 축잘알!")
            print("총", forecast_point, "번 예측 성공하셨습니다.")
        else :
            print(forecast_Final, "국가는 월드컵 우승에 실패했습니다..\n축잘알이 되기 위한 길은 쉽지 않습니다. 한 번 더 도전해보세요!")
            print("총", forecast_point, "번 예측 성공하셨습니다.")
        print("-------------------------------------------------------------------")

    # 2번 메뉴 선택 시
    if (menu == 2) :
        print("-------------------------------------------------------------------")
        name = input("\n귀하의 성함을 적어주세요. 예) 이정현\n성함: ")

        # 남자 아이돌 그룹 월드컵 우승 시뮬레이션

        # 네 개의 그룹 중 선택
        forecast_A = pickGroup4(teamA.getGroup(), "방탄소년단")
        forecast_B = pickGroup4(teamB.getGroup(), "비투비")
        forecast_C = pickGroup4(teamC.getGroup(), "하이라이트")
        forecast_D = pickGroup4(teamD.getGroup(), "위너")
        forecast_E = pickGroup4(teamE.getGroup(), "블락비")
        forecast_F = pickGroup4(teamF.getGroup(), "샤이니")
        forecast_G = pickGroup4(teamG.getGroup(), "B1A4")
        forecast_H = pickGroup4(teamH.getGroup(), "JBJ")

        # 두 개의 그룹 중 선택
        forecast_AB = pickGroup2(forecast_A, forecast_B)
        forecast_CD = pickGroup2(forecast_C, forecast_D)
        forecast_EF = pickGroup2(forecast_E, forecast_F)
        forecast_GH = pickGroup2(forecast_G, forecast_H)

        forecast_ABCD = pickGroup2(forecast_AB, forecast_CD)
        forecast_EFGH = pickGroup2(forecast_EF, forecast_GH)
        forecast_ABCDEFGH = pickGroup2(forecast_ABCD, forecast_EFGH)

        print(name, "님께서는 가장 좋아하시는 남자 아이돌 그룹으로 '", forecast_ABCDEFGH, "' 을(를) 뽑으셨습니다.")
        winText = input(
            "\n" + forecast_ABCDEFGH + " 분들께 우승 소감 한 마디 해주세요~ " + "예)" + forecast_ABCDEFGH + " 오빠들! 항상 응원하고 있어요!" + "\n소감: ")
        print("-------------------------------------------------------------------")
        i = 0
        while (i < 30) :
            print(name, "♥", forecast_ABCDEFGH)
            i += 1
        print("-------------------------------------------------------------------")
    if (menu == 3) :
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 메뉴 번호를 선택해주세요.")
        print("-------------------------------------------------------------------")
