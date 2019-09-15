# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import ClienteForm
import pyodbc 



def home(request):
    
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-BM3KC8C\SQLEXPRESS;' #servidor do banco
                      'Database=Teste;' #tabela
                      'Trusted_Connection=yes;')
    form = ClienteForm
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        try:
            
            
            cursor = conn.cursor()
            if form.is_valid:
                
                nome =  form.data['nome']

                cpf = form.data['cpf']
                cidade = form.data['cidade']
                cursor.execute(f'exec inserirDados "{nome}","{cpf}","{cidade}" ')
                cursor.commit()

                #result_set = cursor.fetchall()

                
        finally:
            cursor.close()
            
    return render(request,"sistema_app/index/index.html",{'form':form})


