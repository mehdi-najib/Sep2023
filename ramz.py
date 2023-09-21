def jam_argham(ramz_digit):
    sum_digit=0
    for k in ramz_digit:
        sum_digit +=ramz_digit[k]
    return sum_digit

def ramzIsok(ramz_digit):
     if ramz_digit['panj']+ramz_digit['se']==14 and \
         ramz_digit['yek']==ramz_digit['do']*2-1 and \
         ramz_digit['char']==ramz_digit['do']+1 and \
         ramz_digit['do']+ramz_digit['se']==10 :
            if jam_argham(ramz_digit)==30:
                return True




for ramz in range (0, 100000):
    this_ramz=str(ramz).zfill(5)


    ramz_digit={}
    ramz_digit['yek']=int(this_ramz[0])
    ramz_digit['do'] =int(this_ramz[1])
    ramz_digit['se'] =int(this_ramz[2])
    ramz_digit['char'] =int(this_ramz[3])
    ramz_digit['panj'] =int(this_ramz[4])

    if ramzIsok(ramz_digit):
        print (ramz_digit)
