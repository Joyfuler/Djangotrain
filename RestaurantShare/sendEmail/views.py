# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from shareRes.models import *
import smtplib
from email.mime.text import MIMEText #태그가 포함된 메일 사용시
from email.mime.multipart import MIMEMultipart #객체 / 파일등 사용시
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

def sendEmail(request):
    checked_res_list = request.POST.getlist('checks') #checkbox에서 여러 개 요소를 가져올 경우 list로 받아옴
    inputReceiver = request.POST['inputReceiver'] # 수신자 이메일. 여러개일 경우 split으로 쪼개 리스트에 담는다.
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']
    
    restaurants = []
    for checked_list in checked_res_list:
        restaurants.append(Restaurant.objects.get(id = checked_list))
    content = {
        'inputContent': inputContent,
        'restaurants' : restaurants
    }    
    
    msg_html = render_to_string('sendEmail/email_format.html', content)
    msg = EmailMessage(subject = inputTitle, body = msg_html,
                       from_email = "triojang2@gmail.com",
                       bcc = inputReceiver.split(','))
    
    msg.content_subtype = 'html'
    msg.send()    
    return HttpResponseRedirect(reverse('index')) 
    
    # mail_html = "<html><body>"
    # mail_html += "<h1> 맛집 공유 </h1>"
    # mail_html += "<p>" + inputContent + "<br>"
    # mail_html += "유저분이 공유한 맛집은 아래와 같습니다. </p>"     
    # for checkedList_id in checked_res_list:
    #     restaurant = Restaurant.objects.get(id = checkedList_id)
    #     mail_html += "<h2>" + restaurant.restaurant_name + "</h3>"
    #     mail_html += "<h4> *관련 링크</h4>" + "<p>" + restaurant.restaurant_link + "</p><br>"
    #     mail_html += "<h4> *상세 내용</h4>" + "<p>" + restaurant.restaurant_content + "</p><br>"
    #     mail_html += "<h4> *관련 키워드</h4>" + "<p>" + restaurant.restaurant_keyword + "</p><br>"
    #     mail_html += "<br>"
    
    # mail_html += "</body></html>"
    
    # # smtp using
    # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # server.login("triojang2@gmail.com", "nxsh ofga ffdf lqyd")
    # msg = MIMEMultipart('alternative')    
    # msg['Subject'] = inputTitle
    # msg['From'] = "triojang2@gmail.com"
    # msg['To'] = inputReceiver
    # mail_html = MIMEText(mail_html, 'html') #mail_html에 입력한 값을 실제 html 코드로 변환
    # msg.attach(mail_html)
    # print(msg['To'], type(msg['To']))
    # server.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
    # server.quit()    
    
    #print(checked_res_list, ", ", inputReceiver, ", ", inputTitle, ", ", inputContent)
    #return HttpResponseRedirect(reverse('index'))