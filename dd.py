# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import sqlite3

con = sqlite3.connect("meal.db")
cur = con.cursor()
query = ("delete FROM meal")
cur.execute(query)
data = cur.fetchone()

