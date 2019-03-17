def FunctionAlgo():
	import io
	from PIL import Image
	import pytesseract
	import  PyPDF2
	from wand.image import Image as wi


	pdf = wi(filename = "/home/kadmin/Desktop/prog1.pdf")
	pdfImg = pdf.convert('jpeg')

	imgBlobs = []

	for img in pdfImg.sequence:
		page = wi(image = img)
		imgBlobs.append(page.make_blob('jpeg'))

	extracted_text = []

	for imgBlob in imgBlobs:
		im = Image.open(io.BytesIO(imgBlob))
		text = pytesseract.image_to_string(im, lang = 'eng')
		extracted_text.append(text)

	pdfFileObj = open("/home/kadmin/Desktop/prog1.pdf", 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	p1 = pdfReader.numPages

	print(p1)



	for i in range (p1 ):
	#print(extracted_text[i])

		result= (extracted_text[i])

		with open('exp1.txt', mode='w') as file:
			file.write(result)