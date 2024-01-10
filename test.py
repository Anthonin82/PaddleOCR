from paddleocr import PaddleOCR



from paddleocr import PaddleOCR,draw_ocr
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
# Predict table image
tools/infer_table.py -c configs/table/SLANet.yml -o Global.pretrained_model={path/to/weights}/best_accuracy  Global.infer_img=ppstructure/docs/table/table.jpg
