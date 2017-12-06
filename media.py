# coding=utf-8
class Movie():
    def __init__(self,id,title,imageUrl,videoSource):
        '''
        初始化以下信息
        :param id:视频id
        :param title:视频标题
        :param imageUrl:封面图片URL
        :param videoSource:视频URL
        '''
        self.videoId = id
        self.videoTitle = title
        self.videoImageUrl = imageUrl
        self.videoUrl = videoSource