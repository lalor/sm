# 说明

乐岸教育教学项目，使用Supervisor的xml-rpc协议，管理多台服务器上的进程。

# 相关技术

使用Flask + Bootstrap进行开发，用到的Flask插件包括：

* Flask_bootstrap
* Flask_sqlalchemy
* Flask_wtf
* Flask_login

# 运行提示

首先，安装相关依赖

    pip install -r requirements.txt

然后，在`settings.py`中，配置数据库连接信息，配置完成以后，执行以下命令创建相关的表以及管理账号：

    export FLASK_APP=app.py
    flask --help
    flask init_db

最后，运行管理系统：

    flask run -h 0.0.0.0 -p 5000
