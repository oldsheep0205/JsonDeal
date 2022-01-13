# JsonDeal
a mod processor for Tale of Immortal
欢迎使用鬼谷八荒json修改器 v 2.5.2！
功能：
1. 批量修改id
2. 批量添加新键值--未完成
3.修改所有给定键的值--未完成
4.  一键适配mod至最新版本

教程：

忠告：json是不允许有注释的，虽然可以识别但不是所有的程序都能识别！
忠告：json文件的结尾是不允许有逗号的，除了我的程序其他的默认程序均不能识别！


1. 将批量处理器放到vallain目录下，与base文件夹和patch_文件夹同级
2. 打开程序

---------
一，修改json内id相关的东西（注意，不仅是id，若是dramadialogue等有上下关联的数字也一样会修改）

1. 输入要修改的json文件
2. 选择功能（目前只有1可用）
3. 属于想要的id， 回车
4. 得到成品，在目录下的output文件夹中

---------
二，适配游戏版本
前提1：必须有vallain，且base中的json文件必须是最新版的
前提2，这个mod所在的patch必须与base文件在同一文件夹。换句话说，将你的patch文件夹放到vallain文件夹下面即可顺利运行

1. 选适配mod，回车
2. 成品在output文件夹下面的update文件夹下面的patch，将其内的json拉出来到覆盖掉就行了

