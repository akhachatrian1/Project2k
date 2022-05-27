## подключение
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

## минимальный пример графика:
x = np.linspace(0,1 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots() # Создает новую figure и заполняет ее сеткой axes
ax.plot(x, y)
plt.show()

## визуализация с помощью pyplot:
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel('some numbers')
plt.show()

## форматирование стиля
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

## равномерно дискретизированное время с интервалом 200 мс
t = np.arange(0., 5., 0.2)

## красные тире, синие квадраты и зеленые треугольники
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

## построение графиков со строками ключевых слов
data = {'a': np.arange(50),
        'c': np.random.randint(0,50,50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('запись a')
plt.ylabel('запись b')
plt.show()

## построение графиков с категориальными переменными
names = ['group_a', 'group_b', 'group_c']
values = [1,10,100]
plt.figure(figsize=(9,3))
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Категориальное построение графика')
plt.show()

# Cпособы установки свойств строки
# аргументы ключевых слов:
plt.plot(x, y, linewidth=2.0)
# методы сеттера Line: line1, line2 = plot(x1, y1, x2, y2)
line, = plt.plot(x, y, '-')
line.set_antialiased(False) # отключить сглаживание
line.set_animated(True)
line.set_marker(',')
# setp
lines = plt.plot(1, 5, 1, 60)
plt.setp(lines, color='g', linewidth=1.5)
plt.setp(lines, 'color', 'g', 'linewidth', 1.5)

## функция gca возвращает текущие оси (matplotlib.axes.Axes)
# функция gcf возвращает текущую фигуру (matplotlib.figure.Figure)
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

# несколько фигур, используя несколько figure вызовов с увеличивающимся номером фигуры
plt.figure(1)                # первый рисунок
plt.subplot(211)             # первый подзаголовок на первом рисунке
plt.plot([1,2,3  ])
plt.subplot(212)             # второй подзаголовок на первом рисунке
plt.plot([4,5,6  ])
plt.figure(2)                # вторая фигура
plt.plot([4,5,6  ])          # создает subplot() по умолчанию
plt.figure(1)                # рисунок 1 текущий; subplot(212) все еще актуален
plt.subplot(211)             # сделать подзаголовок(211) в текущем рисунке 1
plt.title('Easy as 1, 2, 3')
# очистить текущую фигуру clfи текущие оси cla
# явное закрытие close

# Работа с текстом
# text может использоваться для добавления текста в произвольном месте; xlabel, ylabel, title - в определенном месте
mu, sigma = 100,15
x = mu + sigma * np.random.randn(10000)
# гистограмма данных
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.show()

# Логарифмические и нелинейные оси координат
# Фиксация случайного состояния для воспроизводимости
np.random.seed(19680801)
# составление некоторых данных в открытом интервале (0, 1)
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))
# график с различными масштабами осей
plt.figure()
# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)
# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)
# symmetric log
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.01)
plt.title('symlog')
plt.grid(True)
# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# регулировка
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
plt.show()


### Визуализация диаграмм
plt.close("all")
ts = pd.Series(np.random.randn(1000), index = pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot();
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))
df = df.cumsum()
plt.figure()
df.plot();

# зависимость одного столбца от другого, используя ключевые слова x и y в plot():
df3 = pd.DataFrame(np.random.randn(1000, 2),
 columns=["B", "C"]).cumsum()
df3["A"] = pd.Series(list(range(len(df))))
df3.plot(x="A", y="B");

# гистограмму (тип bar) можно создать следующим образом:
plt.figure();
df.iloc[5].plot(kind="bar");

# Для помеченных данных, не относящихся к временным рядам, вы можете создать гистограмму:
plt.figure();
df.iloc[5].plot.bar();
plt.axhline(0, color="k");

# Вызов метода DataFrame’s plot.bar() создает несколько bar-графиков:
df2 = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])
df2.plot.bar();

# Чтобы создать столбчатую диаграмму, stacked=True:
df2.plot.bar(stacked=True);

# Чтобы получить горизонтальные полосы, метод barh
df2.plot.barh(stacked=True);

# Гистограммы можно нарисовать с помощью методов DataFrame.plot.hist() и Series.plot.hist().
df4 = pd.DataFrame(
{
"a": np.random.randn(1000) + 1,
"b": np.random.randn(1000),
"c": np.random.randn(1000) - 1,
},
columns=["a", "b", "c"],
)
plt.figure();
df4.plot.hist(alpha=0.5);

# Гистограмму можно сложить в стопку, stacked=True.
# Размер ячейки можно изменить с помощью ключевого слова bins.
plt.figure();
df4.plot.hist(stacked=True, bins=20);

