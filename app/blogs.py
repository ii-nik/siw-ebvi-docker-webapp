import pymysql
from db import mysql
from flask import request
from flask_login import current_user 
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def getAllBlogs():
    logger.info("Get blogs ...")
    conn = mysql.connect()    
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM blog ORDER BY id ASC")
    
    rows = cursor.fetchall()
    logger.info("Got blogs: {}".format(rows))
    return rows

def getBlogById(id):
    logger.info("Get blog by ID")
    conn = mysql.connect()    
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM blog WHERE id = " + id)
    
    rows = cursor.fetchall()
    logger.info("Got blogs: {}".format(rows))
    if rows == ():
        return
    return rows[0]

def createBlog(form):
    createddate = datetime.now().isoformat()
    login = current_user.name
    text = form.get('text')

    # This is the safe way, no SQL injection possible
    val = (createddate, login, text)
    sql = "INSERT INTO `blog`(`createdate`,`login`,`text`) values (%s, %s, %s)" 

    conn = mysql.connect()   
    cursor = conn.cursor()
    cursor.execute(sql, val)
    conn.commit()
    logger.info(cursor.rowcount, "record inserted.")

    
def searchAllBlogs(searchparameter):
    logger.info("Search blogs ...")

    # This is not safe
    sql = "SELECT id, createdate, login, text FROM blog WHERE text like '%" + searchparameter + "%' ORDER BY id ASC" 

    conn = mysql.connect()    
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    rows = cursor.fetchall()
    logger.info("Found blogs: {}".format(rows))
    return rows

def updateBlog(form):
    text = form.get('text')
    id = form.get('id')

    # This is the safe way, no SQL injection possible
    val = (text, id)
    sql = "UPDATE `blog` SET text = %s WHERE id = %s"

    conn = mysql.connect()   
    cursor = conn.cursor()
    cursor.execute(sql, val)
    conn.commit()
    logger.info(cursor.rowcount, "blog with id {} updated with text {}".format(id, text))

def deleteBlog(id):

    # This is the safe way, no SQL injection possible
    val = (id)
    sql = "DELETE FROM `blog` WHERE id = %s"

    conn = mysql.connect()   
    cursor = conn.cursor()
    cursor.execute(sql, val)
    conn.commit()
    logger.info(cursor.rowcount, "blog with id {} deleted".format(id))