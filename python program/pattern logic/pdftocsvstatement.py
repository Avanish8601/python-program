import tabula             #install tabula package

data= tabula.read_pdf("Financial-Statement_2020.pdf",pages='4+5')   #read pdf file
#print(data)
#convert pdf into csv
tabula.convert_into("Financial-Statement_2020.pdf","Financial-Statement_2020.csv",output_format="csv",pages='4+5')
print(data)
dd
