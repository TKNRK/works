import sys
import logging
from PIL import Image


# 処理する画像：pth，フレーム数：frames，セーブする場所：sv
# 画像が横にスプライトしている場合に縦に並び替える処理
def v2h(pth, frames, sv):
  im = Image.open(pth)
  im = im.convert("RGBA")
  w = im.size[0]
  h = im.size[1]
  images = []
  for i in range(frames):
    images.append(im.crop((w//frames * (i), 0, w//frames * (i+1), h)))

  canvas = Image.new("RGBA", (h, h*frames), (0, 0, 0, 0))
  for i in range(frames):
    img = images[i]
    canvas.paste(img, (0, h*i))

  canvas.save(sv, quality=100)


# 指定された色のピクセルを透過させる処理
def transp(pth, r, g, b):
	img = Image.open(pth)
	img = img.convert("RGBA")
	trans = Image.new("RGBA", img.size, (0, 0, 0, 0))

	w, h = img.size

	for x in range(w):
	  for y in range(h):
	    pixel = img.getpixel((x, y))
	    if pixel[0] == r and pixel[1] == g and pixel[2] == b:
	      pass
	    else:
	      trans.putpixel((x, y), pixel)

	trans.save("trans.png")


if __name__ == "__main__":
  try:
    pth = sys.argv[1]
    frames = int(sys.argv[2])
    sv = sys.argv[3]
    v2h(pth, frames, sv)
  except:
    logging.error("Usage; python v2h.py [gif path] [num of frames] [save to]")
