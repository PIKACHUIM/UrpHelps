def urps_chan(data):
    retu = 0
    if data < 60:
        retu = 0.0
    elif 60 <= data < 61:
        retu = 1.0
    elif 61 <= data < 63:
        retu = 1.3
    elif 63 <= data < 66:
        retu = 1.7
    elif 66 <= data < 70:
        retu = 2.0
    elif 70 <= data < 73:
        retu = 2.3
    elif 73 <= data < 76:
        retu = 2.7
    elif 76 <= data < 80:
        retu = 3.0
    elif 80 <= data < 85:
        retu = 3.3
    elif 85 <= data < 90:
        retu = 3.7
    elif data>=90:
        retu = 4.0
    return retu