# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 19:47:10 2023

@author: pc
"""

import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

# إعداد اتصال MySQL
db_connection = mysql.connector.connect(
    host="localhost",  # استبدل بعنوان الخادم الخاص بك
    user="root",    # استبدل بمعرف المستخدم الخاص بك
    password="",  # استبدل بكلمة المرور الخاصة بك
    database="ecommerce_db"  # استبدل باسم قاعدة البيانات الخاصة بك
)

# إنشاء محرك SQLAlchemy
engine = create_engine("mysql+mysqlconnector://root:@localhost/ecommerce_db")

# استعلام قاعدة البيانات واستخراج البيانات إلى DataFrame
query = """
    SELECT * FROM order_items,products,orders WHERE  order_items.ProductId=products.id
    AND order_items.OrderId=orders.id
"""
df = pd.read_sql(query, engine)

# إغلاق اتصال MySQL
db_connection.close()