# VideoToSMI
Create a smi file based on the video.

- Copyright (c) 2019 Lee Dong-gun
    - Homepage : http://infolab.kunsan.ac.kr
- How to install
    ```bash
    pip install "http://duration.digimoon.net/pip/videotosmi.whl"
    ```
    - other version
        ```bash
        # 0.0.1
        pip install "http://duration.digimoon.net/pip/videotosmi-0.0.1-cp36-none-any.whl"
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