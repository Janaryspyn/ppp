import os
print('Existence', os.access('C:\\Users\\123\\Documents\\pp2 doc.docx', os.F_OK))
print('Readable', os.access('C:\\Users\\123\\Documents\\pp2 doc.docx', os.R_OK))
print('Writeable', os.access('C:\\Users\\123\\Documents\\pp2 doc.docx', os.W_OK))
print('Exucutable', os.access('C:\\Users\\123\\Documents\\pp2 doc.docx', os.X_OK))