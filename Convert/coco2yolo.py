import os
import json
 
 
class BDD_to_YOLOv5:
    def __init__(self, read_path, write_path, width_ratio, height_ratio, category, category_nums):
        self.read_path = read_path
        self.writepath = write_path
        self.bdd100k_width_ratio = width_ratio
        self.bdd100k_height_ratio = height_ratio
        self.select_categorys = category
        self.categorys_nums = category_nums
 
    def bdd_to_yolov5(self, path):
        lines = ""
        with open(path) as fp:
            j = json.load(fp)
            write = open(os.path.join(self.writepath, "%s.txt" % j["name"]), 'w')
            for fr in j["frames"]:
                for objs in fr["objects"]:
                    if objs["category"] in self.select_categorys:
                        temp_category = objs["category"]
                        if (temp_category == "traffic light"):
                            color = objs["attributes"]["trafficLightColor"]
                            temp_category = "tl_" + color
                        idx = self.categorys_nums[temp_category]
                        cx = (objs["box2d"]["x1"] + objs["box2d"]["x2"]) / 2.0
                        cy = (objs["box2d"]["y1"] + objs["box2d"]["y2"]) / 2.0
                        w = objs["box2d"]["x2"] - objs["box2d"]["x1"]
                        h = objs["box2d"]["y2"] - objs["box2d"]["y1"]
                        if w <= 0 or h <= 0:
                            continue
 
                        # 根据图片尺寸进行归一化
                        cx, cy, w, h = cx * self.bdd100k_width_ratio, cy * self.bdd100k_height_ratio, w * self.bdd100k_width_ratio, h * self.bdd100k_height_ratio
                        line = f"{idx} {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}\n"
                        lines += line
                if len(lines) != 0:
                    write.writelines(lines)
                    write.close()
                    print("%s has been dealt!" % j["name"])
 
 
if __name__ == "__main__":
    bdd_labels_dir = "E:/1zhuoying/coco_dataset/jsontotxt/json"# json存储的文件目录
    write_path = "E:/1zhuoying/coco_dataset/jsontotxt/txt" # txt存储目录
    width_ratio = 1.0 / 1920
    height_ratio = 1.0 / 1080
    categorys = ["1", "2", "3", "4", "5", "6"]  ##改成自己数据集类别
    categorys_nums = {#改成自己数据集类别
        "1": 0,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "G": 5,

    }
    fileList = os.listdir(bdd_labels_dir)
    yolo_v5 = BDD_to_YOLOv5(bdd_labels_dir, write_path, width_ratio, height_ratio, categorys, categorys_nums)
    for path in fileList:
        filepath = os.path.join(yolo_v5.read_path, path)
        yolo_v5.bdd_to_yolov5(filepath)
