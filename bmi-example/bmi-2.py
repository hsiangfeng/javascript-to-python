import time

color = {
  'OKGREEN': '\033[92m',
  'WARNING': '\033[93m',
  'FAIL': '\033[91m',
  'ENDC': '\033[0m',
}

cm = float(input('請輸入您的身高：'))
kg = float(input('請輸入您的體重：'))

def bmi (kg, cm):
  if kg <= 0:
    return print('體重輸入不正確')
  if cm <= 0:
    return print('身高輸入不正確')

  bmiNum = round((kg / ((cm ** 2) / 100)) * 100, 2)

  if bmiNum < 18.5:
    print(f'你目前的 BMI 是：{bmiNum}介於{color["WARNING"]}過輕{color["ENDC"]}範圍內。')
  elif 18.5 >= bmiNum < 24:
    print(f'你目前的 BMI 是：{bmiNum}介於{color["OKGREEN"]}正常{color["ENDC"]}範圍內。')
  elif 24 >= bmiNum < 27:
    print(f'你目前的 BMI 是：{bmiNum}介於{color["WARNING"]}過重{color["ENDC"]}範圍內。')
  elif 27 >= bmiNum < 30:
    print(f'你目前的 BMI 是：{bmiNum}介於{color["WARNING"]}輕度{color["ENDC"]}範圍內。')
  elif 30 >= bmiNum < 35:
    print(f'你目前的 BMI 是：{bmiNum}介於{color["FAIL"]}中度{color["FAIL"]}範圍內。')
  elif bmiNum >= 35:
    print(f'你目前的 BMI 是：{bmiNum}介於{color["FAIL"]}重度{color["FAIL"]}範圍內。')
  else:
    print('計算錯誤。')

print('Loading', end='')
for i in range(5):
  if i < 4:
    print('.', end='', flush=True)
  else:
    print('.', flush=True)
  time.sleep(1)
bmi(kg, cm)