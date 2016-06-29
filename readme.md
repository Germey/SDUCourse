## 山东大学刷课系统

### 系统简介

本系统为山东大学选课刷课专用，配置好学号、密码、课程号、课序号即可完成多线程无限刷课，直至选中该课程为止。

本系统基于Python 2.7编写，支持多线程刷课，掉线自动登录，登录失败重试，选中课程即停等功能。

线程数目、登录失败重试次数、超时时间、学号、密码、课程号、课序号均可自定义配置。

### 编写语言

Python 2.7

### 使用方法

#### 1. 安装Python

下载 https://www.python.org/

版本 2.7

#### 2. 安装类库

```
pip install requests pyquery
```

#### 3. 下载代码

````
git clone https://github.com/Germey/SDUCourse.git
````

#### 4. 配置信息

文本编辑器打开 config.py 进行相应配置

USERNAME 学号，PASSWORD 选课密码，KCH 课程号，KXH 课序号

#### 5. 开始刷课

python index.py

### 中止程序

由于启用多线程，所以Ctrl＋C可能无法彻底关闭

#### Windows

可在资源

### 更多配置

#### 线程数目

```
THREAD_NUMBER  #默认为3
```

#### 登录失败重试次数

```
MAX_LOGIN_TIME #默认为3
```

#### 超时时间

```
TIMEOUT #默认30秒
```

### 关于作者

作者崔庆才，山东大学12级，计算机科学与技术学院

个人主页 http://cuiqingcai.com

### 完善项目

如有建议或意见，请在ISSUES中留言，或者尽情PULL REQUESTS，非常感谢。