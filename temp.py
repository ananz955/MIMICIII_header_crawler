    # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
import wfdb
import time

mimic_patient_list = wfdb.get_record_list('mimic3wdb/matched/')
for patient in mimic_patient_list:
    try:
        record_list = wfdb.get_record_list('mimic3wdb/matched/'+patient)
        flog = open('matched.log','w+')
        f.write("get patient"+patient)
        flog.close()
    except:
        time.sleep(10)
        try:
            record_list = wfdb.get_record_list('mimic3wdb/matched/'+patient)
        except:
            pass
    print(record_list)
    for record in record_list:
        f = open('mimic3wdbmatched.csv','a+')
        try:
            header_info = wfdb.rdheader(record, pb_dir='mimic3wdb/matched/'+patient)
        except:
            print("no such header:"+record)
        heder_dict = header_info.__dict__
        print(patient+record)
        f.write((patient+record).rjust(20,' ')+',')
        try:
            for sig in heder_dict['sig_name']:
                f.write(sig+',')
            print(heder_dict['sig_name'])
        except TypeError:
            f.write('none')
        f.write('\n')
        f.close()