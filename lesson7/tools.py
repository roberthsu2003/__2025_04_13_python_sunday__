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