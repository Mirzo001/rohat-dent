# def datetime_range(start, end, delta):
#     current = start
#     while current < end:
#         yield current
#         current += delta

# dts = [dt.strftime('%H:%M') for dt in 
#        datetime_range(datetime(2022, 9, 1, 6), datetime(2022, 9, 1, 23), 
#        timedelta(hours=1))]


################################

# def list_view(request):
#     appointment, search = _search_posts(request)
#     context = {"appointment": appointment, "search": search}
#     return render(request, "list.html", context)


# def list_search_view(request):
#     appointment, search = _search_posts(request)
#     context = {"appointment": appointment, "search": search}
#     return render(request, "search_results.html", context)


# def _search_posts(request):
#     search = request.GET.get("search")
#     appointment = Appointment.objects.all()
#     if search:
#         appointment = Appointment.objects.filter(doctor=request.user)
#         appointment = appointment.filter(patient__name__icontains=search)


#     return appointment, search or "" 
    
##############################

\
    
    
    
    
    
    # def CreateAppointmentView(request):
#     results=Patient.objects.all()
    
#     if request.method == 'POST':
#         print(request.POST)
#         form = AppointmentCreateForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # Appointment.objects.create(**form.cleaned_data)
#             form.save()
#             return redirect(reverse_lazy('dashboard'))
#     else:
#         form = AppointmentCreateForm()
    
#     return render(request, 'appointment/appointment_new.html', {'form': form, "patients":results})
   
    # success_url = reverse_lazy('dashboard')

# class CreateAppointmentView(View):
#     def get(self, request):
#         create_form = AppointmentCreateForm()
#         patients = Patient.objects.all()
        
#         context = {
#             "form": create_form,
#             "patients": patients
#         }
#         return render(request, "appointment/appointment_new.html", context)
    
#     def post(self, request):
        
#         # print(create_form.instance.patient)
#         create_form = AppointmentCreateForm(data=request.POST)
#         # print(request.POST.get('patient'))
#         create_form.instance.doctor = self.request.user
#         # print(create_form.instance.doctor)
#         # create_form.instance.Patient = create_form.data['patient']
        
#         # create_form.instance.Patient = self.request.POST.get('patient')
        
#         if create_form.is_valid():
#             create_form.save()
#             return redirect('dashboard')
#         else:
#             context = {
#             "form": create_form,
#         }
#         return render(request, "appointment/appointment_new.html", context )
# class CreateAppointmentView(LoginRequiredMixin, CreateView, UserPassesTestMixin):
#     model = Appointment
#     template_name = 'appointment/appointment_new.html'
#     fields = ['patient','date','time','status','qaydlar']
    
#     def form_valid(self, form):
#         form.instance.doctor = self.request.user
#         return super().form_valid(form)
#     def test_func(self):
#         return self.request.user
    

    
    # def post(self, request):
    #     form = AppointmentCreateForm(data=request.POST)
    #     form.save()
    #     return redirect(reverse_lazy('dashboard')) 
 
 
 
 
 # shu yerda statusga qarab increment bo'ladi
# class EditAppointmentView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
#     model = Appointment
#     fields = ['patient','date','time','status','qaydlar']
#     template_name = 'appointment/appointment_edit.html'

#     def test_func(self):
#         return self.request.user.is_superuser   
     
    
#     success_url = reverse_lazy('dashboard')
 
    
# class EditAppointmentView(LoginRequiredMixin, View):
#     def get(self, request, pk):
#         appointment = Appointment.objects.get(id=pk)
#         print(appointment)
#         appointment_form = AppointmentEditForm(instance=appointment)
#         if appointment.status == "Completed":
#         #     appointment_form.fields['status'].disabled=True
#             appointment_form.fields['status'].disabled = True
            
#             # status = appointment_form.status(disabled = True)
#         return render(request, "appointment/appointment_edit.html", {"appointment": appointment,"appointment_form": appointment_form})

#     def post(self, request, pk):
#         appointment = Appointment.objects.get(id=pk)
#         appointment_form = AppointmentEditForm(instance=appointment, data=request.POST)
    
#         # appointment_form.save()
        
#         if appointment_form.is_valid():
#             appointment_form.save()
            
#
# print(request.POST)
#         return render(request, "appointment/appointment_edit.html", {"appointment": appointment,"appointment_form": appointment_form})

# def autosuggest(request):
#     # print(request.GET)
#     query_original = request.GET.get('term')
#     queryset = Appointment.objects.filter(patient__name__icontains=query_original)
#     # print(queryset)
#     mylist = []
#     mylist += [x.patient.name for x in queryset] 
#     return JsonResponse(mylist, safe=False)  

# def DoctorsJsonList(request):
#     # data = list(Appointment.objects.values())
#     # return JsonResponse({'data': data})
#     query_original = request.GET.get('term')
#     queryset = Appointment.objects.filter(patient__name__icontains=query_original)
#     # print(queryset)
#     mylist = []
#     mylist += [x.patient.name for x in queryset] 
#     return JsonResponse(mylist, safe=False)  

# def createapp(request):
    
#     # appointment = Appointment.objects.all()
#         # appointment_form = AppointmentEditForm(instance=appointment)
#         # json = JsonResponse({'data': Appointment.objects.get(id=pk)})
#         # return render(request, "appointment/appointment_edit.html", {"appointment": appointment})

#     patient = request.POST('patient')
#     date = request.POST('date')
#     time = request.POST('time')
#     status = request.POST('status')
#     qaydlar = request.POST('qaydlar')
#     app = Appointment(patient=patient, date=date, time=time,status=status, qaydlar=qaydlar)
#     app.save()
#     return render(request, 'appointment/app_new.html')