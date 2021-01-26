//#include "stdafx.h"
#include <conio.h>
#include <stdlib.h>
#include <mysql.h>
#include <stdio.h>
#include <windows.h>
#include <iostream>
using namespace std;

MYSQL* connection, mysql;
MYSQL_RES* result;
MYSQL_ROW row;
MYSQL* link;
int query_state;
const char Host[] = { "localhost" };
const char User[] = { "root" };
const char Pass[] = { "1234" };
const char DBase[] = { "main_data" };
//link = mysql_init(0);

void menu(string user){
	if (user == "admin"){
		cout << "Вы дэбил";
	}
}

void create_group(MYSQL* link,  string name) {
	string query = "CREATE TABLE ";
	query += name;
	query += " (name VARCHAR(20), sname VARCHAR(20))";
	mysql_query(link, query.c_str());
	query = "INSERT INTO groups VALUES ('";
	query += name;
	query += "')";
	mysql_query(link, query.c_str());
}

void add_student(MYSQL* link, string group, string name){
	string query = "INSERT INTO ";
	query += group;
	query += " VALUES ('";
	query += name;
	query += "')";
	mysql_query(link, query.c_str());
}

void add_teacher(MYSQL* link, string name, string subject) {
	string query = "INSERT INTO teachers VALUES ('";
	query += name;
	query += "', '";
	query += subject;
	query += "')";
	mysql_query(link, query.c_str());
}

void add_group_to_teacher(MYSQL* link, string group, string name){
	string quer = "SELECT groups FROM teachers WHERE name = '";
	quer += name;
	quer += "'";
	mysql_query(link, quer.c_str());
	result = mysql_store_result(link);
	row = mysql_fetch_row(result);
	string query;
	if (row[0] == NULL){
		query = "UPDATE teachers SET groups = ('";
	}
	else {
		query = "UPDATE teachers SET groups = CONCAT_WS(',', groups, '";
	}
	query += group;
	query += "') WHERE name = '";
	query += name;
	query += "'";
	cout << query;
	mysql_query(link, query.c_str());
}

int main() {
	setlocale(LC_ALL, ".1251");
	link = mysql_init(0);
	mysql_real_connect(link, Host, User, Pass, DBase, 0, 0, 0);
	result = 0;
	mysql_query(link, "SET NAMES 'cp1251'");

	//add_group_to_teacher(link, "11А", "Stas Shimchenko");
	//create_group(link, "11В");
	string query = "UPDATE teachers SET groups = ('11В') WHERE name = 'Stas Shimchenko'";
	mysql_query(link, query.c_str());
	/*while ((row = mysql_fetch_row(result))){
		for (int i = 0; i < mysql_num_fields(result); i++)
			printf("%s\t", row[i]);
		printf("\n");
	}*/
}
