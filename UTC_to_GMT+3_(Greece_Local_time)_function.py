def earthquakedateconverter(date):
    splitted_string=date.split()

    day_number=splitted_string[2]
    month=splitted_string[1]

    time=splitted_string[3]
    hours=time.split(':')[0]
    mins=time.split(':')[1]
    secs=time.split(':')[2]
    day=splitted_string[0]

    hours=int(hours) #hours is string till now
    if hours>=21:

        hours=hours+3-24     #fix hour
        hours=str(hours)
        hours='0'+hours
        timesequence=[hours,mins,secs]
        splitted_string[3]=(':'.join(timesequence))

        if day=='Mon': #nameday fix - add one
            splitted_string[0]='Tue'
        elif day=='Tue':
            splitted_string[0]='Wed'
        elif day=='Wed':
            splitted_string[0]='Thu'
        elif day=='Thu':
            splitted_string[0]='Fri'
        elif day=='Fri':
            splitted_string[0]='Sat'
        elif day=='Sat':
            splitted_string[0]='Sun'
        elif day=='Sun':
            splitted_string[0]='Mon'

        #day number fix
        day_number = int(day_number)+1
        day_number=str(day_number)

        #month number fix
        if month =='Jan':
            if (int(day_number)>28):
                month = 'Feb'
                day_number='01'

        if month =='Feb':
            if (int(day_number)>28):
                month = 'Mar'
                day_number='01'

        if month =='Mar':
            if (int(day_number)>31):
                month = 'Apr'
                day_number='01'

        if month =='Apr':
            if (int(day_number)>30):
                month = 'May'
                day_number='01'

        if month == 'May':
            if (int(day_number) > 31):
                month = 'Jun'
                day_number = '01'

        if month =='Jun':
            if (int(day_number)>30):
                month = 'Jul'
                day_number='01'

        if month =='Jul':
            if (int(day_number)>31):
                month = 'Aug'
                day_number='01'

        if month =='Aug':
            if (int(day_number)>31):
                month = 'Sept'
                day_number='01'

        if month =='Sept':
            if (int(day_number)>30):
                month = 'Oct'
                day_number='01'

        if month =='Oct':
            if (int(day_number)>31):
                month = 'Nov'
                day_number='01'

        if month =='Nov':
            if (int(day_number)>30):
                month = 'Dec'
                day_number='01'

        if month =='Dec':
            if (int(day_number)>31):
                month = 'Jan'
                day_number='01'


        splitted_string[2] = day_number
        splitted_string[1] = month

    else: #if time <21:00
        a=str(int(hours) + 3)
        if (int(hours) + 3)<10:
            a='0'+str(int(hours) + 3)
        timesequence = [a, mins, secs]
        splitted_string[3] = (':'.join(timesequence))

    reproduced_date_sequence=[splitted_string[0],splitted_string[1],splitted_string[2],splitted_string[3],splitted_string[4],splitted_string[5]]
    reproduced_date = (' '.join(reproduced_date_sequence))
    return (reproduced_date)


