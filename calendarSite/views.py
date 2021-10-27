from django.shortcuts import render
from calendarSite.forms import addDataForm
from calendarSite.forms import indexForm
from calendarSite.forms import searchForm
from calendarSite.forms import subjectForm
from calendarSite.forms import userForm
from calendarSite.models import Calendar

# Create your views here.
# Create your views here.


def index(request):
    return render(request, 'index.html')

def search(request):
   if request.POST:
      form = searchForm(request.POST or None)
      subject = request.POST.getlist("subject")
      user=form['user'].data or ''
      print(user)
      print(subject)

   # ã¡ã?ã»ã¼ã¸æ?å ±ãåå¾ããªã?å ´åã?¯ç©ºæ?å­ãå¥ã?
   """
   if  user != '':
        # ã¡ã?ã»ã¼ã¸ã®å?å®¹ãDBã«ç»é²
        userModel = User(user_id=user,user_subject=subject)
        userModel.save()
   
   
    UserList = User.objects.all()

    return render(request, 'search.html',{
        "UserList": UserList
    })

    dbData = {
        "id": 123,
        "name": "name",
        "form": form,
        "UserList" : UserList,
    }"""
   return render(request, 'search.html')

def addData(request):
   date=0
   user='ããã?'
   subject='ãã?¼ã?ãè¶'
   title='ä¼è¤å?'


   #ãã©ã¼ã?ãæã£ã¦æ¥ã?
   form=addDataForm(request.POST or None)
   #ãã©ã¼ã?ããã?ã¼ã¿ãåå¾?
   date=form['date'].data or ''
   user=form['user'].data or ''
   subject=form['subject'].data or ''
   title=form['title'].data or ''

   print(str(date))
   print(str(user))
   print(str(subject))
   print(str(title))

   #ã?ã¼ã¿ãã?¼ã¹ã«ä¿å­?
   if date!=''and user!='' and subject!='' and title!='':
      calendarModel=Calendar(date=date, user=user, title=title, subject=subject)
      calendarModel.save()

   caleList = Calendar.objects.all()

   print(caleList)

   dbData={
         "caleList":caleList,
         "date":date,
         "title":title
   }
   if date!=''and user!='' and subject!='' and title!='':
      return render(request,'user.html',dbData)
   return render(request, 'addData.html',dbData)

def user(request):
   caleList = Calendar.objects.all()

   print(caleList)
   user="user"
   dbData={
         "caleList":caleList,
         "user":user,
   }
   return render(request,'user.html',dbData)


def subject(request):
   return render(request, 'subject.html')

