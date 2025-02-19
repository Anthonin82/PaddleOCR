from paddleocr import PaddleOCR
# https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/ppstructure/table/README.md
table/predict_table.py \
    --det_model_dir=inference/ch_PP-OCRv3_det_infer \
    --rec_model_dir=inference/ch_PP-OCRv3_rec_infer  \
    --table_model_dir=inference/ch_ppstructure_mobile_v2.0_SLANet_infer \
    --rec_char_dict_path=../ppocr/utils/ppocr_keys_v1.txt \
    --table_char_dict_path=../ppocr/utils/dict/table_structure_dict_ch.txt \
    --image_dir=docs/table/table.jpg \
    --output=../output/table