#Pairut Dumkuengthanant
#ID: 64856070


#Module of Classes

#retrieves total distance
class Distance():
    def output(data)->'int(distance)':
        layer1=data['route']
        dist=layer1['distance']
        if dist==int(0):
            return 0
        else:
            return dist

#retrieves total time          
class Time():
    def output(data)->'int(time)':
        layer1=data['route']

        time1=layer1['time']
        time=(int(time1)/60)
        if time==int(0):
            return 0
        else:
            return time
      
        
#retrieves latitude and longitude        
class Latln():
    def output(data)->None:
        layer1=data['route']
        layer2=layer1['locations']
        print('\n','LATLONGS')
        for i in layer2:
    
            latd=i['latLng']['lat']
            lngtd=i['latLng']['lng']
            
            if latd>0 and lngtd>0:
                print('%.2f'%float(latd)+'N',' ','%.2f'%float(lngtd)+'E')
            elif latd<0 and lngtd>0:
                print('%.2f'%float(abs(latd))+'S',' ','%.2f'%float(lngtd)+'E')
            elif latd>0 and lngtd<0:
                print('%.2f'%float(latd)+'N',' ','%.2f'%float(abs(lngtd))+'W')
            elif latd<0 and lngtd<0:
                print('%.2f'%float(abs(latd))+'S',' ','%.2f'%float(abs(lngtd))+'W')

    #returns list of latitude and longitude
    #for building url for elevation
    def latlong(data)->'[lat,long]':
        layer1=data['route']
        layer2=layer1['locations']
        ll=[]
        for i in layer2:
            latd=i['latLng']['lat']
            lngtd=i['latLng']['lng']
            ll.append(latd)
            ll.append(lngtd)
        return ll
#retrieves directions            
class Directions():
    def output(data)->None:
        layer=data['route']['legs']
        print('\n','DIRECTIONS')
        for i in layer:
            b=i['maneuvers']
            for k in b:
                dirc=k['narrative']
                print(dirc)
#retrieves elevations   
class Elevations:
    def output(data)->None:
        layer=data['elevationProfile']
        print('\n','ELEVATIONS')
        if 'elevationProfile' not in data:
            print('error')
        else:
            for i in layer:
                eleva=int(i['height'])*3.2808
                print(round(eleva))
        
   
    
