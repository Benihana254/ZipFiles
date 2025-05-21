import os,shutil,zipfile
# creating files to be compressed
with open('fileA.txt','w') as f1:
    f1.write('Once upon a time in Nairobi')
with open('file2.txt','w') as f2:
    f2.write('Knights On Broadway!')
#creating a zip file using zipfile module and adding files onto it
with zipfile.ZipFile('archive.zip','w') as zipf:
    zipf.write('fileA.txt')
    zipf.write('file2.txt')
#working with the created zip file
with zipfile.ZipFile('archive.zip','r') as zipf:
    print(zipf.namelist()) # a list of all files in the zip
    print(zipf.open('file2.txt').read()) # reading file2
zip_path = os.path.abspath("archive.zip") # the absolute path of the created zipfile
print(f'This is the path {zip_path}')
#Creating a new directory called new_zipfolder
os.makedirs('new_zipfolder', exist_ok=True)
# copying the zip onto the created folder above
shutil.copy(zip_path,'new_zipfolder' )
#copying the zip onto another folder on the pc
shutil.copy(r'C:\Users\gh\PycharmProjects\ZipFiles\archive.zip', r'C:\Users\gh\Desktop\FolderB')
