from time import sleep, localtime
import tm1637

# 設定 CLK 與 DIO 腳位 (BCM)
CLK = 23  
DIO = 24

tm = tm1637.TM1637(clk=CLK, dio=DIO)
tm.brightness(1)

show_colon = False

try:
    while True:
        # 取得目前本機時間
        t = localtime()
        # 每次迴圈將冒號狀態反轉 (閃爍效果)
        show_colon = not show_colon
        # 將小時、分鐘與冒號狀態寫入顯示器
        tm.numbers(t.tm_hour, t.tm_min, show_colon)
        # 同步於終端顯示
        print(f"目前時間: {t.tm_hour}:{t.tm_min}, 冒號: {show_colon}")
        sleep(1)

except KeyboardInterrupt:
    # 程式中斷時關閉所有 LED (熄滅顯示器)
    tm.write([0, 0, 0, 0])