# -*- coding: utf-8 -*-
"""

MS-Celeb-1M extractor

"""

import os,sys
import base64
import argparse


def parse_args():
    
    parser = argparse.ArgumentParser() 
    parser.add_argument('--extract_data_path', '-edp', help='Path for extracted dataset', required=True)
    parser.add_argument('--tsv_file_path' , '-tfp',  help='Path for source tsv file', required=True)
    args = parser.parse_args()
    
    return args


def main():
    
    args = parse_args()
    
    file_name = args.tsv_file_path  
    prefix = args.extract_data_path   
    
    count = 0
    
    #create dataset folder if needed
    if not os.path.exists(prefix):
        os.makedirs(prefix)

    #extracting images
    with open(file_name, encoding="utf8") as infile:
        for line in infile:

            # print line
            line_elms = line.strip().split('\t')
            dirname = line_elms[0]
            imgid = line_elms[1]
            imgid = str(count)

            # print (dirname)
            imgdata = base64.b64decode(line_elms[6])

            # mkdir
            mid_dir = prefix + '/' + dirname
            
            # handling os separators
            mid_dir = mid_dir.replace(os.sep, '/')
            
            #create class folder
            if not os.path.exists(mid_dir):
                os.makedirs(mid_dir)
            
            # save file
            filename = mid_dir + '/' + line_elms[1] + "-" + line_elms[4] + '.jpg'
            
            #debug output name 
            print (filename, 'current image counter - ', count)
            
            #writing image to file
            with open(filename, 'wb') as f:
                f.write(imgdata)

            count+=1
            
    print("Files extracted - ", count)


if __name__ == '__main__':
    main()
    
    