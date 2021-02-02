# PdfScanner
Creating pdf files by scanning and applying thresholding, cropping and orientation features onto images captured through a webcam (mobile camera for this project)

---PDF SCANNER---
This Pdf scanner is made using ip webcam and a few image processing techniques. 
Technology Stack used: Python, OpenCV, Pillow.
---Features of pdf scanner:---
1. Connected the phone camera with the laptop using python.
2. Used black and white conversion (if the image is normal and readable)
3. Used Adaptive thresholding (if the image is unclear and not readable)
---Additional features added:---
1.	Introduced mouse click events to select the edge coordinates to crop the image. The coordinates selected will be displayed in the form (x, y) over the image frame.
2.	Used the Image module from the Pillow package to save as many pdfs as wanted in a desired dynamically allocated directory without replacing the existing ones. (made use of the “random” library to implement this feature)
3.	Now, you can opt to change the orientation of the image by rotating it 90 degree clockwise/anti-clockwise or by 180 degrees.
4.	Made the user experience better by stating proper guidelines to run the code.
