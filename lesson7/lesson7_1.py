def get_status(bmi:float)->str:
    if bmi < 18.5:
        status = "體重過輕"
    elif bmi < 24:
        status = "正常"
    elif bmi < 27:
        status = "過重"
    elif bmi < 30:
        status = "輕度肥胖"
    elif bmi <35:
        status = "中度肥胖"
    else:
        status = "重度肥胖"
    
    return status

def get_bmi(w:int, h:int)->float:
    return round(w/pow(h/100,2),1)

def main():
    height:int = int(input("請輸入身高公分"))
    weight:int = int(input("請輸入體重公斤"))
    BMI:float = get_bmi(weight,height)

    print(f"身高:{height}""cm")
    print(f"體重:{weight}""kg")
    print(f"BMI:{BMI}")
    status:str = get_status(BMI)   
    print(f"狀態為:{status}")

if __name__ == '__main__':
    main()