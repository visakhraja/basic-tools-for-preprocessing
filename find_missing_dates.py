#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 14:36:06 2024

@author: v.sivaprasad
"""
import glob
import os
from datetime import datetime, timedelta

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def extract_date_from_filename(full_path):
    # Get the basename (filename) from the full path
    filename = os.path.basename(full_path)
    # Extract the date part from the filename
    #date_part = filename.split('_')[5].split(".")[0][:-6] #AMSR2
    date_part = filename.split('_')[6].split(".")[0]  #AMSRE
    
    return date_part

# Define the start and end date
start_date = datetime.strptime('20020619', '%Y%m%d')
end_date = datetime.strptime('20111003', '%Y%m%d')

# Use glob to get the list of filenames with full path
data = glob.glob('/media/v.sivaprasad/Expansion/FZJ/DATA/soil_moisture/AMSR/AMSRE_A/*nc')

# Generate all expected dates
expected_dates = set([single_date.strftime('%Y%m%d') for single_date in daterange(start_date, end_date)])

# Extract dates from the filenames in the 'data' list
existing_dates = set([extract_date_from_filename(filepath) for filepath in data])

# Find missing dates
missing_dates = expected_dates - existing_dates

print(f"Missing dates: {sorted(missing_dates)}")


