import os,shutil,zipfile
with open('fileA.txt','w') as f1:
    f1.write('Once upon a time in Nairobi')
with open('file2.txt','w') as f2:
    f2.write('Knights On Broadway!')
with zipfile.ZipFile('archive.zip','w') as zipf:
    zipf.write('fileA.txt')
    zipf.write('file2.txt')
with zipfile.ZipFile('archive.zip','r') as zipf:
    print(zipf.namelist())
    print(zipf.open('file2.txt').read())
zip_path = os.path.abspath("archive.zip")
print(f'This is the path {zip_path}')
os.makedirs('new_zipfolder', exist_ok=True)
shutil.copy(zip_path,'new_zipfolder' )
shutil.copy(r'C:\Users\gh\PycharmProjects\ZipFiles\archive.zip', r'C:\Users\gh\Desktop\FolderB')
