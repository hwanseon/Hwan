# 윳놏이 과제 김환선
import random

sticks = []
heung_total = 0
nol_total = 0


while nol_total < 20 or heung_total < 20 :
    while True :
        for _ in range(4) :
            sticks.append(random.randint(0, 1))

        cnt = sticks.count(1)
        if cnt == 0 :
             jumsu = "윷"
             score = 4
        elif cnt == 1 :
             jumsu = "걸"
             score = 3
        elif cnt == 2 :
             jumsu = "개"
             score = 2
        elif cnt == 3 :
             jumsu = "도"
             score = 1
        else :
             jumsu = "모"
             score = 5

        heung_total += score
        print(f"흥부 {sticks} : {jumsu} ({score}점) / (총 {heung_total}점) --->")
        sticks.clear()

        if (jumsu == "윷" or jumsu == "모") and heung_total < 20 :
             continue
        else :
             break
        
    if heung_total >= 20 : 
         print(f"흥부 승리 => 흥부 : {heung_total} , 놀부 : {nol_total}")
         
         break 

    while True :
        for _ in range(4) :
            sticks.append(random.randint(0, 1))

        cnt = sticks.count(1)
        if cnt == 0 :
             jumsu = "윷"
             score = 4
        elif cnt == 1 :
             jumsu = "걸"
             score = 3
        elif cnt == 2 :
             jumsu = "개"
             score = 2
        elif cnt == 3 :
             jumsu = "도"
             score = 1
        else :
             jumsu = "모"
             score = 5

        nol_total += score
        print(f"\t\t\t\t\t<--- 놀부 {sticks} : {jumsu} ({score}점) / (총 {nol_total}점)")
        sticks.clear()

        if (jumsu == "윷" or jumsu == "모") and nol_total < 20 :
             continue
        else :
             break         
    
    if nol_total >= 20 :
         print(f"놀부 승리 => 놀부 : {nol_total}, 흥부 : {heung_total}")
         
         break

    # elif nol_total >= 20 :
    #      print(f"놀부 승리 => 놀부 : {nol_total}, 흥부 : {heung_total}")
    # else :
    #      pass

         
    # for i in range(1000) :
    #     i = random.randint(0, 1)
    #     sticks.append(i)
    #     i = random.randint(0, 1)
    #     sticks.append(i)
    #     i = random.randint(0, 1)
    #     sticks.append(i) 
    #     i = random.randint(0, 1)
    #     sticks.append(i)  
    #     if sticks.count(1) == 0 :
    #         jumsu = "윷"
    #         total = total + 4
    #         socre = "4점"
    #     elif sticks.count(1) == 1 :
    #         jumsu = "걸"
    #         total = total + 3
    #         socre = "3점"

    #     elif sticks.count(1) == 2 :
    #         jumsu = "개"
    #         total = total + 2
    #         socre = "2점"

    #     elif sticks.count(1) == 3 :
    #         jumsu = "도"
    #         total = total + 1
    #         socre = "1점"

    #     else :
    #         jumsu = "모"
    #         total = total + 5
    #         socre = "5점"

    #     while jumsu == "윷" or jumsu == "모" :                    
    #                 i = random.randint(0, 1)
    #                 sticks.append(i)
    #                 i = random.randint(0, 1)
    #                 sticks.append(i)
    #                 i = random.randint(0, 1)
    #                 sticks.append(i) 
    #                 i = random.randint(0, 1)
    #                 sticks.append(i) 
                
    #                 if jumsu != "윳" or jumsu != "모" :
    #                     break

        

        