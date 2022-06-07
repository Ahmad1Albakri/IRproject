import re
from collections import defaultdict

cisi_txt_data = defaultdict(dict)


def get_cacm_data(file_path):
    with open(file_path, 'r') as f:
        text = f.read().replace('\t', " ")

        cisi_file_start = re.compile('\.I')
        cisi_id_start = re.compile('[\n]\.I')
        cisi_title_start = re.compile('[\n]\.T')
        cisi_author_start = re.compile('[\n]\.A')
        cisi_text_start = re.compile('[\n]\.W')
        cisi_cross_start = re.compile('[\n]\.X')
        cisi_publication_date = re.compile('[\n]\.B')
        cisi_adding_date = re.compile('[\n]\.N')

        lines = re.split(cisi_id_start, text);
        global x, t, w, b, n;

        for line in lines:
            if line == '':
                continue
            entries = re.split(cisi_title_start, line)

            if len(entries) >= 2:
                id = entries[0].strip()

                # without the id
                entries = re.split(cisi_text_start, entries[1])
                cisi_txt_data[id]['abstract'] = ''
                cisi_txt_data[id]['title'] = ''
                cisi_txt_data[id]['publication_date'] = ''
                cisi_txt_data[id]['author'] = ''

                if (len(entries) > 1):
                    title = entries[0].replace('\n', " ")
                    cisi_txt_data[id]['title'] = title.strip()

                    entries = re.split(cisi_publication_date, entries[1])
                    cisi_txt_data[id]['abstract'] = entries[0].replace('\n', " ").strip()

                    entries = re.split(cisi_author_start, entries[1])

                    if (len(entries) > 1):
                        publication_date = entries[0]
                        cisi_txt_data[id]['publication_date'] = publication_date.replace('\n', " ").strip()

                        entries = re.split(cisi_adding_date, entries[1])
                        cisi_txt_data[id]['author'] = entries[0].replace('\n', " ").strip()

                        entries = re.split(cisi_cross_start, entries[1])
                        cisi_txt_data[id]['adding_date'] = entries[0].replace('\n', " ").strip()
                        cisi_txt_data[id]['cross_references'] = entries[1].replace('\n', ' ').strip()
                    else:
                        entries = re.split(cisi_adding_date, entries[0])
                        cisi_txt_data[id]['publication_date'] = entries[0].replace('\n', " ").strip()
                        entries = re.split(cisi_cross_start, entries[1])
                        cisi_txt_data[id]['adding_date'] = entries[0].replace('\n', " ").strip()
                        cisi_txt_data[id]['cross_references'] = entries[1].replace('\n', ' ').strip()

                else:
                    entries = re.split(cisi_publication_date, entries[0])
                    title = entries[0].replace('\n', " ")
                    cisi_txt_data[id]['title'] = title.strip()
                    entries = re.split(cisi_author_start, entries[1])
                    if (len(entries) > 1):
                        publication_date = entries[0]
                        cisi_txt_data[id]['publication_date'] = publication_date.replace('\n', " ").strip()
                        entries = re.split(cisi_adding_date, entries[1])
                        cisi_txt_data[id]['author'] = entries[0].replace('\n', " ").strip()

                        entries = re.split(cisi_cross_start, entries[1])
                        cisi_txt_data[id]['adding_date'] = entries[0].replace('\n', " ").strip()
                        cisi_txt_data[id]['cross_references'] = entries[1].replace('\n', ' ').strip()

                    else:
                        entries = re.split(cisi_adding_date, entries[0])
                        cisi_txt_data[id]['publication_date'] = entries[0].replace('\n', " ").strip()
                        entries = re.split(cisi_cross_start, entries[1])
                        cisi_txt_data[id]['adding_date'] = entries[0].replace('\n', " ").strip()
                        cisi_txt_data[id]['cross_references'] = entries[1].replace('\n', ' ').strip()

    return assemble(cisi_txt_data)


def assemble(doc):
    ret = []
    for k in doc:
        ret.append((doc[k]['title'])
                   + " " + (doc[k]['publication_date'])
                   + " " + (doc[k]['author'])
                   + " " + (doc[k]['adding_date'])
                   + " " + (doc[k]['abstract']))
    return ret
