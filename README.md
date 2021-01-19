1. Условия
Необходимо разработать информационную систему автоматизированного тестирования
учащихся. 2. Техническое задание
В системе должны быть предусмотрены 4 типа (роли) пользователей:
1. Администратор учебного процесса. 2. Администратор системы. 3. Преподаватель. 4. Студент. 1. Администратор учебного процесса должен иметь возможность: - просматривать результаты тестирования студентов; - просматривать списки групп, относящихся к преподавателю
- просматривать запланированные тестирования; - просматривать оценки за тестирования; - просматривать загруженные преподавателем задания. 2. Администратор системы должен иметь возможность: - добавлять группы
- добавлять списки студентов в группы; - назначать группы преподавателям; - назначать роли (регистрировать пользователей). 3. Преподаватель должен иметь возможность: - добавлять задания для тестирования с группировкой их по учебным модулям; - просматривать списки групп; - просматривать результаты тестирования студентов по своему предмету у своих групп; - задавать параметры для формирования системой тестирования: кол-во вопросов всего, кол-во заданий из модуля, кол-во модулей. 4. Студент должен иметь возможность: - проходить тестирование по билетам, сформированными системой из заданий; - видеть оценку за тестирование. Система должна:
МОСКОВСКАЯ ПРЕДПРОФЕССИОНАЛЬНАЯ
ОЛИМПИАДА ШКОЛЬНИКОВ
Профиль «Информационные технологии»
Командный кейс №6 «Автоматизированное тестирование учащихся»
Москва
2020/2021 уч. г.
- давать возможность планировать проведение тестирования; - автоматически формировать билеты из заданий: случайно или в ручную; - автоматически проверять ответы и выставлять оценку; - отображать результаты тестирования авторизованным пользователям: администратору
учебного процесса и преподавателю. Количество учебных модулей при формировании теста выбирается произвольное
количество вопросов случайными или определённым образом. Архитектура системы должна включать в себя как минимум два программных модуля:
серверную часть (back-end) и клиентскую часть (front-end). Пользовательский интерфейс рекомендуется делать кроссплатформенным, удобным и
понятным пользователю. Рекомендуется использовать СУБД для хранения собранных данных, также предоставить
ER модель. Проект рекомендуется вести с помощью системы контроля версий git. Рекомендуется использовать unit-тестирование при разработке программных модулей
системы. 3. Регламент испытаний
- От имени администратора системы добавляются пользователи: 1 администратор
учебного процесса, не менее 2-ух преподавателей, не менее 2-ух групп учащихся по не менее
5-ти пользователей в каждой. Каждая группа назначается разному преподавателю. - От имени преподавателей добавляются задания по не менее чем 2-ум учебным модулям. - Планируется проведение тестирования. - Формируются билеты для тестирования для не менее чем одной группы. - От имени учащегося проходится тестирование по сформированному билету с
получением оценки по завершению. - От имени преподавателя просматриваются оценки, закрепленной за ним группы. - От имени администратора учебного процесса просматриваются оценки по всем группам. 4. Примерный перечень средств и инструментов для выполнения задания
● https://www.python.org/
● https://nodejs.org/
МОСКОВСКАЯ ПРЕДПРОФЕССИОНАЛЬНАЯ
ОЛИМПИАДА ШКОЛЬНИКОВ
Профиль «Информационные технологии»
Командный кейс №6 «Автоматизированное тестирование учащихся»
Москва
2020/2021 уч. г.
● https://sqlite.org/
● https://www.postgresql.org/
● https://pypi.org/project/requests/
● https://reactjs.org/
● https://vuejs.org/
● https://matplotlib.org/
● https://poiskvps.ru/
