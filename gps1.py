#Pairut Dumkuengthanant
#ID: 64856070

#input module
import url
import outpus
#ask user to enter # of destination
def num_dest()->int:
    while True:
        num_loc=input((""))
        try:
            if (int(num_loc) >= 2):
                return int(num_loc)
            else:
                print("error")
        except:
            print("error")
#ask user to enter addresses or location(s)
def dest(num_loc: int)-> 'locations':
    ll=[]
    for i in range(int(num_loc)):
        destination=input("")
        ll.append(destination) 
    return ll
#ask user how many possible (total) outputs user desires
def num_output()->int:
    while True:
        num_loc=input((""))
        try:
            if (int(num_loc) >= 1):
                return int(num_loc)
            else:
                print("error")
        except:
            print("error")
#error function
def Map_error()->None:
    return

def main():
    num=num_dest()
    loc_lst=dest(num)
    noutp=num_output()
    #build the url under the 'try' if failed, then it is possibly
    #an appkey error or other building url erros
    try:
        url1=url.build_url(loc_lst)

    except:
        print('\n','MAPQUEST ERROR')
        Map_error()
    #builds url for elevations and inputing url into json  
    try:
        json=url.get_result(url1)
        lst_latlong=outpus.Latln.latlong(json)
        ele_url=url.get_elevations(lst_latlong)
        json_eleva=url.get_result(ele_url)
    except:
        print('\n','NO ROUTE FOUND')
        Map_error()
        
    #reading the url is usually sucessful even if addresses are incorrect
    #check errors by parcing through the information sent from url
    if (outpus.Distance.output(json)==int(0) and outpus.Time.output(json)==int(0)):
        print('\n', 'NO ROUTE FOUND')
        Map_error()
    #compile list of command inputs then extract list
    #for specific action(s) to be executed
    lst_action=[]
    for i in range(noutp):
        user_in=input("")
        lst_action.append(user_in)    
       
    for in1 in lst_action:
        
        if str(in1)=='STEPS':
            outpus.Directions.output(json)
        
        elif str(in1)=='TOTALDISTANCE':
            distance=outpus.Distance.output(json)
            print('\n','TOTAL DISTANCE:', round(distance),'miles')
       
        elif str(in1)=='TOTALTIME':
            time=outpus.Time.output(json)
            print('\n','TOTAL TIME:', round(time),'minutes')
       
        elif str(in1)=='LATLONG':
            outpus.Latln.output(json)
       
        elif str(in1)=='ELEVATION':
            outpus.Elevations.output(json_eleva)
        
    print('\n','Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
if __name__=='__main__':
    
    main()
