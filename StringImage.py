from PIL import Image
import argparse

# 命令行输入参数处理，详情可见MODULE.MD
parser = argparse.ArgumentParser()
parser.add_argument('file')     # 输入文件
parser.add_argument('-o', '--output')   # 输出文件
parser.add_argument('--width', type=int, default=80)    # 输出字符画宽
parser.add_argument('--height', type=int, default=80)    # 输出字符画高

#获取参数
args = parser.parse_args()

print(args)
input("press any key to continue")

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# 将256灰度映射到70个字符上


def get_char(r, g, b, alpha=256):  # RGBA颜色中，最后ALPHA值为透明度，0代表全透明，1表示不透明
	if alpha == 0:  # 若ALPHA为0则为透明，用空白表示
		return ' '
	length = len(ascii_char)
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 根据当前像素的RGB值返回对应的灰度值
	unit = (256.0 + 1)/length  # 将灰度值按比例对应到列表长度(+1的理由没有明白，测试下不加一结果也一样，怀疑是四舍五入之类的)
	return ascii_char[int(gray/unit)]  # 将灰度值按比例对应为灰度列表中的字符


if __name__ == '__main__':  # 若模块是直接运行的，则执行以下代码块

	im = Image.open(IMG)
	im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

	txt = ""

	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*im.getpixel((j, i)))
			# 如果是在函数调用中，*args表示将可迭代对象扩展为函数的参数列表
			# 例如args = (1,2,3)
			# func = (*args)
			# 等价于函数调用func(1,2,3)
		txt += '\n'

	print(txt)

	# 字符画输出到文件
	if OUTPUT:
		with open(OUTPUT, 'w') as f:
			f.write(txt)
	else:
		with open("output.txt", 'w') as f:
			f.write(txt)
