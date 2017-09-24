<center><h1>学习笔记之Git篇</h1></center>


####在之前如果有人问我Git时什么？我会回答他说 l do not know!因为是真不知道，就是现在你问我Git是什么？答：Git是目前世界上最先进的分布式版本控制系统，再多就不知道了。起初的学习对于我来说还是挺困难的，也走了挺多的误区，就是一个简单的创建本地仓库然后上传到远程GitHub也废了很大的功夫和时间，也就做了一些乱七八糟的笔记，最后老哥说这几天你学的东西整理总结一下写一个Markdown文档也是对自己的学的一小点东西的知识做一个回顾，我不会写，因为以前没写过，所以就有了这些罗里吧嗦的东西，以后万一成大神以后看到这些也就知道我此时写的这些有点乱的东西是怎么想的了。


##1. 安装Git：
   + 这个其实挺简单的在Git官网上下载对应版本的Git Windows软件 点击安装 全部都是默认选项一直到安装完成。
##2. 准备Git的初始化：
   1. 首先通过下面的的命令查看Git的版本信息
      + `git -version`
   2.  配置姓名 邮箱账号，因为Git是分布式版本控制系统，所以，每个机器都必须自报家门：你的名字和Email地址 
      + ` git config --giobal user.name "511717123out" `
      + ` git config --giobal user.email "511717123@qq.com" `
      + 注意`git config`命令的--`global`参数，用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置，**当然也可以对某个仓库指定不同的用户名和Email地址**\(这个命令我没用过\)
    1. 也可以开启颜色显示
       + ` git config --global color.ui true`
##3. 创建仓库，就是版本库，英文名repository，可以简单理解成一个目录，这个目录里面的所有文件都可以被Git管理起来，每个文件的修改、删除，Git都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻可以还原
    1. 选择一个合适的地方，创建一个空目录 随便一个哪个盘都可以 目录名字最好不要使用中文
       + `mkdir e:/Pytnon`创建目录
       + `cd c:/Python`进入这个目录
       + `pwd`显示Python这个目录并进入这个目录
    2. 通过`git init`这个命令把这个目录变成Git可以管理的创库
       + `git init`
       + 目录下多了一个.git的目录，这个目录是Git来跟踪管理版本库的，没事千万不要手动修改这个目录里面的文件，不然改乱了，就把Git仓库给破坏了
    3. 在Python目录下创建一个文件并提交到暂存区
       1. 添加指定文件到暂存区
          + `git add 文件名`
       2. 添加指定目录到暂存区
          + `git add 目录名`
       3. 添加当前目录下所有文件到暂存区
          + `git add .`后面有一个点
    4. 提交暂存区到仓库
       1. 提交暂存区到仓库
          + `git commit -m "提交说明"`
       2. 提交暂存区指定文件到仓库
          + `git commit 文件名 -m "提交说明"`
##4. 添加远程仓库
    1. 在GitHub网站上注册一个账号
    2. 使用默认的`Git ssh协议`使用ssh协议前要先在本地生成公钥\(Public\)和私钥\(Private\)
       1. 检查本地是否有秘钥
          + `ls -al ~/.ssh`
       2. 有的话把 .ssh文件夹下id_rsa文件用文本浏览器打开把里面的内容复制到GitHub中，没有的话就生成一个新的秘钥
          + `ssh-keygen -t rsa -C "511717123@qq.com"`
          + 密匙位置默认 使用默认值 不设置密码
       3. 登陆 GitHub，打开“Account settings”，“SSH Keys”页面：然后，点“Add SSH Key”，填上任意 Title，在 Key 文本框里粘贴id_rsa.pub文件的内容
    3. 在GitHub上创建一个创库 然后关联远程创库
       1. 关联远程仓库
          + `git remote add origin git@github.com:511717out/Python-project-library.git`
          + 511717out账户名，Python-project-library.git仓库名
          + 添加后，远程库的名字就是origin，这是Git默认的叫法，也可以改成别的，但是origin这个名字一看就知道是远程库
##5. 把本地仓库提交到远程仓库
        1. 提交timetable.md文件到暂存区
           + `git add timetable.md`
        2. 提交到本地仓库
           + `git commit -m "cmd submit timetable"`
        3. 提交本地master分支到远程创库  master 是默认分支
           + `git push -u origin master`
##6. 和远程仓库同步
    1. 把远程Python-project-library仓库克隆到本地
       + `git clone git@github.com:511717out/Python-project-library.git `
    2. 下载远程仓库的所有变动
       + `git fetch [remote]`
    3.  显示所有远程仓库
       + `git remote -v`
    4.  显示某个远程仓库的信息
       + `git remote show [remote` 
    5.  增加一个新的远程仓库，并命名
       + `git remote add [名字] [url]`
    6.  取回远程仓库的变化，并与本地分支合并
       + `git pull [remote] [branch]`
    7.  上传本地指定分支到远程仓库
       + `上传本地指定分支到远程仓库`
    8.  强行推送当前分支到远程仓库，即使有冲突
       + `git push [remote] --force`
    9.  推送所有分支到远程仓库
       + `git push [remote] --all`
##7. 后悔药
    1. 恢复暂存区的指定文件到工作区
       + `git checkout [file]`
    2. 恢复某个commit的指定文件到暂存区和工作区
       + `git checkout [commit] [file]`
    3. 恢复暂存区的所有文件到工作区
       + `git checkout .`注意后面的点



<center><h3>未完后续待学习</h3></center>