import re

query_list = []


def get_data(file_path):
    with open(file_path, 'r') as f:
        text = f.read().replace('\t', " ")

        cisi_file_start = re.compile('\.I ')
        cisi_id_start = re.compile('[\n]\.I')
        cisi_title_start = re.compile('[\n]\.T')
        cisi_author_start = re.compile('[\n]\.A')
        cisi_text_start = re.compile('[\n]\.W')
        cisi_publication_date_start = re.compile('[\n]\.B')
        cisi_cross_start = re.compile('[\n]\.X')

        lines = re.split(cisi_id_start, text)


        for line in lines:
            if line == '':
                continue
            entries = re.split(cisi_title_start, line)
            retLine = ''
            if(len(entries) > 1):
                id = entries[0].strip()
                entries = re.split(cisi_author_start, entries[1])
                if(len(entries) > 1):
                    title = entries[0].replace('\n', " ")
                    retLine += title.strip()
                    author = ''

                    if len(entries) > 1:
                        for i in range(1, len(entries) - 1):
                            author += entries[i].replace('\n', " ").strip()

                entries = re.split(cisi_text_start, entries[len(entries) - 1])

                retLine += author + entries[0].replace('\n', " ").strip()

                    # print(f'{line}')
                entries = re.split(cisi_publication_date_start, entries[1])
                abstract = entries[0]
                retLine += abstract.replace('\n', " ").strip()

                cross_references = entries[1]
                retLine += cross_references.replace('\n', " ").strip()

            else:
                entries = re.split(cisi_text_start, line)
                id = entries[0].strip()
                abstract = entries[1]
                retLine += abstract.replace('\n', " ").strip()
            query_list.append(retLine)
    return query_list