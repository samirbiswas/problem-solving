def timeConversion(s):
    if s[0:2] == "12" and s[8:10] == "AM":
        return "00" + s[2:8]
    elif s[8:10] == "AM":
        return s[0:8]
    elif s[0:2] == "12" and s[8:10]=="PM":
        return s[0:8]
    else:
        return str(int(s[0:2]) + 12) + s[2:8]


result = timeConversion("01:10:00PM")
print(result)