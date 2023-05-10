# Add a page
pdf.add_page()

# Add summary statistics
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Summary Statistics:", ln=True)
pdf.ln(5)
for row in summary_stats.itertuples():
    row_data = [row.Index] + [f"{x:.2f}" for x in row[1:]]
    for i in range(len(row_data)):
        pdf.cell(0, 10, row_data[i], border=1, ln=(i==len(row_data)-1))

pdf.ln(10)

# Add head view
pdf.cell(0, 10, "Head View:", ln=True)
pdf.ln(5)
for row in head_view.itertuples():
    row_data = [str(x) for x in row[1:]]
    for i in range(len(row_data)):
        pdf.cell(0, 10, row_data[i], border=1, ln=(i==len(row_data)-1))

pdf.ln(10)

# Add histogram plot
pdf.cell(0, 10, "Histogram Plot:", ln=True)
pdf.ln(5)
pdf.image("histogram.png", w=pdf.get_page_width() - 40, h=100)
