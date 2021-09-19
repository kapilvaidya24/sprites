import os
list_filename=[]
for filename in os.listdir("mario/"):
    if filename.endswith(".png"): 
        list_filename.append(filename)


from PIL import Image

for file in list_filename:
	file_exact_name="mario/"+file
	try:
		im = Image.open(file_exact_name)
	except IOError:
		print("Error with"+file_exact_name)
		continue	

	fill_color = (255,255,255)  # your new background color

	im = im.convert("RGBA")   # it had mode P after DL it from OP
	if im.mode in ('RGBA', 'LA'):
	    background = Image.new(im.mode[:-1], im.size, fill_color)
	    background.paste(im, im.split()[-1]) # omit transparency
	    im = background

	im.convert("RGB").save(file_exact_name) 