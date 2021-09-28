# EN:
Patch for Yolo v5s inference with Kneron 720 with Python script. KDPISIConfig Python constructor now formats data correctly to launch net with extra parameters.

To apply patch:
1. Download and unzip host_lib from [here](https://www.kneron.com/developer_center/).</br>
   Install dependencies, more detailed instruction are available [here](http://doc.kneron.com/docs/#720_1.3.0/getting_start_720/).

1. Copy patch to your host_lib directory:
    ```
    cp yolov5s720.patch /path/to/host_lib
1. Enter host_lib directory:
    ```
    cd /path/to/host_lib
1. Initialize git repository and commit everything:
    ```
    git init
    git add .
    git commit
1. Apply patch:
    ```
    git apply --reject --whitespace=fix KDPISIConfig-fix.patch
1. (Optional) Run Python Yolov5s example:
    ```
    cd python
    sudo python3 -t KL720-cam_isi_yolov5s_example
# RU:
Патч для inferenc'а Yolo v5s на Kneron 720 с помощью Python скрипта. Конструктор KDPISIConfig в Python теперь форматирует информацию корректно, что позволяет запускать сети с дополнительными параметрами. 

Чтобы применить патч:
1. Скачайте и распакуйте host_lib [отсюда](https://www.kneron.com/developer_center/).</br>
   Установите зависимости, более подробная инструкция доступно [здесь](http://doc.kneron.com/docs/#720_1.3.0/getting_start_720/).
1. Скопируйте патч в директорию host_lib:
   ```
   cp yolov5s720.patch /path/to/host_lib
1. Войдите в директорию host_lib:
   ```
   cd /path/to/host_lib
1. Инициализируйте git репозиторий и commit'ните всё:
    ```
    git init
    git add .
    git commit
1. Примените патч:
    ```
    git apply --reject --whitespace=fix yolov5s720.patch`
1. (Дополнительно) Запустите пример Yolov5s на Python:
    ```
    cd python
    sudo python3 -t KL720-cam_isi_yolov5s_example
