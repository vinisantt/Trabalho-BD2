# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .forms import ClienteForm,DeleteClienteForm
import pyodbc 



def home(request):

    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-BM3KC8C\SQLEXPRESS;' #servidor do banco
                      'Database=Teste;' #tabela
                      'Trusted_Connection=yes;')
    form = ClienteForm
    form2 = DeleteClienteForm
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        
        if "inserir" in request.POST:

            try:
                cursor = conn.cursor()
                if form.is_valid:
                    
                    nome =  form.data['nome']

                    cpf = form.data['cpf']
                    cidade = form.data['cidade']
                    cursor.execute(f'exec inserirDados "{nome}","{cpf}","{cidade}" ')
                    cursor.commit()
                    return redirect('home')
                    #result_set = cursor.fetchall()

            finally:
                cursor.close()

        
        elif "deletar" in request.POST:
            try:
                cursor = conn.cursor()
                if form2.is_valid:
                    idCliente = int(form.data['idCliente'])
                    cursor.execute(f'exec deletarDados "{idCliente}" ')
                    cursor.commit()
                    return redirect('home')

            finally:
                cursor.close()
            
    return render(request,"sistema_app/index/index.html",{'form':form,'form2':form2})


