from .models import Project, Report
from .serializers import ProjectSerializer, ReportSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import datetime
from dateutil import parser



today = datetime.datetime.today()
start_date = datetime.datetime(today.year, today.month, 1)

def lom(year, month, day):
    d = datetime.date(year + int(month/12), month%12+1, 1)-datetime.timedelta(days=1)
    return d

end_date = lom(today.year, today.month,today.day)



class projects(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
    
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)


class addReport(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ReportSerializer(data = request.data)
        if serializer.is_valid():

            date = parser.parse(serializer.data['date'])
            

            last_date = Report.objects.order_by("-date").filter(user=request.user.id)

            def is_reported(last_date, date):

                y,w,d = date.isocalendar()

                rep = []
                for i in last_date:

                    last_date = datetime.datetime(i.date)

                    year, week_num, day_of_week = last_date.isocalendar()

                    if week_num != w:
                        rep.append(0)
                    else:
                        rep.append(1)

                if 1 in rep:
                    return True
                else:
                    return False
            
            if is_reported(last_date, date) is False:

                serializer.save()

        return Response(serializer.data)

class reports(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        reports = Report.objects.order_by("-date").filter(date__range=[start_date, end_date])
        serializer = ReportSerializer(reports, many=True)

        return Response(serializer.data)



