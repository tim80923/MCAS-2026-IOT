import RPi.GPIO as GPIO
import time

# 設定腳位 
LED_PIN = 11
BUZ_PIN = 13
FREQ = 523 # 蜂鳴器頻率

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZ_PIN, GPIO.OUT)

voice = GPIO.PWM(BUZ_PIN, FREQ)

def sos_signal(duration):
    """控制 LED 亮起與蜂鳴器發聲"""
    GPIO.output(LED_PIN, True)
    voice.start(50)  # 啟動 PWM 讓蜂鳴器響起
    time.sleep(duration)
    
    """控制 LED 熄滅與蜂鳴器停止"""
    GPIO.output(LED_PIN, False)
    voice.stop()
    time.sleep(0.2)  # 每個訊號間的短暫間隔

try:
    while True:
        # S: 3 短 (0.2秒)
        for _ in range(3):
            sos_signal(0.2)
        time.sleep(0.4) # 字母間的間隔
        
        # O: 3 長 (0.6秒)
        for _ in range(3):
            sos_signal(0.6)
        time.sleep(0.4)
        
        # S: 3 短 (0.2秒)
        for _ in range(3):
            sos_signal(0.2)
            
        time.sleep(2) # 發送完一次 SOS 休息 2 秒再重複

except KeyboardInterrupt:
    pass
finally:
    voice.stop()
    del voice  # 刪除PWM物件，避免結束程式跳出例外錯誤
    GPIO.cleanup()