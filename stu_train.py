import matplotlib.pyplot as plt
import ezodf




# Provide the path to your ODS file
ods_file_path = "C:\\Users\\weiii\\OneDrive\\文件\\大三\\112-2\\政治學的資料探勘與機器學習\\stu-sch-1 - train.ods"
doc = ezodf.opendoc(ods_file_path)

# Assuming there is only one sheet in the ODS file
sheet = doc.sheets[0]
data=[]
# Iterate through rows and columns to read data
for row in sheet.rows():
    for cell in row:
        data.append(cell)

print(data)


