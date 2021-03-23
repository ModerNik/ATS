from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import re
from selenium import webdriver
import mysql.connector
import mysql
import json
from mysql.connector import Error
#designed by apple in california (oleg in blyatskoi school)
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name,
            charset= 'utf8',
            use_pure = True
        )
        #print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
connection = create_connection("localhost", "root", "1234", "main_data")
cursor = connection.cursor()
cursor.execute("SET NAMES cp1251")
cursor.execute("set character set cp1251")

class myHandler(BaseHTTPRequestHandler):

    def OpenHtmlLocation(self, url):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=cp1251')
        self.end_headers()
        print(url)
        file = open(url, 'r')
        message = file.read()
        file.close()
        self.wfile.write(bytes(message, "cp1251"))
        return
    
    def do_GET(self):
        self.send_response(200)
        path = self.path
        if path == "/":
            path = "/index.html"
        print(path)
        isText = True
        try:
            if ".css" in path:
                self.send_header('Content-type', 'text/css; charset=cp1251')
                file  = open("html" + path, 'r')
            elif ".js" in path:
                self.send_header('Content-type', 'text/javascript')
                file = open("html" + path, 'r')
            elif ".png" in path:
                self.send_header('Content-type', 'image/png')
                file = open("html" + path, 'rb')
                isText = False
            elif ".jpg" in path:
                self.send_header('Content-type', 'image/jpeg')
                file = open("html" + path, 'rb')
                isText = False
            else:
                self.send_header('Content-type', 'text/html; charset=cp1251')
                file = open("html" + path, 'r')
            print(file)
        except FileNotFoundError:
            
            file  = open("html/404.html", 'r')
        #self.send_header('charset', 'utf-8')
        self.end_headers()
        message = file.read()
        file.close()
        if isText:
            self.wfile.write(bytes(message, "cp1251"))
        else:
            self.wfile.write(bytes(message))
        return

    def do_POST(self):
        #self.send_response(301)
        #self.send_header('Location','/support')
        #self.end_headers()
        path = self.path

        #Парсим параметры запроса и сохраняем их в fields в виде последовательных пар "ключ", "значение"
        content_len = int(self.headers.get('Content-Length'))
        post = self.rfile.read(content_len)
        #print(post)
        post = re.split(r'\'+', str(post))[1]
        #print(post)
        fields = re.split(r'[ \'\&=]+', str(post))
        #print(fields[1])

        FileToOpen = 'html/404.html'
        if path == "/signin":
            isParsed = False
            if len(fields) == 4:
                if "login" == fields[0]:
                    login = fields[1]
                    if "password" == fields[2]:
                        password = fields[3]
                        isParsed = True
            if isParsed:
                #УРА ДАВААААЙ УРААА ДААА
                cursor.execute("SELECT * FROM logpass WHERE login='%s'" % (login))
                results = cursor.fetchall()
                for row in results:
                    log = row[0]
                    pasw = row[1]
                    status = row[2]
                    name = row[3]
                if password == pasw:
                    if status == "admin":
                        FileToOpen = '/system_admins.html'
                    if status == "teacher":
                        FileToOpen = '/teachers.html'
                    if status == "ladmin":
                        FileToOpen = '/learning_admin.html'
                    if status == "student":
                        FileToOpen = '/students.html'
                else:
                    print ("it's sad")
            self.send_response(302)
            self.send_header('Location', FileToOpen)
            self.end_headers()
            return
        
        if path == "/add_person":
            FileToOpen = 'add_person.html'
            name_person = fields[1]
            name_person = name_person.replace('+', ' ');
            select = fields[3]
            login = fields[5]
            password = fields[7]
            if select == "s1":
                group = "11a"
                cursor.execute("INSERT INTO %s VALUES ('%s')" % (group, name_person))
                status = "student"
            if select == "s2":
                subject = "MA"
                cursor.execute("INSERT INTO teachers VALUES ('%s', '%s', NULL)" % (name_person, subject))
                status = "teacher"
            if select == "s3":
                status = "admin"
            if select == "s4":
                status = "ladmin"
            cursor.execute("INSERT INTO logpass VALUES ('%s', '%s', '%s', '%s')" % (login, password, status, name_person))
            connection.commit()
            self.send_response(302)
            self.send_header('Location', FileToOpen)
            self.end_headers()
            return;

        if path == "/add_group":
            FileToOpen = 'add_group.html'
            new_group = fields[1]
            name_teacher = fields[3]
            name_teacher = name_teacher.replace('+', ' ');
            name_student = fields[5]
            name_student = name_student.replace('+', ' ');
            cursor.execute("CREATE TABLE %s (name varchar(50))" % (new_group))
            cursor.execute("INSERT INTO groups VALUES ('%s')" % (new_group))
            cursor.execute("INSERT INTO %s VALUES ('%s')" % (new_group, name_student))
            cursor.execute("UPDATE teachers SET groups=concat_ws(',', groups, '%s') where name = '%s'" % (new_group, name_teacher))
            connection.commit()
            self.send_response(302)
            self.send_header('Location', FileToOpen)
            self.end_headers()
            return;
            
        if path == "/add_student_to_group":
            FileToOpen = 'add_group.html'
            group2 = fields[1]
            name_student = fields[3]
            name_student = name_teacher.replace('+', ' ');
            cursor.execute("INSERT INTO %s VALUES ('%s')" % (group2, name_student))

        if path == "/add_group_to_teacher":
            FileToOpen = 'add_group.html'
            group = fields[1]
            name_teacher = fields[3]
            name_teacher = name_teacher.replace('+', ' ');
            cursor.execute("UPDATE teachers SET groups=concat_ws(',', groups, '%s') where name = '%s'" % (group, name_teacher))

        if path == "/add_question":
            FileToOpen = 'add_question.html'
            name = fields[1]
            name = name.replace('+', ' ');
            group = fields[3]
            problem = fields[5]
            problem = problem.replace('+', ' ');
            v1 = fields[7]
            v1 = v1.replace('+', ' ');
            v2 = fields[9]
            v2 = v2.replace('+', ' ');
            v3 = fields[11]
            v3 = v3.replace('+', ' ');
            v4 = fields[13]
            v4 = v4.replace('+', ' ');
            answer = feilds[15]
            answer = answer.replace('+', ' ');
            cursor.execute("SELECT sub FROM teachers WHERE name='%s'" % (name_teacher))
            results = cursor.fetchall()
            for row in results:
                sub = row[0]
            cursor.execute("INSERT INTO questions VALUES(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, '%s')" % (sub, name, group, problem, v1, v2, v3, v4, answer, teacher))

        
        if path == "/find_group":
            FileToOpen = 'all_groups.html'
            find_group = fields[1]
            cursor.execute("SELECT * FROM %s" % (find_group))
            #cursor.execute("SELECT * FROM groups WHERE name LIKE '%s'" % (find_group))
            results = cursor.fetchall()
            print(results)
            self.send_response(302)
            self.send_header('Location', FileToOpen)
            self.end_headers()
            from webdriver_manager.chrome import ChromeDriverManager
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get("http://localhost:8081/all_groups.html")
            driver.execute_script("""
            var find_group = arguments[0];
            document.getElementById('1').innerHTML = find_group;
            """, find_group)
            
            self.send_response(302)
            self.send_header('Location', FileToOpen)
            self.end_headers()
            from bs4 import BeautifulSoup
            with open("html/all_groups.html", "r") as f:
                '''contents = f.read()
                soup = BeautifulSoup(contents, 'html.parser')
                tag = soup.find("div", id="result_form")
                tag.replace_with("2")
                print(soup.find("div", id="result_form"))'''
                markup = '<div id="result_form">1</div> '
                soup = BeautifulSoup(markup)
                soup.div
                new_tag = soup.new_tag('div')
                new_tag = '2'
                new_tag.string = soup.div.string
                soup.div.replace_with(new_tag)
                print(soup.div.prettify())

        if path == "/find_teacher":
            FileToOpen = 'all_teachers.html'
            find_teacher = fields[1]
            curson.execute("SELECT * FROM teachers WHERE name LIKE '%s'" % (find_teacher))
            results = cursor.fetchall()
        

server = HTTPServer(('127.0.0.1', 8081), myHandler)
server.serve_forever()
