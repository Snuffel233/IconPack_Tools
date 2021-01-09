# What is this?

这是一个用Python编写的，简单的图标包适配小工具，它可以通过以包名命名的图标自动转化为图标包开发所需的格式并生成` appfilter.xml `和` drawable.xml`

# How to use?

请确保安装Python3并且已经将其加入path

## 导入资源

将图标资源放入addAPPinfo/input双击运行` add.py`即可自动执行

## 获取资源包

addAPPinfo/resources内的文件即为资源文件，目前已经适配了超两千个包名，如果还是不够，可以尝试自行获取

首先，将appfilter信息完整化，例如

```xml
<!-- 百度网盘 -->
<item component="ComponentInfo{com.baidu.netdisk/com.baidu.netdisk.ui.DefaultMainActivity}" drawable="百度网盘" />
<!-- 菜鸟 -->
<item component="ComponentInfo{com.cainiao.wireless/com.cainiao.wireless.homepage.view.activity.WelcomeActivity}" drawable="菜鸟" />
<!-- 虫洞 -->
<item component="ComponentInfo{com.viper.wormhole/com.chaozhuo.gameassistant.SplashActivity}" drawable="虫洞" />
<!-- 钉钉 -->
<item component="ComponentInfo{com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity}" drawable="钉钉" />
```

将上面部分改为

```xml
<?xml version="1.0" encoding="UTF-8"?>
<resources>
	<item component="ComponentInfo{com.baidu.netdisk/com.baidu.netdisk.ui.DefaultMainActivity}" drawable="百度网盘" />
	<item component="ComponentInfo{com.cainiao.wireless/com.cainiao.wireless.homepage.view.activity.WelcomeActivity}" drawable="菜鸟" />
	<item component="ComponentInfo{com.viper.wormhole/com.chaozhuo.gameassistant.SplashActivity}" drawable="虫洞" />
	<item component="ComponentInfo{com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity}" drawable="钉钉" />
</resources>
```

并命名为input.xml放入inputAPPinfo/input，双击运行input.py，然后将output内生成的文件放入addAPPinfo/resources即可完成资源库补充

## 系统软件

我们把诸如电话短信等这种几乎每个手机都有的软件独立归纳，只需要修改几个文件的文件名即可完成全部适配

覆盖内容如下

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
		<category title="系统" />
    <item drawable="market" name="应用商店" />
    <item drawable="browser" name="浏览器"  />
    <item drawable="calculator" name="计算器" />
    <item drawable="calendar" name="日历" />
    <item drawable="camera" name="相机" />
    <item drawable="clock" name="时钟" />
    <item drawable="compass" name="指南针" />
    <item drawable="contacts" name="联系人" />
    <item drawable="downloads" name="下载" />
    <item drawable="email" name="邮件" />
    <item drawable="files" name="文件管理" />
    <item drawable="fm" name="FM收音机" />
    <item drawable="gallery" name="相册" />
    <item drawable="health" name="健康" />
    <item drawable="music" name="音乐" />
    <item drawable="cellphone" name="电话" />
    <item drawable="security" name="安全中心" />
    <item drawable="settings" name="设置" />
    <item drawable="sms" name="短信" />
    <item drawable="sound_recorder" name="录音机" />
    <item drawable="weather" name="天气" />
    <item drawable="wallet" name="钱包" />
    <item drawable="feedback" name="用户反馈" />
    <item drawable="theme" name="主题" />
    <item drawable="voiceassistant" name="语音助手" />
</resources>
```

drawable标签内对应图标命名方式，name标签内对应系统应用类别

### 使用方法

首先，打开system/system.xml将里面所有内容复制到图标包工程appfilter.xml内，将上面所有内容复制到drawable.xml内即可

# Warning⚠️

使用本工具前，请确保你有使用Android Studio开发图标包的基础知识，因为How to use？内全部内容建立在此之上，下面推荐几个大佬写的图标包开源程序

- AndIconPack：https://github.com/hujincan/AndIconpack
- NanoIconPack：https://github.com/by-syk/NanoIconPack

# 开源协议

本项目遵循MIT协议开源

# Others

本人Python初学者，代码水平下水道，欢迎各位大佬指点

如果本项目对你有用，不妨点下Star？