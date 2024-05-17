cd yolov9
python detect_dual.py \
--img 736 --conf-thres 0.5 --device cpu \
--weights ../best.pt \
--source ../images \
--project ../results \
--save-txt \
--save-conf