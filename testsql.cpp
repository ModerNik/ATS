//#include "stdafx.h"
#include <conio.h>
#include <stdlib.h>
#include <mysql.h>
#include <stdio.h>
#include <iostream>
using namespace std;

MYSQL *connection, mysql;
MYSQL_RES *result;
MYSQL_ROW *row;
int query_state;

int main(){
	/*mysql_init(&mysql);
    connection = mysql_real_connect(&mysql, "localhost", "root", "1234", "cpp_data", 3305, 0, 0);
    if (connection == NULL) {
        cout << "err" << endl;
        return 1;
    } else {
        cout << "connected" << endl;
    }
    (query_state = mysql_query(connection, "select user_count()");
    if (query_state != 0) {
        cout << mysql_error(connection) << endl;
        return 1;
    }

    result = mysql_store_result(connection);
    while ((row = mysql_fetch_row(result)) != NULL) {
        cout << "Number of active users : " << row[0] << endl;
    }

    mysql_free_result(result);
    mysql_close(connection);
    */
        MYSQL* conn;
        // Получаем дескриптор соединения
        conn = mysql_init(NULL);
        if (conn == NULL)
        {
            // Если дескриптор не получен – выводим сообщение об ошибке
            fprintf(stderr, "Error: can't create MySQL-descriptor\n");
            //exit(1); //Если используется оконное приложение
        }
        // Подключаемся к серверу
        if (!mysql_real_connect(conn, "localhost", "root", "root", "test", NULL, NULL, 0))
        {
            // Если нет возможности установить соединение с сервером
            // базы данных выводим сообщение об ошибке
            fprintf(stderr, "Error: can'tconnecttodatabase %s\n", mysql_error(conn));
        }
        else
        {
            // Если соединение успешно установлено выводим фразу - "Success!"
            fprintf(stdout, "Success!\n");
        }
        // Закрываем соединение с сервером базы данных
        mysql_close(conn);

        system("Pause");
return 0;
}