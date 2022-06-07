
import re
from collections import defaultdict

cisi_txt_data = defaultdict(dict)

query_list = []

def get_cacm_query(file_path):
    with open(file_path, 'r') as f:
        text = f.read().replace('\t', " ")

        cisi_file_start = re.compile('\.I ')
        cisi_id_start = re.compile('[\n]\.I')
        cisi_title_start = re.compile('[\n]\.T')
        cisi_author_start = re.compile('[\n]\.A')
        cisi_text_start = re.compile('[\n]\.W')
        cisi_cross_start = re.compile('[\n]\.X')
        cisi_publication_date = re.compile('[\n]\.B')
        cisi_adding_date = re.compile('[\n]\.N')

        lines = re.split(cisi_file_start, text);



        for line in lines:
            if line == '':
                continue
            retLine = ''
            entries = re.split(cisi_text_start, line)

            if len(entries) >= 2:
                id = entries[0].strip()

                # without the id
                entries = re.split(cisi_author_start, entries[1])
                if(len(entries) > 1):
                    retLine += entries[0].replace('\n', " ").strip()
                    entries = re.split(cisi_adding_date, entries[1])
                    retLine += entries[0].replace('\n', " ").strip()
                    retLine += entries[1].replace('\n', " ").strip()

                else:
                    entries = re.split(cisi_adding_date, entries[0])
                    retLine += entries[0].replace('\n', " ").strip()
                    retLine += entries[1].replace('\n', " ").strip()
                query_list.append(retLine)
    return query_list


