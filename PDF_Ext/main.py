import pdfplumber

def infoheader(path='placeholder.pdf'): 
    txt='='*100+'\n'
    with pdfplumber.open(path) as pdf:  
        for data in pdf.metadata:
            txt+=str(data)+': '+str(pdf.metadata[data])+'\n'
    txt+='='*100+'\n\n'
    return txt

def extractor(path='placeholder.pdf', infoheader_show=True):
    text=''
    if infoheader_show:
        text+=infoheader(path)
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text+='Page'+str(page.page_number)+'\n'+'='*100+'\n'
            text+=page.extract_text()+'\n'
            text+='='*100+'\n\n'
    return text

def writer(text, file):
    with open(file, 'w') as f:
        f.write(text)

def pdf2txt(fin='placeholder.pdf', fout='placeholder.txt', infoheader=True):
    writer(extractor(path=fin, infoheader_show=True), fout)
    print("Copied content of", fin.split('\\')[-1], "to", fout.split('\\')[-1])

pdf2txt()