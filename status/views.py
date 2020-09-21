from datetime import date
import calendar
import pymsteams

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
# from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from .forms import StatusForm
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import Tasks

User = get_user_model()


class CreateStatus(LoginRequiredMixin, CreateView):
    model = Tasks
    # fields = ('detail','starting_date','percentange','comment')
    template_name = 'status/tasks_form.html'
    form_class = StatusForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        firstname = str(self.request.user.first_name) + ' ' +str(self.request.user.last_name) 
        task = str(self.object.detail)
        date = str(self.object.starting_date)
        percent = str(self.object.percentange)
        comment = str(self.object.comment) + '</pre>'
        msg = "<pre> Task Name: " + task + '<br> Start Date :' + date +'<br> Percentage : ' + percent + '%' + '<br> Comment:' + comment
        team = pymsteams.connectorcard(settings.OUTLOOK_WEBHOOK)
        team.title(firstname)
        team.text(msg)
        team.send() 																							  			
        return super().form_valid(form)


class StatusDetailView(LoginRequiredMixin, DetailView):
    model = Tasks


class StatusListView(LoginRequiredMixin, ListView):
    model = Tasks

    def get_queryset(self):
        return Tasks.objects.filter(user__username__iexact=self.request.user).order_by('-updated_at')


class UpdateStatusView(LoginRequiredMixin, UpdateView):
    model = Tasks
    form_class = StatusForm
    template_name = 'status/tasks_form.html'


class DeleteStatusView(LoginRequiredMixin, DeleteView):
    model = Tasks
    success_url = reverse_lazy('status:list')


def CustomSerarch(request):
    query = dict(request.GET)
    if query:
        fromdate = (query.get('q'))[0]
        todate = query.get('q')[1]
        qs = Tasks.objects.filter(Q(created_at__gte=fromdate) &
                                  Q(created_at__lte=todate) & (Q(user__username__iexact=request.user) or Q(
            user__id__iexact=pk))).order_by('-updated_at')
        return render(request, 'status/tasks_list.html', {'object_list': qs})
    return render(request, 'status/tasks_list.html', {})


class adminSearchTask(LoginRequiredMixin, ListView):
    model = User
    template_name = 'status/user_list.html'


def adminDetailTask(request, pk):
    qs = Tasks.objects.filter(user__id__iexact=pk)
    return render(request, 'status/tasks_list.html', {'object_list': qs})


def emailTask(request):
    query = dict(request.GET)
    if query:
        fromdate = (query.get('q'))[0]
        todate = query.get('q')[1]
        qs = Tasks.objects.filter(Q(created_at__gte=fromdate) &
                                  Q(created_at__lte=todate) & (Q(user__username__iexact=request.user))).order_by(
            'created_at')
        data = ''
        # for i in list(qs.values()):
        #     print(calendar.day_name[i['created_at'].weekday()])

        try:
            day = None
            for i in list(qs.values()):
                if calendar.day_name[i['created_at'].weekday()] != day:
                    data += '\n' + 'Date:' + i['created_at'].strftime("%d-%m-%Y") + ' : ' + str(
                        calendar.day_name[i['created_at'].weekday()] + '\n')
                    day = calendar.day_name[i['created_at'].weekday()]
                data += ('Task Name:' + i['detail'] + '\n' +
                         'Started Date:' + i['starting_date'].strftime("%d-%m-%Y") + '\n' +
                         'Percent:' + str(i['percentange']) + "%" + '\n \n')
            print(data)
            task = "Task from : " + list(qs.values())[0]['created_at'].strftime("%d-%m-%Y") + " to : " + list(qs.values())[-1]['created_at'].strftime("%d-%m-%Y")
            admin = 'admin@mail.com'
            send_mail(subject=task,
                      message=data,
                      from_email=request.user.email,
                      recipient_list=[admin, request.user.email])
        except IndexError:
            data = "No record Found"
            return render(request, 'status/email_task.html', {'message': "No record found to email"})
        return render(request, 'status/email_task.html', {
            'message': "The mail has been send to " + request.user.email + ' and ' + admin})
    return render(request, 'status/email_task.html', {})
