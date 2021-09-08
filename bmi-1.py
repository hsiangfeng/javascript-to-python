def bmi (kg, cm):
  if kg <= 0:
    return print('體重輸入不正確')
  if cm <= 0:
    return print('身高輸入不正確')

  bmiNum = round((kg / ((cm ** 2) / 100)) * 100, 2)

  if bmiNum < 18.5:
    print(f'你目前的 BMI 是：{bmiNum}，介於過輕範圍內。')
  elif 18.5 >= bmiNum < 24:
    print(f'你目前的 BMI 是：{bmiNum}，介於正常範圍內。')
  elif 24 >= bmiNum < 27:
    print(f'你目前的 BMI 是：{bmiNum}，介於過重範圍內。')
  elif 27 >= bmiNum < 30:
    print(f'你目前的 BMI 是：{bmiNum}，介於輕度範圍內。')
  elif 30 >= bmiNum < 35:
    print(f'你目前的 BMI 是：{bmiNum}，介於中度範圍內。')
  elif bmiNum >= 35:
    print(f'你目前的 BMI 是：{bmiNum}，介於中度範圍內。')
  else:
    print('計算錯誤。')

bmi(68, 175) # 你目前的 BMI 是： 22.2 介於過重範圍內。
bmi(95, 185) # 你目前的 BMI 是： 27.76 介於中度範圍內。
