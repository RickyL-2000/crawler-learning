# -*- encoding=utf8 -*-
__author__ = "RickyLi"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

swipe([510, 1836], [554, 501], duration=0.7)

poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.tencent.karaoke:id/b9c").child("com.tencent.karaoke:id/bzr")[6].click()


