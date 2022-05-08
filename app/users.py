import pymysql
from db import mysql
from flask import request
import logging

logger = logging.getLogger(__name__)

def getAllUsers():
    logger.info("Get users ...")
    conn = mysql.connect()    
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM user")
    
    rows = cursor.fetchall()
    logger.info("Got users: {}".format(rows))
    return rows

def getUserByLogin(login):
    logger.info("Get user {}".format(login))
    conn = mysql.connect()    
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM user where login = '" + login + "'")
    
    rows = cursor.fetchall()
    logger.info("Got user: {}".format(rows))
    if rows == ():
        return
    return rows[0]

def loginUser(login, password):
    logger.info("Get user {} / {}".format(login, password))
    conn = mysql.connect()    
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM user where login = '" + login + "' and password = '" + password  + "'")
    
    rows = cursor.fetchall()
    logger.info("Got user: {}".format(rows))
    if rows == ():
        return
    return rows[0]

def createUserFromForm(form):
    email = form.get('email')
    name = form.get('name')
    login = form.get('login')
    password = form.get('password')
    role = 'user'

    # This is the safe way, no SQL injection possible
    val = (name, email, login, password, role)
    sql = "INSERT INTO `user`(`name`,`email`,`login`,`password`,`role`) values (%s, %s, %s, %s, %s)" 

    conn = mysql.connect()   
    cursor = conn.cursor()
    cursor.execute(sql, val)
    conn.commit()
    logger.info(cursor.rowcount, "record inserted.")
