from common import constants, kdp_wrapper
import kdp_host_api as api
import time
import ctypes
import sys

VIDEO_SOURCE = 0


def yolo_v5s_detection(device_index):
    app_id = constants.AppID.APP_CENTER_APP.value
    kdp_wrapper.isi_load_nef(device_index, '../input_models/KL720/kl720_yolov5s/models_720.nef', app_id)
    model_id = 211
    res_buf_size = 2048
    image_source_w = 640
    image_source_h = 480
    ext_param = [0.15, 0.45, 20, 3, 6, 3, 0,
                 # anchors[3][6]
                 10, 13, 16, 30, 33, 23,
                 30, 61, 62, 45, 59, 119,
                 116, 90, 156, 198, 373, 326,
                 # strides[3]
                 8, 16, 32,
                 ]
    ext_param_types = ['f', 'f', 'I', 'H', 'H', 'H', 'H']
    image_format = constants.IMAGE_FORMAT_SUB128 | constants.NPU_FORMAT_RGB565 | constants.IMAGE_FORMAT_CHANGE_ASPECT_RATIO
    isi_configuration = constants.KDPISIConfig(app_id, res_buf_size, image_source_w, image_source_h, image_format, ext_param, ext_param_types)
    cfg_size = sys.getsizeof(isi_configuration)
    image_buf_size = kdp_wrapper.start_isi_mode_ext(device_index, isi_configuration, cfg_size)

    if image_buf_size < 3:
        print(f"ISI mode window {image_buf_size} too small...\n")
        return -1
    print(f"\nConfig model {model_id}...\n")
    ret = kdp_wrapper.isi_config(device_index, model_id, 0)
    if ret:
        print(f"ISI config returned {ret}\n")
        return -1

    capture = kdp_wrapper.setup_capture(VIDEO_SOURCE, image_source_w, image_source_h)

    img_id_tx = 1
    img_id_rx = img_id_tx
    buf_len = image_source_w * image_source_h * 2
    t_all = time.time()
    while True:
        t = time.time()
        frames = []
        error_code = ctypes.c_uint32(0)
        img_buf_left = ctypes.c_uint32(0)
        img_buf = kdp_wrapper.isi_capture_frame(capture, frames)
        ret = api.kdp_isi_inference(device_index, img_buf, buf_len, img_id_tx,
                                    ctypes.byref(error_code), ctypes.byref(img_buf_left))
        if ret:
            print(f"kdp_isi_inference returned: {ret}")
            return -1
        img_id_tx += 1

        r_data = (ctypes.c_char * 2048)()
        rsp_code = ctypes.c_uint32(0)
        r_size = ctypes.c_uint32(0)
        ret = api.kdp_isi_retrieve_res(device_index, img_id_rx, ctypes.byref(rsp_code), ctypes.byref(r_size), r_data)
        if ret:
            print(f"kdp_isi_retrieve_res returned: {ret}")
            return -1
        img_id_rx += 1

        od_header_res = kdp_wrapper.cast_and_get(r_data, constants.YoloResult)
        box_result = kdp_wrapper.cast_and_get(od_header_res.boxes, constants.BoundingBox * od_header_res.box_count)[
                     :od_header_res.box_count]
        dets = [[b.x1, b.y1, b.x2, b.y2, b.score, b.class_num] for b in box_result]
        kdp_wrapper.draw_capture_result(device_index, dets, frames, 'yolo')

        print('\rFPS: {:.2f}, AVG: {:.2f}'.format(1/(time.time() - t), img_id_tx/(time.time() - t_all)), end='')


def user_test(device_index, _user_id):
    ret = yolo_v5s_detection(device_index)
    kdp_wrapper.end_det(device_index)
    return ret
