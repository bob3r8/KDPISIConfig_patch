# DEPRECIATED DUE HOST_LIB DEPRECIATION

# EN
Patch for Kneron's host_lib. I faced issues launching networks by start_isi_mode_ext from kdp_wrapper.py. That was because of incorrect ISI configuration. KDPISIConfig Python constructor with this patch formats data correctly to launch net with extra parameters, but now you have to specify variables types:</br>
`f` - for float</br>
`H` - for unsigned int16</br>
`h` - for signed int16</br>
`I` - for unsigned int32</br>
`i` - for signed int32</br>

To apply patch:
1. Download and unzip host_lib from [here](https://www.kneron.com/developer_center/).</br>
   Install dependencies, more detailed instruction are available [here](http://doc.kneron.com/docs/#720_1.3.0/getting_start_720/).

1. Copy patch to your host_lib directory:
    ```
    cp KDPISIConfig-fix.patch /path/to/host_lib
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
 
# УСТАРЕЛО ПО ПРИЧИНЕ УСТАРЕВАНИЯ HOST_LIB

# RU
Патч для host_lib Kneron'а. Я встретился с проблемами при запуске сетей с помощью функции start_isi_mode_ext из kdp_wrapper.py. Это было из-за неправильной конфигурации для ISI. Конструктор KDPISIConfig в Python теперь форматирует информацию корректно, что позволяет запускать сети с дополнительными параметрами, однако теперь необходимо указывать типы переменных:</br>
`f` - для float</br>
`H` - для unsigned int16</br>
`h` - для signed int16</br>
`I` - для unsigned int32</br>
`i` - для signed int32</br>

Чтобы применить патч:
1. Скачайте и распакуйте host_lib [отсюда](https://www.kneron.com/developer_center/).</br>
   Установите зависимости, более подробная инструкция доступно [здесь](http://doc.kneron.com/docs/#720_1.3.0/getting_start_720/).
1. Скопируйте патч в директорию host_lib:
   ```
   cp KDPISIConfig-fix.patch /path/to/host_lib
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
    git apply --reject --whitespace=fix  KDPISIConfig-fix.patch`
1. (Дополнительно) Запустите пример Yolov5s на Python:
    ```
    cd python
    sudo python3 -t KL720-cam_isi_yolov5s_example
