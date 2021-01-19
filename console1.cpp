#include <iostream>
#include <mysql.h>
MYSQL* connection, mysql;
MYSQL_RES* result;
MYSQL_ROW row;
int query_state;

int main() {
    mysql_init(&mysql);
    //connection = mysql_real_connect(&mysql,"host","user",
    //                   "password","database",port,"unix_socket",clientflag);
    connection = mysql_real_connect(&mysql, "localhost",
        "root", "qwer", "cpp_data", 3306, 0, 0);
    if (connection == NULL) {
        std::cout << mysql_error(&amp; mysql) << std::endl;
        return 1;
    }

    query_state = mysql_query(connection, "select user_count()");
    if (query_state != 0) {
        std::cout << mysql_error(connection) << std::endl;
        return 1;
    }

    result = mysql_store_result(connection);
    while ((row = mysql_fetch_row(result)) != NULL) {
        std::cout << "Number of active users : " << row[0] << std::endl;
    }

    mysql_free_result(result);
    mysql_close(connection);

    return 0;
}
