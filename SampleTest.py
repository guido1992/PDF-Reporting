# -*- coding: utf-8 -*-
"""
Created on Fri 22nd September - 20:05:12 2023

@author: rathk
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs

from PIL import Image
from fpdf import FPDF
import datetime as dt

### ----- PDF DESIGN -----

# Create a PDF object
pdf = FPDF()

# Width & Height
WIDTH = 210
HEIGHT = 297

# Set Date
day = dt.datetime.today().strftime("%d/%m/%Y")

# Usage example
shapefile_path = 'C:/Users/rathk/OneDrive/Desktop/Sample/counties/counties.shp'
csv_path = 'C:/Users/rathk/OneDrive/Desktop/Sample/Ireland_Counties.csv'
common_column = 'Counties'
metric_columns = ['Site1', 'Site2', 'Site3']  # Add your metric column names here
title = '          A sample analysis report written in Python'
#about_text = 'This is an about page with some description about the PDF.'
page_titles = ['Site 1 Data', 'Site 2 Data', 'Site 3 Data']
page_subtext = ['The below map of Ireland highlights the current view of Site 1 and the status of each LA in regards to how many files'
              ' have been transferred through the pipeline at present.', 'The below map of Ireland highlights the current view of Site' 
              ' 2 and the status of each LA in regards to how many files have been transferred through the pipeline at present.', 
              ' The below map of Ireland highlights the current view of Site 3 and the status of each LA in regards to how many files'
              ' have been transferred through the pipeline at present.']

def create_multi_metric_heatmap_pdf_with_text(pdf, shapefile_path, csv_path, common_column, metric_columns):
    # Read the shapefile
    gdf = gpd.read_file(shapefile_path)
    
    # Rename columns
    gdf.rename(columns={'NAME_TAG': 'Counties'}, inplace=True)

    # Define the string values you want to remove
    values_to_remove = ['Antrim', 'Armagh', 'Londonderry', 'Tyrone', 'Fermanagh', 'Down']

    # Remove rows with specified string values from the DataFrame
    gdf = gdf.loc[~gdf['Counties'].isin(values_to_remove)]

    # Read the CSV data
    csv_data = pd.read_csv(csv_path)

    # Create a PDF document
    #pdf = FPDF()
    
    ### ----- TEXT VARIABLES -----

    TITLE = '          A sample analysis report written in Python'

    # Title page
    def create_title(day, pdf):
        # Set font, bold and header size
        pdf.set_font('Arial', 'B', 20)
        # Add line break
        pdf.ln(210)
        # Add title
        pdf.write(5, f'{TITLE}')
        # Add line break
        pdf.ln(50)   
        # Set font and title size for date of report
        pdf.set_font('Arial', '', 12)
        # Add report date
        pdf.write(4, f'{day}')
        # Add line break
        pdf.ln(5)

    ### ----- FIRST PAGE -----

    pdf.add_page()
    # Add title function to page one
    create_title(day, pdf)

    # Add image Logo
    pdf.image(r'C:/Users/rathk/OneDrive/Desktop/Sample/SampleLogo.jpg', 50, 20, WIDTH/2)
    
    # About Page
    P2H = 'About Company'                          # Page Header
    P2Title = 'The Importance of Data'                    # Paragraph Title
    P2Title1 = 'The Challenges'                           # Paragraph Title

    # Set font, bold and title size
    pdf.set_font('Arial', 'B', 18)
    # Add line break
    pdf.ln(15)
    # Add header
    pdf.write(10, f'{P2H}')
    # Add line break
    pdf.ln(15)
    # Set font and size
    pdf.set_font('Arial', '', 12)
    # Paragraph 1
    pdf.write(10, 'Sample Company is a data and analytics consultancy team who place high importance on trust and doing the right'
              ' thing. We take a holistic view. That means that while other consultants will sell a product, we start by understanding'
              ' the customer and their business. We take a long-term value creation perspective. We recognise that organisations may'
              ' not initially understand how all-encompassing data is. We partner with clients to understand their organisation, data'
              ' culture and operational challenges. Having identified the business issue, we move at the right pace for the customer.')
    
    # Add line break
    pdf.ln(20)
    # Set font, bold and title size
    pdf.set_font('Arial', 'B', 18)
    # Add header
    pdf.write(10, 'What We Do')
    # Add line break
    pdf.ln(10)
    # Set font and size
    pdf.set_font('Arial', '', 12)
    # Paragrapgh 2
    pdf.write(10, 'We help our customers establish a data culture, building confidence through incremental gains. We help join the'
              ' organisation together across all functions, business lines and reporting outputs. We help our customers see their entire'
              ' organisation and to manage it differently from a position of powerful insight.'
              
              ' We ensure data is fully embedded in your business and that your Users are properly equipped to use it and lead with data.' 
              ' Our services include Data Strategy, Busines Intelligence, Data Architecture and Implementation, Data Analytics and Artificial'
              ' Intelligence solutions, Data Visualisation, Training, Data Literacy and more.')
    
    # Add line break
    pdf.ln(20)
    # Set font, bold and title size
    pdf.set_font('Arial', 'B', 18)
    # Add header
    pdf.write(10, 'Why is this Important For Your Business?')
    # Add line break
    pdf.ln(10)
    # Set font and size
    pdf.set_font('Arial', '', 12)
    # Paragraph 3
    pdf.write(10, 'It is forecasted there will be a ten-fold increase in worldwide data by 2025, so the potential and opportunities for data'
                  ' are greater now than ever. Yet for many organisations, the ability to "think data" is still a significant challenge.' 
                  ' Numerous research studies have shown that the more data-driven organisations are, the better their results will be.')

    #for metric_column in metric_columns:
        # Join the datasets based on a common column
    #    merged_data = gdf.merge(csv_data, on=common_column)
        
    for i, metric_column in enumerate(metric_columns):
        # Join the datasets based on a common column
        merged_data = gdf.merge(csv_data, on=common_column)

        # Create a heatmap
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_aspect('equal')  # Equal aspect ratio

        # Plot the shapefile
        gdf.plot(ax=ax, color='white', edgecolor='black')

        # Plot the heatmap based on the current metric column
        merged_data.plot(column=metric_column, cmap='Blues', legend=True, ax=ax)

        # Customize the plot as needed (e.g., title, labels, legend)
        
        # Remove the axis on each side of the plot
        ax.axis('off')

        # Save the plot as an image (e.g., PNG)
        heatmap_filename = f'heatmap_{metric_column}.png'
        plt.savefig(heatmap_filename, dpi=300, bbox_inches='tight')

        # Add a new page to the PDF and embed the heatmap image
        pdf.add_page()
        pdf.set_xy(0, 0)
        pdf.image(heatmap_filename, x=20, y=50, w=170)
        
        # Add a page title and subtext for the visualization
        pdf.set_font("Arial", 'B', size=18)
        pdf.cell(200, 30, txt=page_titles[i], ln=True, align='C')
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 5, page_subtext[i])
        
        ### ----- FOURTH PAGE -----

        # Insert new page
        #pdf.add_page()

        # Set font, bold and title size
        #pdf.set_font('Arial', 'B', 18)
        # Add header
        #pdf.write(20, 'Site 2 Data')
        # Add line break
        #pdf.ln(15)
        # Set font and size
        #pdf.set_font('Arial', '', 12)
        # Paragraph
        #pdf.write(10, 'The below map of Ireland highlights the current view of Site 2 and the status of each LA in regards to how many files'
        #              ' have been transferred through the pipeline at present.')
        
    # Save the multi-page PDF to the specified path
    #pdf.output('C:/Users/rathk/OneDrive/Desktop/Sample/Test.pdf', 'F')

    #print('Sample PDF file created successfully.')

create_multi_metric_heatmap_pdf_with_text(pdf, shapefile_path, csv_path, common_column, metric_columns)

### ----- NEW PAGE -----

# Insert new page
pdf.add_page()

# Set font, bold and title size
pdf.set_font('Arial', 'B', 18)
# Add header
pdf.write(20, 'Carlow Analysis - Site 1 to Site 3')
# Add line break
pdf.ln(15)
# Set font and size
pdf.set_font('Arial', '', 12)
# Paragraph
pdf.write(10, 'The below map of Carlow highlights the current view of the upload status across the LA in regards to how many files'
              ' have been transferred through the pipeline at present.')

# Read shapefile
gdf = gpd.read_file(shapefile_path)

# Rename columns
gdf.rename(columns={'NAME_TAG': 'Counties'}, inplace=True)

# Define the string values you want to remove
values_to_remove = ['Antrim', 'Armagh', 'Londonderry', 'Tyrone', 'Fermanagh', 'Down']

# Remove rows with specified string values from the DataFrame
gdf = gdf.loc[~gdf['Counties'].isin(values_to_remove)]

# Carlow Map
gdf[gdf.Counties=="Carlow"].plot()

# Save the graph as an image (e.g., PNG)
Carlow = 'Carlow.png'
plt.savefig(Carlow, bbox_inches='tight', pad_inches=0)  # Use bbox_inches='tight' to remove extra white space
plt.close()  # Close the Matplotlib plot

# Open the image using PIL
image = Image.open(Carlow)

# Remove white space around the image
image = image.crop(image.getbbox())

# Save the cropped image back to the same file
image.save(Carlow)

# Insert the graph image into the PDF
pdf.image(Carlow, x=10, y=60, w=170)  # Adjust the position and size as needed







### ----- NEW PAGE -----

#pdf.add_page()
#pdf.set_font("Arial", size=16)
#pdf.cell(200, 10, txt="Additional Page 2", ln=True, align='C')
#pdf.ln(10)
#pdf.cell(200, 10, txt="Content for Additional Page 2", ln=True, align='C')

### ----- EXPORT PDF FILE -----

# Save the multi-page PDF to the specified path
pdf.output('C:/Users/rathk/OneDrive/Desktop/Sample/Test.pdf', 'F')

print('Sample PDF file created successfully.')