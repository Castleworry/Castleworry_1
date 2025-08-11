import random
from typing import Literal
from tools import GuessGesture
import tools


def main():
    gestures = ["剪刀","石頭","布"]
    record = {"勝":0,"敗":0,"平":0}
    print("\n=======猜拳遊戲=======\n")

    while True:
        player_gesture = GuessGesture.input_gesture()
        if player_gesture == "q":
            print(f"遊戲結束,你的成績是:{tools.GuessGesture.record['勝']}勝,{record['敗']}敗,{record['平']}平")
            break

        computer_gesture = random.randint(0,2)
        print(f"你出了{gestures[player_gesture]}")
        print(f"電腦出了{gestures[computer_gesture]}")
        GuessGesture.compare(player_gesture,computer_gesture,record)
        print(f"目前成績:{record['勝']}勝,{record['敗']}敗,{record['平']}平\n")
        
            

if __name__ == "__main__":
    main()