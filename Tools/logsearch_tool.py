#!/usr/local/bin/python3

###############
# Task1-1 : Download 받은 log Directory 에서 검색값 찾아서 출력 ( Complete (Y) )
# Task1-2 : Download 받은 log Directory 에서 검색값 찾아서 File로 저장 ( Complete (Y) )
# Task1-3 : Download 받은 log Directory 에서 여러개의 검색값 찾아서 순차적(검색 시간단위) File로 저장 ( Complete (Y) )
# Task1-4 : Download 받은 log Directory 에서 특정 시간 ( 2019-01-30 00:00:00 - 01:00:00 )여러개의 검색값 찾아서 File로 저장 ( Complete (Y/N) )
# Task2-1 : Download 받은 log Directory 에서 검색값 찾아서 전송량 Sum ( Complete (Y/N) )
# Task2-2 : Download 받은 log Directory 에서 검색값 찾아서 Hit Miss count table ( Complete (Y/N) )
# Task2-2 : Download 받은 log Directory 에서 검색값 찾아서 HTTP response code Table ( Complete (Y/N) )


import os
import gzip
import sys
from datetime import datetime

def pathlist(root_dir):

    final_path = []

    for root, dirs, files in os.walk(root_dir, onerror=None):  # walk the root dir
        for filename in files:  # iterate over the files in the current dir
            # file_path = os.path.join(root, filename)  # build the file path
            final_path.append(os.path.join(root, filename))  # build the file path
            # final_path += [file_path]
    list_num = len(final_path)
    return list_num, final_path

def res_file():
    result_file = 'result-' + str(datetime.now().strftime('%Y%m%d-%H%M%S')) + '.txt'
    return result_file

def line_search(args,r_final_path,r_list_num):

    keyword_num = len(args)
    result = open(res_file(),"a+")
    end_count = 0

    for r_file_path in r_final_path:
        try:
            with gzip.open(r_file_path, "rb") as f:  # open the file for reading
                # read the file line by line
                for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                    try:
                        line = line.decode("utf-8")  # try to decode the contents to utf-8
                    except ValueError:  # decoding failed, skip the line
                        continue
                    count = 0
                    for keyword in args:
#                        print("[[[[" + keyword + "]]]]")
#                        print(str(r_file_path) + " <====> " + str(r_final_path[0]))
                        end_count += 1
                        if r_file_path == r_final_path[0] and end_count == 1:
                            print("This is Sample Log line. Is this log format correct for processing further?")
                            print(" ")
                            print(line)
                            print(" ")
                            yndecision = str(input("Type Y/N :"))
                            if yndecision == "Y" or yndecision == "y":
                                continue
                            else:
                                sys.exit(1)
                        elif not keyword in line:  # if the keyword exists on the current line...
                            break
                        elif count == len(args)-1 and keyword in line:
                            result.write(line)
                        else:
                            print(" ")
                            print("Processing.......")
                            count += 1
                            # print(line)
    #                        print(file_path)  # print the file path
    #                        break  # no need to iterate over the rest of the file
        except (IOError, OSError):  # ignore read and permission errors
            pass

    result.close()

#def total_sum():
#    continue

#def specific_log_time():
#    continue

#def response_table():
#    continue

def main():
    # Get the Variables from Users
    args = sys.argv[1:]

    if not args:
        print('Usage: logsearch_tool.py "Keyword1" "Keyword2" "Keyword3" ...')
        sys.exit(1)

    root_dir = input("Root Directory : ")  # path to the root directory to search

    r_list_num,r_final_path = pathlist(root_dir)
    print(" ")
    print("---------------------------------------------------")
    print("Start Processing : " + str(r_list_num) + " EA files")
    print("---------------------------------------------------")
    print(" ")

    line_search(args,r_final_path,r_list_num)

    print(" ")
    print("COMPLETED")


if __name__ == '__main__':
    main()
