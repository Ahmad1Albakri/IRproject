# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
from collections import defaultdict

cisi_txt_data = defaultdict(dict)


def get_data(file_path):
    with open(file_path, 'r') as f:
        text = f.read().replace('\t', " ")

        cisi_file_start = re.compile('\.I')
        cisi_id_start = re.compile('[\n]\.I')
        cisi_title_start = re.compile('[\n]\.T')
        cisi_author_start = re.compile('[\n]\.A')
        cisi_text_start = re.compile('[\n]\.W')
        cisi_cross_start = re.compile('[\n]\.X')

        lines = re.split(cisi_id_start, text)

        for line in lines:
            if line == '':
                continue
            entries = re.split(cisi_title_start, line)

            if len(entries) >= 2:
                id = entries[0].strip()

                # print('id = ')
                # print(f'{id}')
                #
                # print('************')

                # without the id
                entries = re.split(cisi_author_start, entries[1])

                # print(f'{entries[0]}')
                title = entries[0].replace('\n', " ")
                cisi_txt_data[id]['title'] = title.strip()

                author = ''

                if len(entries) > 1:
                    for i in range(1, len(entries) - 1):
                        author += entries[i].replace('\n', " ").strip()

                entries = re.split(cisi_text_start, entries[len(entries) - 1])

                cisi_txt_data[id]['author'] = author + entries[0].replace('\n', " ").strip()

                # print(f'{line}')
                entries = re.split(cisi_cross_start, entries[1])
                abstract = entries[0]
                cisi_txt_data[id]['abstract'] = abstract.replace('\n', " ").strip()

                cross_references = entries[1]
                cisi_txt_data[id]['cross_references'] = cross_references.replace('\n', " ").strip()

    return cisi_txt_data


def assemble(doc):
    ret = []
    for k in doc:
        ret.append((doc[k]["title"])
                   + " " + (doc[k]["author"])
                   + " " + (doc[k]["abstract"]))
    return ret


def getDoc(idx):
    return (cisi_txt_data[str(idx)]["title"]
            + '\n' + cisi_txt_data[str(idx)]['author']
            + '\n' + cisi_txt_data[str(idx)]['abstract'])
