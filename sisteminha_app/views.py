# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import ClienteForm,DeleteClienteForm
import pyodbc 



def home(request):

    form = ClienteForm
    form2 = DeleteClienteForm

    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-0P0GI6A\SQLEXPRESS;' #servidor do banco
                      'Database=Teste;' #tabela
                      'Trusted_Connection=yes;', autocommit=True)
    
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        form2 = DeleteClienteForm(request.POST)

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
                    idCliente = int(form2.data['idCliente'])
                    cursor.execute(f'exec deletarDados "{idCliente}" ')
                    cursor.commit()
                    return redirect('home')

            finally:
                cursor.close()
            
    return render(request,"sistema_app/index/index.html",{'form':form,'form2':form2})

def consultaBanco(request):
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-0P0GI6A\SQLEXPRESS;' #servidor do banco
                      'Database=Teste;' #tabela
                      'Trusted_Connection=yes;', autocommit=True)
    banco = conn.cursor()
    banco.execute('exec selecionarDados')
    banco_completo = banco.fetchall()
    return render(request, "sistema_app/index/banco.html", {'banco':banco_completo})

def quantidadeTotal(request, pk):
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-0P0GI6A\SQLEXPRESS;' #servidor do banco
                      'Database=Teste;' #tabela
                      'Trusted_Connection=yes;', autocommit=True)
    banco = conn.cursor()
    banco.execute(f'SELECT * FROM [dbo].[QuantidadeTotal]({pk})')
    banco_completo = banco.fetchall()
    return render(request, "sistema_app/index/qt.html", {'banco':banco_completo})

