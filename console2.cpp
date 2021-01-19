//#include"stdafx.h"
#include<iostream.h>
#include<conio.h>
#include<stdlib.h>
#include<stdio.h>
#include<mysql.h>
#include<string>
#include<vector>

using namespace std;

int_tmain(intargc, _TCHAR* argv[])
{

	system("cls");

	MYSQL* conn;
	MYSQL_RES* res;
	MYSQL_ROW row;

	int i = 0;

	// Получаем дескриптор соединения
	conn = mysql_init(NULL);
	if (conn == NULL)
	{
		// Если дескриптор не получен – выводим сообщение об ошибке
		fprintf(stderr, "Error: can'tcreate MySQL-descriptor\n");
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

	mysql_set_character_set(conn, "utf8");
	//Смотрим изменилась ли кодировка на нужную, по умалчанию идёт latin1
	cout << "connectioncharacterset: " << mysql_character_set_name(conn) << endl;

	mysql_query(conn, "SELECT id, text FROM mnu"); //Делаем запрос к таблице по имени МНУ =)

	if (res = mysql_store_result(conn)) {
		while (row = mysql_fetch_row(res)) {
			for (i = 0; i < mysql_num_fields(res); i++) {
				std::cout << row[i] << "\n"; //Выводим все что есть в базе через цикл
			}
		}
	} elsefprintf(stderr, "%s\n", mysql_error(conn));

	// Закрываем соединение с сервером базы данных
	mysql_close(conn);

	system("Pause");

	return 0;
}
