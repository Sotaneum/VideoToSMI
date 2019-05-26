from videotosmi import Video

video = Video()
video.add_model('mscoco','maskrcnn','D:/tests/config.json')
filter_ = ['car','bus','truck']

video.detect('D:/tests/4.mov','mscoco',ftr=filter_)