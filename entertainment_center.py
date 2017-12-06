# coding=utf-8
import urllib
import json
import fresh_tomatoes
import media

#解决json编码问题
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def get_video_info():
    '''
    通过请求视频信息的API，获取视频信息的json数据，解析后存入列表中
    :return: 视频信息列表
    '''

    req_homePage = urllib.urlopen("http://118.89.50.76:8888/api/HomeVideo")#请求首页信息API
    video_info_data = json.loads(req_homePage.read())#对JSON数据进行解析

    vidoe_info_list = []# 初始化列表
    for item in video_info_data:#通过循环将JSON中解析出的对象存入列表中
        vidoe_info = media.Movie(item['VideoId'],item['VideoTitle'],item['VideoImageUrl'],get_video_url(item['VideoId']))
        vidoe_info_list.append(vidoe_info)

    return vidoe_info_list

def get_video_url(videoId):
    '''
    该方法通过请求视频API获取视频的URL,并将其返回
    :param videoId: 视频id，用于请求相应视频的URL
    :return: 视频的URL
    '''

    req_video_Url = urllib.urlopen("http://118.89.50.76:8888/api/VideoPlayInfo/"+videoId)# 请求视频URL API
    video_url_data = json.loads(req_video_Url.read())# 对JSON数据进行解析
    return video_url_data[0]['VideoSource']#返回视频URL

def show_page():
    '''
    调用fresh_tomatoes模块创建一个 HTML 文件来可视化视频列表
    :return:null
    '''

    fresh_tomatoes.open_movies_page(get_video_info())#调用open_movies_page函数，传入视频信息列表

#调用show_page()
show_page()



