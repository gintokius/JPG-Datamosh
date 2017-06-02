import io
import random

def findDataEntry(data):
	return data.index(b'\xFF\xDA')+2

def rewriteCodeSequence(data, pos):
	length = pos + random.randint(1,15)
	if length < len(data):
		for i in range(pos, length):
			data[i] = random.randint(1,255)
	return data

def deleteByte(data):
	startPos = random.randint(0,len(data))
	amount = random.randint(1,5)
	for i in range(startPos,startPos+amount):
		if startPos + amount < len(data):
			del data[i]
	return data

def corruptData(data,intensity):
	for i in range(1,intensity):
		if random.randint(1,100) > 80:
			pos = random.randint(0,len(data))
			data = rewriteCodeSequence(data, pos)
		else:
			data = deleteByte(data)
	return data


def main():
	with open('picture.jpg','rb') as fd:
		jpgdata = bytearray(fd.read())

	if jpgdata.startswith(b'\xFF\xD8'):
		dataStart = findDataEntry(jpgdata)
		heading = jpgdata[:dataStart]
		data = jpgdata[dataStart:-10]
		ending = jpgdata[-10:]
		corruptData(data, 10)
		jpgdata = heading + data + ending
		with open('result.jpg','wb') as fd:
			fd.write(jpgdata)
			print('success')

if __name__ == '__main__':
	main()
