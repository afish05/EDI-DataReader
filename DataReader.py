import os
import re

data_dir = r'C:\Users\afisher\Desktop\Data Migration Script\Data'

for file in os.listdir(data_dir):
    filename = (os.path.join(data_dir, file))
    openfile = open(filename, 'r')
    edifile = openfile.read()

    if edifile[:3] == 'ISA':

        #grab the decimal values of the delimiters first
        seg_delim = list(bytes(edifile[105],'ANSI'))
        ele_delim = list(bytes(edifile[3],'ANSI'))    
        sub_ele_delim = list(bytes(edifile[104],'ANSI'))

        #replace seg_delim with newline
        format_env = edifile.replace(edifile[105],'\n')

        #replace element delim - prob a better way, but can't get regex splits to work otherwsise
        format_del = edifile.replace(edifile[3],'*')

        #grab the ISA and GS
        isa = re.findall('^ISA.*',format_env)
        gs = re.findall('^GS.*',format_env,re.MULTILINE)

        #split_delim = '\'\\'+edifile[3]+'\''
        #str(split_delim)

        #grab the ISA quals/IDs and GS IDs
        isa_sql = re.split('\*',str(isa))[5]
        isa_sid = re.split('\*',str(isa))[6]
        isa_rql = re.split('\*',str(isa))[7]
        isa_rid = re.split('\*',str(isa))[8]
        snd_gs = re.split('\*',str(gs))[2]
        rcv_gs = re.split('\*',str(gs))[3]
        
        #print(sisa_q, sisa_id, risa_q, risa_id, seg_delim, ele_delim, sub_ele_delim)
        print(isa_sql, isa_sid, isa_rql, isa_rid, snd_gs, rcv_gs, seg_delim, ele_delim, sub_ele_delim)
        
        openfile.close()
    else:
        pass
         
exit



