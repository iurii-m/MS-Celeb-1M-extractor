# -*- coding: utf-8 -*-
"""

clean labeled dataset according to the C-MS-CELEB

"""


import os
import shutil
import argparse


def parse_args():
    
    parser = argparse.ArgumentParser() 
    parser.add_argument('--ms_celeb_path', '-ms', help='Path for extracted ms-celeb-1m dataset', required=True)
    parser.add_argument('--ms_celeb_cleaned_path' , '-clms',  help='Path for cleaned ms-celeb-1m data', required=True)
    args = parser.parse_args()
    
    return args


def main():
    
    args = parse_args()
    
    src_folder = args.ms_celeb_path
    dst_folder = args.ms_celeb_cleaned_path 

    
    files_2_process = ['clean_list_128Vec_WT051_P010.txt',
                       'relabel_list_128Vec_T058.txt']
    
    count = 0
    non_found_count = 0
    found_count = 0
    
    for filename in files_2_process:
        
        # reading lines from the file
        file = open(filename, 'r' , encoding='utf8') 
        Lines = file.readlines() 
          
        # Strips the newline character 
        for line in Lines: 
            
            line_elems = line.split(" ")
            real_folder_name = line_elems[0]
            file_rel_path = line_elems[1].split("/")
            
            old_folder_name = file_rel_path[0]       
            file_name = file_rel_path[1]    
            file_name = file_name.replace('\n','')
            
           
            #copy
            old_filename = src_folder +'/'+old_folder_name +'/'+file_name
            new_filename = dst_folder +'/'+real_folder_name +'/'+file_name

            
            print('filename ', file_name , 'old folder', old_folder_name, 'real folder', real_folder_name, "not found images count - ", non_found_count, "found images count - ", found_count)

            if os.path.isfile(old_filename) :
                os.makedirs(dst_folder+'/'+real_folder_name, exist_ok=True)
                shutil.copyfile(old_filename, new_filename)
                found_count+=1
            else:
                non_found_count+=1
                
            count+=1

      
   
    
    #Final results print
    print(' all images - ', count, ' found images count - ', found_count, ' not found images count - ', non_found_count)

if __name__ == '__main__':
    main()



