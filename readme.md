## python练习笔记

### python   分支结构

- if   语句语法结构
```
- if 条件表达式：
    事件A
```
&ensp;&ensp;同一个逻辑下   要保持一致的缩进
- 例子1：计算一个数字的绝对值；
- 例子2：计算两个数的大小；
- 例子3：将两个数按照从小到大排序；

**练习题：**
1. 将两个数字按照从大到小的顺序排序；
2. 计算4个数值当照片当中的最大值（MapReduce）；

<<<<<<< HEAD:readme.md

### 二、双分支结构
语法结构：
```
if 条件表达式：
    事件A
else：
    事件B
```
**练习**
1. 计算两个数字当中的较小值
2. 根据成绩判断其对应的两种情况
- 及格：继续努力
- 不及格：请认真复习，准备补考;
  
**Python3 迭代器与生成器**
迭代是访问集合元素的一种方式
迭代器可以记住遍历位置的对象，从第一个元素开始访问，知道所有元素被访问完

迭代器又两个基本的方法：
iter（）和next（）
字符串、列表、或元组对象都可用于创建迭代器
参考例子4.py

**多支结构：**
if - elif - else 结构
逐个对【条件表达式】进行判断
- *红绿灯例子代码*
参考test03.py
- *根据成绩，判断其对应的等级*
    - 小于60分：不及格
    - 介于60到90：良好
    - 大于90：优秀
参考test04.py

**编写一个程序**
根据年龄判断其所处的阶段：
- 小于18岁：青少年儿童
- 18-60岁：成年人
- 大于60岁：老年人
参考test05.py


**内联if（if表达式或条件函数或条件语句）**
```
基本语法：
值1 if 条件 else 值2
条件为真，返回值1；反之，返回值2
```
参考test06.py

**分支结构--条件语句**
条件语句常用的是比较运算符（关系运算符，大于，小于等）
逻辑运算符（布尔值，或与非）
逻辑与：
and
参考test07.py
逻辑或：
or
参考test08.py
逻辑非：
not
参考test09.py

**练习题：**
1. 面试成绩、笔试成绩都大于60分，可以进入复试；否则，没有资格进入复试；
2. 面试成绩、笔试成绩任意一个科目小于60分，没有资格进入复试；否则进入复试；
参看xiti01.py

*案例：门票价格*
参考代码case01.py
*案例2：已知坐标(x,y)，判断其所在的象限*
参看代码case02.py

### 二、循环
**for-in循环**
```
语法结构：
for 变量 in 集合：
    具体操作
```
1. **遍历列表**
for-in循环用enumerate遍历列表及索引
 *遍历字典*
 三个方法
-  items():返回字典内的key-value对
 - keys():返回字典内的所有key列表
- values()：返回字典中所有value列表
 参看：xunhuan01.py

**练习：**
构造一个列表，其由正数、负数、零构成。
将其中的正数输出。
参看：for-in-test01.py

2. **for-in次数控制**
    1. 语法结构
       1. 语法规则
        ```
        range （初始值，终止值，步长）
        ```
    
    2. range函数
        生成数字列表
        可以指定：初始值、终止值、步长
        
    3. 循环
        参考例子ex2.2.1.py

**练习**
&ensp;&ensp;&ensp;1. 计算1到100的和；
&ensp;&ensp;&ensp;2.输出1-100内的所有奇数；
&ensp;&ensp;&ensp;3.将1到100以内，所有被7整除的数输出；
参考test2.2.1.py

3. **while 循环**
    1. 语法结构
        ```
        语法规则：
        while 条件表达式：
            循环体
        while循环：
        条件为真时，运行循环体
        需要注意的是：最后要让【条件表达式】不成立 
        ```
      
    2. 数值案例
          增值、减值案例；参考ex3.1.py
    3. 空值案例
        参考ex3.1.py

**练习**
&ensp;&ensp;&ensp;将1到100以内的所有被7整除的数输出。（使用while）

- 方式A：通过空值初始值和循环变量的方式；
- 方式B：通过循环结构嵌套的方式：
  


4. **while 遍历**
#### 练习
**计算一个列表内：**
- 奇数的个数
- 偶数的个数
- 参考ex4.py

5. 跳出循环break
   ```
   语法规则：
   循环（while或for-in）
        if 条件表达式：
            break
   ```
   break语句结束循环，完全结束一个循环，跳出循环体
   核心要义：就是不需要完成整个循环
   ### 练习 
   使用break，判断一个列表内，是否存在奇数。
   参考ex5.py

6. 跳出循环continue
   ```
   循环（while或for-in）
        if 条件表达式：
            continue
   ```
   continue：结束循环，忽略当次循环的剩下语句，从下次执行
   核心要义：本次循环的后续不执行了，从下一轮继续开始执行。
   参考ex6.py

# 三、函数
函数是封装好的，可重复使用的，用来实现单一，或相关联功能的代码段。

函数能提高程序的模块性，和代码的重复利用率。你已经知道 Python 提供了许多内建函数，比如 print()。但你也可以自己创建函数，这被叫做用户自定义函数。

---
## 定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：

- 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
- 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号起始，并且缩进。
- Return[expression] 结束函数，选择性地返回一个值给调用方。不带表达式的 return 相当于返回 None。

---
#### 1. 内置函数
常用的内置函数：
input();format();等

list();set();tuple();dict()是将可迭代的对象转化成列表、集合、元组、字典等

#### 2. 自定义函数
语法规则：
```
def 函数名（参数）：
    函数体
    【return 返回值】
```
自定义函数：使用def定义，使用时，调用方法与内置函数一致
例子3.2.1 根据半径，计算圆的面积。
######  练习
根据正方形的边长，计算面积。

（参考ex3.2.1.py）
#### 3. 函数进阶
1. 局部函数
   在函数内部定义的函数 
2. 匿名函数
   - 定义
      - 变量名=lambda 参数：表达式（block）
      - 参数：可选，通常以逗号分隔的变量表达式形式，也就是位置参数表达式：不能包含循环、return，可以使用if。。。else。。。
    - 使用
      - max(key=lambda)
      - sort(key=lambda)
    - 注意：
       - 1. 表达式中不能包含循环、return
       - 2. 可以包含if...else...语句（三元表达式）
       - 3. 表达式计算结果直接返回

#### 4. 函数作用域
