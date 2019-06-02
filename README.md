# VideoToSMI
Create a smi file based on the video.

- Copyright (c) 2019 [InfoLab](http://infolab.kunsan.ac.kr) ([Donggun LEE](http://duration.digimoon.net))
 - How to install
    - requirement
        ```bash
        # python 3.6 -- tensorflow
        pip install tensorflow==1.9.0 exifread>=2.1.2 piexif>=1.1.2 pillow>=6.0.0 matplotlib>=3.1.0 scikit-image>=0.15.0 IPython>=7.5.0 keras>=2.2.4 cython>=0.29.7 deepgeo
        
        # python 3.6 -- tensorflow-gpu
        pip install tensorflow-gpu==1.9.0 exifread>=2.1.2 piexif>=1.1.2 pillow>=6.0.0 matplotlib>=3.1.0 scikit-image>=0.15.0 IPython>=7.5.0 keras>=2.2.4 cython>=0.29.7 deepgeo
        ```
    - install
        ```bash
        pip install VideoToSMI
        ```
    - other version
        ```bash
        # 0.0.1
        pip install VideoToSMI==0.0.1
        ```
- Functions
    ```python
    video = Video()

    # Goto https://github.com/Sotaneum/deepgeo
    def add_model(model_name, lib_name, config_data):
    pass

    # TO SMI
    def detect(file_url, model_name, frame_set, rotation, filter)
    return FILE
    ```
- How to use
    - Import VideoToSMI
        ```python
        from videotosmi import Video
        ```
    - Video To SMI
        ```python
        video = Video()
        video.add_model('mscoco','maskrcnn','d:/config.json')
        filter_ = ['car','bus','truck']
        video.detect('d:/test.mov','mscoco',ftr=filter_)

        # rotation 180
        video.detect('d:/test.mov','mscoco',rotation=180, ftr=filter_)

        #Frame 60
        video.detect('d:/test.mov','mscoco',frame_set=60,rotation=180, ftr=filter_)
        ```
