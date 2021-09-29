from PIL import Image
import pathlib

pics_dir = './pics/'
files = []

# store all filenames in a list
for file in pathlib.Path(pics_dir).iterdir():
	if file.is_file():
		files.append(file.name)

# helper functions
def sorter(item):
	item = int(item.split('.')[0])
	return item

def add_path(item):
	return pics_dir + str(item)

# sorted list of files' path
files = list(map(add_path, sorted(files[1:], key=sorter)))

# save to pdf
images = []

for path in files:
	images.append(Image.open(path).convert('RGB'))

name = input('Enter file name: ')

images[0].save(f'{name}.pdf', save_all=True, append_images=images[1:])

print('done')	
