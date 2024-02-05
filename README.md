# text2packet

#### 介绍
程序用来根据文本文件生成wireshark可以解析的文件, 文本文件从以太网的目的MAC地址开始输入

#### 软件架构
软件架构说明
本软件采用pyqt5, 先用Qtdesigner 生成UI界面,然后解析ui界面生成python代码。在主模块中处理输入的文本，添加pcap头和时间戳,生成output.pcap文件


#### 安装教程

1.  安装python requirement

pip install -r requirements.txt

2. 生成widget.exe 

pyinstaller -F -w -i maple.ico widget.py --noconsole --hidden-import PySide6.QtXml -n text2pcap

#### 使用说明

1.  输入文本文件，参照测试数据 
2.  点击格式文本按钮
3.  点击生成pcap文件按钮
4.  点击打开按钮，可以启用wireshark打开pcap文件

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
