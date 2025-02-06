import sweetviz as sv
import pandas as pd

file_path = './MLZilla Data Set.xlsx' 
data = pd.read_excel(file_path)
if 'TotalCharges' in data.columns:
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
report = sv.analyze(data)

report.show_html('MLZilla_EDA_Report.html')

print("EDA report generated successfully: index.html")
