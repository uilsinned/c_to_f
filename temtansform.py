#攝氏('C) 轉換成華氏('F)
#讓使用者輸入攝氏溫度
#然後印出華氏溫度
temC = input('請輸入攝氏溫度=')
temC = float(temC)
temF = temC * 9 / 5 + 32
print('華氏溫度為:', temF)