from run import app
import ddddocr


@app.route('/api/ddddocr')
def get_ddddocr():
    ocr = ddddocr.DdddOcr()
    with open("C:\\Users\\Admin\\Desktop\\111.jpg",'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    return res