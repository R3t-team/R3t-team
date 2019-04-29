# @author: heyanlll

进入游戏后跟npc对话，意思很明确，打败怪物后可以得到flag

![](http://ww1.sinaimg.cn/large/005Z7H2Aly1g2jogcnwnsj30hu0e3di8.jpg)

然后探索房间，左上是卖道具和武器，右上是木桩打了可以升级加经验，左下是boss房，右下没有用处。开始的思路是利用内存修改器将人物的等级、金币调慢，然后打boss。

![](
    http://ww1.sinaimg.cn/large/005Z7H2Aly1g2jogx0bcnj30hu0e3agn.jpg
)

不出所料被秒，顶级装备和满级打到boss身上都是0伤害。只有一瓶药剂能打boss100血，但显然是不能磨死。改变思路，存档后发现文件类型是rxdata，data文件夹里的各种属性文件也都是rxdata，根据自己玩rpg的经验，可以修改存档进行作弊。

![](http://ww4.sinaimg.cn/large/005Z7H2Aly1g2johqbtkmj30cz0a9dhm.jpg)

```
工具下载地址：

http://www.pc6.com/softview/SoftView_55599.html
```
![](http://ww1.sinaimg.cn/large/005Z7H2Aly1g2joiuxvsfj30hu0e3q3w.jpg
)

进入房间后来到第二关，根据提示，要开宝箱的门。一共9个门，其中2-1 2-3是打不开的，3-3 是bad bad door。 其他的门开启需要一定的顺序，不断尝试即可，但要注意不要碰到吸血鬼和bad bad door

![](
    http://ww2.sinaimg.cn/large/005Z7H2Aly1g2joka6lxej30hu0e3mxq.jpg
)

每个宝箱对应一个数字，开启六个门后，发现隐藏门，根据提示将数字组合后提交其md
5即为flag
