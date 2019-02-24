from font_img.font_img_opt import FontImgOpt
from img_char.img_char_opt import ImgCharOpt
from img_feature.img_feature_opt import ImgFeatureOpt
from PIL import Image
import numpy as np


class FifcOpt():
    def __init__(self):
        self.__img_char_opt = ImgCharOpt(
            "./font_img/image/", "./img_char/image_save_dict/")
        self.__img_feat_opt = ImgFeatureOpt(
            "./img_feature/weight/char_feature.hdf5")

    def img2char(self, img):
        char = self.__img_char_opt.image2char(img)
        return char

    def char2img(self, char):
        img = self.__img_char_opt.char2image(char)
        return img

    def feat2img(self, feat):
        img = self.__img_feat_opt.feature2img(feat)
        return img

    def img2feat(self, img):
        feat = self.__img_feat_opt.img2feature(img)
        return feat

    def char2feat(self, char):
        img = self.char2img(char)
        feat = self.img2feat(img)
        return feat

    def feat2char(self, feat):
        img = self.feat2img(feat)
        char = self.img2char(img)
        return char


def img_open(filepath):
    img = Image.open(filepath)
    img = img.convert("RGB")
    img = img.resize((28, 28))
    img = np.array(img)
    return img


def main():
    fifc_opt = FifcOpt()
    img_path = "./font_img/image/e98080_0.png"
    img = img_open(img_path)

    # img char img
    char = fifc_opt.img2char(img)
    print(char)
    # char = "退"

    # img feat char
    # feat = fifc_opt.img2feat(img)
    # img = fifc_opt.feat2img(feat)
    # char = fifc_opt.img2char(img)

    # char img char
    char = "退"
    img = fifc_opt.char2img(char)
    char = fifc_opt.img2char(img)
    print(char)


if __name__ == "__main__":
    main()