# горизонтальные и кумулятивные гистограммы с помощью orientation='horizontal' and cumulative=True.
plt.figure();
df4["a"].plot.hist(orientation="horizontal", cumulative=True);

# Построение гистограмм, интерфейс DataFrame.hist
plt.figure();
df["A"].diff().hist();

# DataFrame.hist() выводит гистограммы столбцов в отдельные окна subplots.figure();
df.diff().hist(color="k", alpha=0.5, bins=50);

# Box plots
# задаем цвета, передавая словарь с ключами  boxes, whiskers, medians and caps (если ключа нет, то цвет по умолчанию); sym - стиль отдельных точек
df = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C","D", "E"])
df.plot.box();
color = { "boxes": "DarkGreen", "whiskers": "DarkOrange", "medians": "DarkBlue", "caps": "Gray",}
df.plot.box(color=color, sym="r+");
#  горизонтальная и произвольно расположенная прямоугольная диаграмма с помощью vert=False и positions
df.plot.box(vert=False, positions=[1, 4, 5, 6, 8]);

# Построение, интерфейс DataFrame.boxplot
df = pd.DataFrame(np.random.rand(10, 5))
plt.figure();
bp = df.boxplot()

#  стратифицированный boxplot, используя by для группировки
df = pd.DataFrame(np.random.rand(10, 2), columns=["Col1", "Col2"])
df["X"] = pd.Series(["A","A","A","A","A", "B","B","B","B","B"])
plt.figure();
bp = df.boxplot(by="X")

# подмножество столбцов для рисования, а также сгруппировка столбцов
df = pd.DataFrame(np.random.rand(10, 3), columns=["Col1", "Col2", "Col3"])
df["X"] = pd.Series(["A", "A", "A", "A", "A", "B", "B", "B", "B", "B"])
df["Y"] = pd.Series(["A", "B", "A", "B", "A", "B", "A", "B", "A", "B"])
plt.figure();
bp = df.boxplot(column=["Col1", "Col2"], by=["X", "Y"])

# Area plot (график с закрашенной областью)
df = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])
df.plot.area();
df.plot.area(stacked=False); # stacked - прозрачность

#  Scatter plot (Точечная диаграмма)
df = pd.DataFrame(np.random.rand(50, 4), columns=["a", "b", "c", "d"])
df.plot.scatter(x="a", y="b");
ax = df.plot.scatter(x="a", y="b", color="DarkBlue", label="Group 1")
df.plot.scatter(x="c", y="d", color="DarkGreen", label="Group 2", ax=ax);
# Можно задать столбец цветов для каждой точки:
df.plot.scatter(x="a", y="b", c="c", s=50);
# Для каждой точки можно задать свой размер
df.plot.scatter(x="a", y="b", s=df["c"] * 200);

# Шестиугольники (Hexagonal bin plot)
df = pd.DataFrame(np.random.randn(1000, 2), columns=["a", "b"])
df["b"] = df["b"] + np.arange(1000)
df.plot.hexbin(x="a", y="b", gridsize=25);

# Круговой график (Pie plot)
series = pd.Series(3 * np.random.rand(4), index=["a", "b", "c", "d"], name="series")
series.plot.pie(figsize=(6, 6));

# График матрицы рассеяния (Scatter matrix plot)
from pandas.plotting import scatter_matrix
df = pd.DataFrame(np.random.randn(1000, 4), columns=["a", "b", "c", "d"])
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal="kde");

# График плотности (Density plot)
ser = pd.Series(np.random.randn(1000))
ser.plot.kde();

# Производительность
# Упрощение сегмента линии
# Изображение данных без упрощений и с упрощениями
y = np.random.rand(100000)
y[50000:] *= 2
y[np.geomspace(10, 50000, 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['path.simplify_threshold'] = 0.0
plt.plot(y)
plt.show()

mpl.rcParams['path.simplify_threshold'] = 1.0
plt.plot(y)
plt.show()

# Упрощение маркеров
x = np.linspace(0,1 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots() 
ax.plot(x, y)
plt.plot(x, y, markevery=10)
plt.show()

# Разделение линий на более мелкие куски
mpl.rcParams['path.simplify_threshold'] = 1.0

y = np.random.rand(100000)
y[50000:] *= 2
y[np.geomspace(10, 50000, 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['agg.path.chunksize'] = 0
plt.plot(y)
plt.show()

mpl.rcParams['agg.path.chunksize'] = 10000
plt.plot(y)
plt.show()







