# -*- coding: utf-8 -*-
Time = int(input())

Hours = Time // 3600
Time -= Hours*3600
Minutes = Time // 60
Time -= Minutes*60

print('{}:{}:{}'.format(Hours,Minutes,Time))