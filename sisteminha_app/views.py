# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.db import connection



def home(request):

    cursor = connection.cursor()

    if request == 'POST':
        try:
            cursor.callproc('[dbo].[selecionarDados]')
            if cursor.return_value == 1:
                result_set = cursor.fetchall()
                
        finally:
            cursor.close()
            
    return render(request,"sistema_app/index/index.html",{})


