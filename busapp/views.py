from django.shortcuts import render
import datetime,pyttsx3

# Create your views here.
def home(request):
    #return HttpResponse("this is homepage")
    return render(request,'home.html')

def about(request):
    return render(request,'aboutme.html')

def contact(request):
    return render(request,'contact.html')

def feedback(request):
    return render(request,'feedback.html')

def search(request):
    if request.method=="POST":
        #timing list for buses  according to place-dest
        #for kore village
        s_kore=["05:30","06:30","07:00","08:00","09:30","10:30","11:15","12:30","13:45","14:45","15:10","16:15","17:00","17:45","18:30","20:00","21:00"]
        kore_s=["04:40","05:35","06:20","06:50","07:50","08:45","09:35","11:10","12:00","14:20","15:05","16:05","16:50","17:35","19:05"]
        #for dativare village
        dat_s=["03:00","04:30","05:05","06:10","07:15","08:00","08:30","13:00","14:20","16:10","17:45"]
        s_dat=["05:30","06:30","07:10","07:30","12:20","13:45","15:30","17:00","18:30","20:00"]
        #for khardi village
        s_khar=["04:30","07:00","08:00","08:45","09:20","10:30","11:00","12:40","13:45","15:30","16:10","17:00","18:30","20:00"]
        khar_s=["04:30","05:30","06:05","07:50","08:50","09:30","10:30","11:15","11:30","13:20","14:30","16:10","17:00"]
        #for palghar 
        s_pal=["07:30"]
        pal_s=["08:00"]
        #

        hrfinal=[] #hours final list
        F_hrlist=[] #final hrs list
        mnfinal=[]  #final minute list
        Av_hrlist=[] #available buses hrs
        Av_mnlist=[] #available buses mnt
        FAv_hrlist=[] #final available buses hr
        output=[]     #output buses list 1-12 hrs
        Av_output=[]  #output for AVAILABLE buses list 1-12 hrs

        #taking input value from html page
        placename=str(request.POST.get('place')).lower()
        destinationname=str(request.POST.get('dstn')).lower()
        
        if placename==destinationname:
            t="SELECT PROPER PLACE AND DESTINATION !!"
            p=0

        elif (placename!='saphale' and destinationname !='saphale'):
            p=0
            t="SELECT PROPER CHOICE"


        else:
            p=1
            #making a targetlist
            if placename=="saphale":
                if destinationname=="kore":
                    targetlist=s_kore
                elif destinationname=="dativare":
                    targetlist=s_dat
                elif destinationname=="khardi":
                    targetlist=s_khar
                elif destinationname=="palghar":
                    targetlist=s_pal
                
                    
            if destinationname=="saphale":
                if placename=="kore":
                    targetlist=kore_s
                elif placename=="dativare":
                    targetlist=dat_s
                elif placename=="khardi":
                    targetlist=khar_s
                elif placename=="palghar":
                    targetlist=pal_s
            
                        
            for item in targetlist:
                temp=item
                hr=int(temp[0:2])
                mn=int(temp[3:])
                hrfinal.append(hr) #making hour list
                mnfinal.append(mn) #making minute list
                #calculating total minute from list
                total_min1=hr*60 + mn
                #getting total minute from realtime list
                total_min2=datetime.datetime.now().hour*60 + datetime.datetime.now().minute
                if total_min1 >= total_min2:
                    Av_hrlist.append(hr)
                    Av_mnlist.append(mn) #available bus mns for bus

                    #available bus hrs for bus & convrting as 1 to 12
                    if hr > 12 :
                        FAv_hrlist.append(hr-12) 
                    else:
                        FAv_hrlist.append(hr)

                #converting a hrslist into [1 to 12] form
                if hr>12:
                    F_hrlist.append(hr-12)
                else:
                    F_hrlist.append(hr)

            for i in range (len(hrfinal)):
                if (hrfinal[i]>=12):
                    txt=str(F_hrlist[i])+":"+str(mnfinal[i])+" PM"
                    output.append(txt)
                else:
                    txt=str(F_hrlist[i])+":"+str(mnfinal[i])+" AM"
                    output.append(txt)

            for i in range (len(Av_hrlist)):
                if (Av_hrlist[i]>=12):
                    txt=str(FAv_hrlist[i])+":"+str(Av_mnlist[i])+" PM"
                    Av_output.append(txt)
                else:
                    txt=str(FAv_hrlist[i])+":"+str(Av_mnlist[i])+" AM"
                    Av_output.append(txt)



        data={
            'out_list':output,
            'Av_outlist':Av_output,
            'flag':p,
            'from':placename,
            'to': destinationname
        }
    
        if Av_output==[] :
            pass
        else:
            eng=pyttsx3.init('sapi5')
            h=str(FAv_hrlist[0])
            m=str(Av_mnlist[0])
            Anc="your bus is at",h,m
            eng.say(Anc)
            eng.runAndWait() 
        

        return render(request,'home.html',data)
    
    return render(request,'home.html')

    