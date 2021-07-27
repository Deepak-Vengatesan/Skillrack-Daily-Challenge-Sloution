def Time(seconds):
    hh = seconds//3600
    mm = seconds%3600//60 
    ss = seconds%3600%60
    if hh>12 :
        hh = hh%12 
    if hh == 0:
        hh = 12 
    print(f"{str(hh).zfill(2)}:{str(mm).zfill(2)}:{str(ss).zfill(2)}")

hh,mm,ss = map(int,input().split(":")) 
k, x = map(int,input().split())
timeInseconds = hh*3600 + mm*60 + ss 
extraTime = x 
Time(timeInseconds+extraTime) # clock 1 
extraTime = x//k 
Time(timeInseconds+extraTime)  # clock 2  
