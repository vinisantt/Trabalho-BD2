# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import ClienteForm
import pyodbc 



def home(request):
    form = ClienteForm
    if request.method == 'POST':
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-BM3KC8C\SQLEXPRESS;' #servidor do banco
                      'Database=Teste;' #tabela
                      'Trusted_Connection=yes;')
            
            cursor = conn.cursor()
            cursor.execute(" exec selecionarDados ")

            result_set = cursor.fetchall()

            print(result_set)
                
        finally:
            cursor.close()
            
    return render(request,"sistema_app/index/index.html",{'form':form})


