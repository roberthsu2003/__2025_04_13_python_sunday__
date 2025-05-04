def main():
    height:int = int(input("請輸入身高公分"))
    weight:int = int(input("請輸入體重公斤"))
    BMI = round(weight/pow(height/100,2),1)

    print(f"身高:{height}""cm")
    print(f"體重:{weight}""kg")
    print(f"BMI:{BMI}")

    if BMI < 18.5:
        status = "體重過輕"
    elif BMI < 24:
        status = "正常"
    elif BMI < 27:
        status = "過重"
    elif BMI < 30:
        status = "輕度肥胖"
    elif BMI <35:
        status = "中度肥胖"
    else:
        status = "重度肥胖"
    print(f"狀態:{status}")

if __name__ == '__main__':
    main()