import math
import sqlite3
import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QTableWidgetItem


class AboutWindow(QWidget):
    def __init__(self):
        super(AboutWindow, self).__init__()

        self.setWindowTitle('О программе')
        self.setLayout(QVBoxLayout(self))
        self.info = QLabel(self)
        self.info.setStyleSheet('font: italic 14pt "Times New Roman";')
        self.info.setText('Расчет треугольника позволит вам рассчитать все стороны, углы и площадь равностороннего,\n'
                          'разностороннего, равнобедренного, прямоугольного треугольника.\n\n'
                          'Нажмите "Запуск", чтобы перейти в калькулятор.\n\nНажмите "Проверить", чтобы узнать о '
                          'корректности введенных данных.\n\n'
                          'Введите 3 известных значения.\nНапример, 2 стороны и 1 угол или 3 стороны,'
                          ' и нажмите "Вычислить",\nчтобы узнать остальные стороны, углы и площадь треугольника.\n\n'
                          'При нажатии на кнопку "История решений" Вам откроется окно с таблицей базы данных,\n'
                          'В окне внизу вы можете ввести запрос для работы с базой данных.\n При нажатии на кнопку'
                          '"Выполнить", выполняется соответсвующий запрос.')
        self.layout().addWidget(self.info)


class Solution(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Solution, self).__init__(parent)
        uic.loadUi('solution.ui', self)

        con = sqlite3.connect('project.db')
        cur = con.cursor()
        res = cur.execute('''SELECT sol FROM my
        ''').fetchall()

        self.label = QLabel(self)
        self.label.setStyleSheet('font: italic 14pt "Times New Roman";')
        if res[-1] == (1,):
            self.label.setText("Решение по 3 сторонам\n\nИз теоремы косинусов имеем:\na**2 = b**2 + c**2 - 2 * b * c *"
                               " cosA\n"
                               "b**2 = a**2 + c**2 - 2 * a * c * cosB\nОткуда\ncosA = (b**2 + c**2 - a**2) / "
                               "(2 * b * c)\ncosB = (a**2 + c**2 - b**2) / (2 * a * c)\ncosA, cosB и углы A и B.\n"
                               "Далее, угол C находим из выражения:\nС = 180° - А - В (Теорема о сумме углов "
                               "треугольника)")
            self.label.move(10, 10)

        elif res[-1] == (2,):
            self.label.setText('Найдем сторону c используя теорему косинусов:\nc**2 = a**2 + b**2 – 2 * a * b * cosC\n'
                               'c = sqrt(a**2 + b**2 – 2 * a * b * cosC) \nДалее, из теоремы косинусов: \na**2 = b**2'
                               ' + c**2 – 2 * b * c * cosA\nнайдем cosA: \ncosA = (b**2 + c**2 - a**2) / (2 * b * c) '
                               '\nДалее находим угол A. \nПоскольку уже нам известны два угла то находим третий из'
                               ' теоремы о сумме углов треугольника: \nB = 180° – A – C\n')
            self.label.move(10, 10)

        elif res[-1] == (3,):
            self.label.setText('Найдем сторону b используя теорему косинусов: \nb**2 = a**2 + c**2 – 2 * a * c * cosB\n'
                               'b = sqrt(a**2 + c**2 – 2 * a * c * cosB) \nДалее, из теоремы косинусов: \na**2 = b**2'
                               ' + c**2 – 2 * b * c * cosA\nнайдем cosA: \ncosA = (b**2 + c**2 - a**2) / (2 * b * c) \n'
                               'Далее находим угол A. \nПоскольку уже нам известны два угла то находим третий из '
                               'теоремы о сумме углов треугольника: \nC = 180° – A –  B\n')
            self.label.move(10, 10)

        elif res[-1] == (4,):
            self.label.setText('Найдем сторону a используя теорему косинусов: \na**2 = c**2 + b**2 – 2 * c * b * cosA\n'
                               'a = sqrt(c**2 + b**2 – 2 * c * b * cosA) \nДалее, из теоремы косинусов: \nc**2 = b**2 '
                               '+ a**2 – 2 * a * b * cosC\nнайдем cosC: \ncosC = (b**2 + a**2 - c**2) / (2 * b * a) \n'
                               'Далее находим угол C. \nПоскольку уже нам известны два угла то находим третий из '
                               'теоремы о сумме углов треугольника: \nB = 180° – A – C\n')
            self.label.move(10, 10)

        elif res[-1] == (5,):
            self.label.setText('Найдем стороны b и c и угол C. \nТак как, уже известны два угла, то можно найти третий'
                               ' из теоремы о сумме углов треугольника: \nС = 180° – A – В\nДалее, для находждения '
                               'сторон b и c воспользуемся тероемой синусов: \nb / (sinB) = a / (sinA),  c / (sinC) = '
                               'a / (sinA) \nОткуда\nb = (a * sinB) / (sinA),  c = (a * sinC) / (sinA) \n')
            self.label.move(10, 10)

        elif res[-1] == (6,):
            self.label.setText('Найдем стороны b и c и угол B. \nТак как, уже известны два угла, то можно найти '
                               'третий из теоремы о сумме углов треугольника: \nB = 180° – A – C\nДалее, для '
                               'находждения сторон b и c воспользуемся тероемой синусов: \nb / (sinB) = a / (sinA),'
                               '  c / (sinC) = a / (sinA) \nОткуда\nb = (a * sinB) / (sinA),  c = (a * sinC) / (sinA)'
                               ' \n')
            self.label.move(10, 10)

        elif res[-1] == (7,):
            self.label.setText('Найдем стороны b и c и угол A. \nТак как, уже известны два угла, то можно найти '
                               'третий из теоремы о сумме углов треугольника: \nA = 180° – A – C\n	Далее, для '
                               'находждения сторон b и c воспользуемся тероемой синусов: \nb / (sinB) = a / (sinA),'
                               '  c / (sinC) = a / (sinA) \nОткуда\nb = (a * sinB) / (sinA),  c = (a * sinC) / (sinA)'
                               ' \n')
            self.label.move(10, 10)

        elif res[-1] == (8,):
            self.label.setText('Найдем стороны a  и c и угол C. \nТак как, уже известны два угла, то можно найти '
                               'третий из теоремы о сумме углов треугольника: \nС = 180° – A – В\n	Далее, для '
                               'находждения сторон a  и c воспользуемся тероемой синусов: \nb / (sinB) = a / (sinA),'
                               '  c / (sinC) = b / (sinB) \nОткуда\na = (b * sinA) / (sinB),  c = (b * sinC) / (sinB)'
                               ' \n')
            self.label.move(10, 10)

        elif res[-1] == (9,):
            self.label.setText('Найдем стороны a и c и угол B. \nТак как, уже известны два угла, то можно найти'
                               ' третий из теоремы о сумме углов треугольника: \nB = 180° – A – C\nДалее, для'
                               ' находждения сторон a  и c воспользуемся тероемой синусов: \nb / (sinB) = a / (sinA),'
                               '  c / (sinC) = b / (sinB) \nОткуда\na = (b * sinA) / (sinB),  c = (b * sinC) / (sinB)'
                               ' \n')
            self.label.move(10, 10)

        elif res[-1] == (10,):
            self.label.setText('Найдем стороны a и c и угол A. \nТак как, уже известны два угла, то можно найти '
                               'третий из теоремы о сумме углов треугольника: \nA = 180° – B – C\nДалее, для'
                               ' находждения сторон a  и c воспользуемся тероемой синусов: \nb / (sinB) = a / (sinA),'
                               '  c / (sinC) = b / (sinB) \nОткуда\na = (b * sinA) / (sinB),  c = (b * sinC) / (sinB)'
                               ' \n')
            self.label.move(10, 10)

        elif res[-1] == (11,):
            self.label.setText('Найдем стороны a  и b и угол C. \nТак как, уже известны два угла, то можно найти '
                               'третий из теоремы о сумме углов треугольника: \nС = 180° – A – В\nДалее, для '
                               'находждения сторон a  и c воспользуемся тероемой синусов: \nc / (sinC) = a / (sinA),'
                               '  c / (sinC) = b / (sinB) \nОткуда\na = (c * sinA) / (sinC),  b = (c * sinB) / (sinC)'
                               ' \n')
            self.label.move(10, 10)

        elif res[-1] == (12,):
            self.label.setText('Найдем стороны a  и b и угол B. \nТак как, уже известны два угла, то можно найти '
                               'третий из теоремы о сумме углов треугольника: \nB = 180° – A – C\nДалее, для '
                               'находждения сторон a  и c воспользуемся тероемой синусов: \nc / (sinC) = a / (sinA),'
                               '  c / (sinC) = b / (sinB) \nОткуда\na = (c * sinA) / (sinC),  b = (c * sinB) / (sinC)'
                               ' \n')
            self.label.move(10, 10)

        else:
            self.label.setText('Найдем стороны a  и b и угол A. \nТак как, уже известны два угла, то можно найти '
                               'третий из теоремы о сумме углов треугольника: \nA = 180° – C – В\nДалее, для '
                               'находждения сторон a  и c воспользуемся тероемой синусов: \nc / (sinC) = a / (sinA),'
                               '  c / (sinC) = b / (sinB) \nОткуда\na = (c * sinA) / (sinC),  b = (c * sinB) / (sinC)'
                               ' \n')
            self.label.move(10, 10)


class MyError(Exception):
    # Собственный класс исключений для ненатуральных значений сторон треугольника
    def __init__(self, text):
        self.txt = text


class ActionHistory(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ActionHistory, self).__init__(parent)
        uic.loadUi('history.ui', self)

        self.connection = sqlite3.connect("project.db")
        self.pushButton.clicked.connect(self.select_data)
        # По умолчанию будем выводить все данные из таблицы my
        self.textEdit.setPlainText("SELECT * FROM my")
        self.select_data()

    def select_data(self):
        # при нажатии на кнопку можем выполнить запрос в отднльном поле
        query = self.textEdit.toPlainText()
        res = self.connection.cursor().execute(query).fetchall()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()


class ClassDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClassDialog, self).__init__(parent)
        uic.loadUi('calc.ui', self)
        self.pushButton_2.clicked.connect(self.go)
        # Открывает окно "решение"
        self.pushButton_3.clicked.connect(self.count)
        self.pushButton.clicked.connect(self.count_2)

    def go(self):
        if self.label_8.text() != "Упс, кажется недостаточно данных. Я не могу решить эту задачу" and\
                self.label_8.text() != 'Некорректные данные':
            dialog = Solution(self)
            dialog.exec_()

    def count(self):
        self.label_8.setText('')
        if self.lineEdit_2.text() == '':
            self.a = -1
        else:
            try:
                if int(self.lineEdit_2.text()) > 0:
                    self.a = int(self.lineEdit_2.text())
                if int(self.lineEdit_2.text()) <= 0:
                    raise MyError('Для стороны введите натуральное число')
            except MyError:
                self.label_8.setText('Для стороны введите натуральное число')
            except Exception as e:
                self.label_8.setText(f"Ошибка! {e}")

        if self.lineEdit_3.text() == '':
            self.b = -1
        else:
            try:
                if int(self.lineEdit_3.text()) > 0:
                    self.b = int(self.lineEdit_3.text())
                if int(self.lineEdit_3.text()) <= 0:
                    raise MyError('Для стороны введите натуральное число')
            except MyError:
                self.label_8.setText('Для стороны введите натуральное число')
            except Exception as e:
                self.label_8.setText(f"Ошибка! {e}")

        if self.lineEdit_5.text() == '':
            self.c = -1
        else:
            try:
                if int(self.lineEdit_5.text()) > 0:
                    self.c = int(self.lineEdit_5.text())
                if int(self.lineEdit_5.text()) <= 0:
                    raise MyError('Для стороны введите натуральное число')
            except MyError:
                self.label_8.setText('Для стороны введите натуральное число')
            except Exception as e:
                self.label_8.setText(f"Ошибка! {e}")

        if self.lineEdit.text() == '':
            self.alfa = -1
        else:
            try:
                if 0 < int(self.lineEdit.text()) < 180:
                    self.alfa = int(self.lineEdit.text())
                if int(self.lineEdit.text()) <= 0 or int(self.lineEdit.text()) >= 180:
                    raise MyError('Для угла введите натуральное число, не превышающее 180')
            except MyError:
                self.label_8.setText('Для угла введите натуральное число, не превышающее 180')
            except Exception as e:
                self.label_8.setText(f"Ошибка! {e}")

        if self.lineEdit_4.text() == '':
            self.betta = -1
        else:
            try:
                if 0 < int(self.lineEdit_4.text()) < 180:
                    self.betta = int(self.lineEdit_4.text())
                if int(self.lineEdit_4.text()) <= 0 or int(self.lineEdit_4.text()) >= 180:
                    raise MyError('Для угла введите натуральное число, не превышающее 180')
            except MyError:
                self.label_8.setText('Для угла введите натуральное число, не превышающее 180')
            except Exception as e:
                self.label_8.setText(f"Ошибка! {e}")

        if self.lineEdit_6.text() == '':
            self.gamma = -1
        else:
            try:
                if 0 < int(self.lineEdit_6.text()) < 180:
                    self.gamma = int(self.lineEdit_6.text())
                if int(self.lineEdit_6.text()) <= 0 or int(self.lineEdit_6.text()) >= 180:
                    raise MyError('Для угла введите натуральное число, не превышающее 180')
            except MyError:
                self.label_8.setText('Для угла введите натуральное число, не превышающее 180')
            except Exception as e:
                self.label_8.setText(f"Ошибка! {e}")

        try:
            self.label_10.setText(str(self.a))
            self.label_11.setText(str(self.b))
            self.label_12.setText(str(self.c))
            self.label_13.setText(str(self.alfa))
            self.label_14.setText(str(self.betta))
            self.label_15.setText(str(self.gamma))
        except Exception as e:
            self.label_8.setText(f"Ошибка! {e}")

    def count_2(self):
        a = int(self.label_10.text())
        b = int(self.label_11.text())
        c = int(self.label_12.text())
        alfa = int(self.label_13.text())
        betta = int(self.label_14.text())
        gamma = int(self.label_15.text())
        if alfa != -1 and betta != -1 and gamma != -1:
            if not (179 < (alfa + betta + gamma) < 181):
                self.label_8.setText('Некорректные данные')
                return ''
        if (a != -1 and b != -1 and c == -1 and alfa != -1 and betta == -1 and gamma == -1) or \
                (a != -1 and b != -1 and c == -1 and alfa == -1 and betta != -1 and gamma == -1) or \
                (a == -1 and b != -1 and c != -1 and alfa == -1 and betta != -1 and gamma == -1) or \
                (a == -1 and b != -1 and c != -1 and alfa == -1 and betta == -1 and gamma != -1) or \
                (a != -1 and b == -1 and c != -1 and alfa != -1 and betta == -1 and gamma == -1) or \
                (a != -1 and b == -1 and c != -1 and alfa == -1 and betta == -1 and gamma != -1):
            self.label_8.setText('К сожалению, я не могу решить этот треугольник')
            return ''
        if a != -1 and b != -1 and c != -1:  # по трем сторонам
            if (a + b) <= c or (b + c) <= a or (a + c) <= b:
                self.label_8.setText('Некорректные данные')
                return

            if alfa == -1:
                alfa = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / math.pi

            if betta == -1:
                betta = (math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)) * 180) / math.pi

            if gamma == -1:
                gamma = 180 - alfa - betta

            con = sqlite3.connect('project.db')
            # Вносим значения в базу данных
            cur = con.cursor()
            res = cur.execute('''INSERT INTO my(side_a,side_b,side_c,angle_A,angle_B,angle_C,sol)
                        VALUES(?, ?, ?, ?, ?, ?, 1)
                        ''', (a, b, c, alfa, betta, gamma,)).fetchall()
            con.commit()
            print(res)

        elif a != -1 and b != -1 and gamma != -1:  # сторона а, сторона b и угол между ними
            if c == -1:
                c = (a ** 2 + b ** 2 - 2 * a * b * math.cos((gamma * math.pi) / 180)) ** (1 / 2)

            if alfa == -1:
                alfa = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / math.pi

            if betta == -1:
                betta = 180 - alfa - gamma

            con = sqlite3.connect('project.db')
            # Вносим значения в базу данных
            cur = con.cursor()
            res = cur.execute('''INSERT INTO my(side_a,side_b,side_c,angle_A,angle_B,angle_C,sol)
                                    VALUES(?, ?, ?, ?, ?, ?, 2)
                                    ''', (a, b, c, alfa, betta, gamma,)).fetchall()
            con.commit()
            print(res)

        elif a != -1 and c != -1 and betta != -1:  # сторона а, сторона c и угол между ними
            if b == -1:
                b = (a ** 2 + c ** 2 - 2 * a * c * math.cos((betta * math.pi) / 180)) ** (1 / 2)

            if alfa == -1:
                alfa = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / math.pi

            if gamma == -1:
                gamma = 180 - alfa - betta

            con = sqlite3.connect('project.db')
            # Вносим значения в базу данных
            cur = con.cursor()
            res = cur.execute('''INSERT INTO my(side_a,side_b,side_c,angle_A,angle_B,angle_C,sol)
                                                VALUES(?, ?, ?, ?, ?, ?, 3)
                                                ''', (a, b, c, alfa, betta, gamma,)).fetchall()
            con.commit()
            print(res)

        elif c != -1 and b != -1 and alfa != -1:  # сторона c, сторона b и угол между ними
            if a == -1:
                a = (c ** 2 + b ** 2 - 2 * c * b * math.cos((alfa * math.pi) / 180)) ** (1 / 2)
            if gamma == -1:
                gamma = (math.acos((b ** 2 + a ** 2 - c ** 2) / (2 * b * a)) * 180) / math.pi
            if betta == -1:
                betta = 180 - alfa - gamma

            con = sqlite3.connect('project.db')
            # Вносим значения в базу данных
            cur = con.cursor()
            res = cur.execute('''INSERT INTO my(side_a,side_b,side_c,angle_A,angle_B,angle_C,sol)
                                                VALUES(?, ?, ?, ?, ?, ?, 4)
                                                ''', (a, b, c, alfa, betta, gamma,)).fetchall()
            con.commit()
            print(res)

        elif a != -1:
            if alfa != -1 and betta != -1:
                sol = 5  # сторона а и углы А и В
                if gamma == -1:
                    gamma = 180 - alfa - betta

            elif alfa != -1 and gamma != -1:
                sol = 6  # сторона а и углы А и C
                if betta == -1:
                    betta = 180 - alfa - gamma

            elif betta != -1 and gamma != -1:
                sol = 7  # сторона а и углы B и C
                if alfa == -1:
                    alfa = 180 - betta - gamma

            if b == -1:
                b = (a * math.sin((betta * math.pi) / 180)) / math.sin((alfa * math.pi) / 180)
            if c == -1:
                c = (a * math.sin((gamma * math.pi) / 180)) / math.sin((alfa * math.pi) / 180)

            con = sqlite3.connect('project.db')
            # Вносим значения в базу данных
            cur = con.cursor()
            res = cur.execute('''INSERT INTO my(side_a,side_b,side_c,angle_A,angle_B,angle_C,sol)
                                                VALUES(?, ?, ?, ?, ?, ?, ?)
                                                ''', (a, b, c, alfa, betta, gamma, sol,)).fetchall()
            con.commit()
            print(res)

        elif b != -1:
            if alfa != -1 and betta != -1:
                sol = 8  # сторона b и углы А и В
                if gamma == -1:
                    gamma = 180 - alfa - betta

            elif alfa != -1 and gamma != -1:
                sol = 9  # сторона b и углы А и C
                if betta == -1:
                    betta = 180 - alfa - gamma

            elif betta != -1 and gamma != -1:
                sol = 10  # сторона b и углы B и C
                if alfa == -1:
                    alfa = 180 - betta - gamma

            if a == -1:
                a = (b * math.sin((alfa * math.pi) / 180)) / math.sin((betta * math.pi) / 180)
            if c == -1:
                c = (b * math.sin((gamma * math.pi) / 180)) / math.sin((betta * math.pi) / 180)

            con = sqlite3.connect('project.db')
            # Вносим значения в базу данных
            cur = con.cursor()
            res = cur.execute('''INSERT INTO my(side_a,side_b,side_c,angle_A,angle_B,angle_C,sol)
                                                            VALUES(?, ?, ?, ?, ?, ?, ?)
                                                            ''', (a, b, c, alfa, betta, gamma, sol,)).fetchall()

        elif c != -1:
            if alfa != -1 and betta != -1:
                sol = 11  # сторона c и углы А и В
                if gamma == -1:
                    gamma = 180 - alfa - betta

            elif alfa != -1 and gamma != -1:
                sol = 12  # сторона c и углы А и C
                if betta == -1:
                    betta = 180 - alfa - gamma

            elif betta != -1 and gamma != -1:
                sol = 13  # сторона c и углы B и C
                if alfa == -1:
                    alfa = 180 - betta - gamma

            if a == -1:
                a = (c * math.sin((alfa * math.pi) / 180)) / math.sin((gamma * math.pi) / 180)
            if b == -1:
                b = (c * math.sin((betta * math.pi) / 180)) / math.sin((gamma * math.pi) / 180)

            con = sqlite3.connect('project.db')
            # Вносим значения в базу данных
            cur = con.cursor()
            res = cur.execute('''INSERT INTO my(side_a,side_b,side_c,angle_A,angle_B,angle_C,sol)
                                                            VALUES(?, ?, ?, ?, ?, ?, ?)
                                                            ''', (a, b, c, alfa, betta, gamma, sol,)).fetchall()
        else:
            self.label_8.setText("Упс, кажется недостаточно данных. Я не могу решить эту задачу")  # В случае,
        # когда нам даны только один/два параметра или только три угла
        if not (179 < (alfa + betta + gamma) < 181):
            self.label_8.setText('Некорректные данные')
            return
        self.label_8.setText(f'Ответ:a = {a}, b = {b}, c = {c}, alfa = {alfa}, betta = {betta}, gamma = {gamma}')

        if alfa == betta == gamma and (a <= 0 or b <= 0 or c <= 0 or not (a == b == c)):
            self.label_8.setText("Упс, кажется недостаточно данных. Я не могу решить эту задачу")


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('project.ui', self)
        self.pushButton.clicked.connect(self.run)  # Открывает окно "калькулятор"

        self.pushButton_2.clicked.connect(self.history)  # Открывает окно "история решений"

        self.pushButton_3.clicked.connect(self.close_project)  # Закрывает окно

        self.about_window = AboutWindow()  # Открывает вкладку "Помощь" -> "О программе"
        self.action.triggered.connect(self.about)

    def run(self):
        dialog = ClassDialog(self)
        dialog.exec_()

    def history(self):
        dialog = ActionHistory(self)
        dialog.exec_()

    def close_project(self):
        sys.exit(app.exec_())

    def about(self):
        self.about_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
