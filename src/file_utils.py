import os
import settings

parent_dir = 'data'


def check_paths(output_dir):
    global parent_dir
    if output_dir:
        if os.path.exists(output_dir):
            if os.path.exists(os.path.join(output_dir, parent_dir)):
                output_dir = os.path.join(output_dir, parent_dir)
            else:
                os.makedirs(os.path.join(output_dir, parent_dir))
                output_dir = os.path.join(output_dir, parent_dir)
        else:
            os.makedirs(output_dir)
            os.makedirs(os.path.join(output_dir, parent_dir))
            output_dir = os.path.join(output_dir, parent_dir)
    else:
        if os.path.exists(parent_dir):
            output_dir = os.path.join(parent_dir)
        else:
            os.makedirs(parent_dir)
            output_dir = os.path.join(parent_dir)
    return output_dir


def open_files(primary_url, output_dir):
    output_dir = output_dir if output_dir else ''
    if os.path.exists(os.path.join(output_dir, 'category_names.txt')):
        settings.fcn = open(os.path.join(output_dir,'category_names.txt'), 'r+', encoding='utf-8')
        settings.cat_names = set([t.replace('\n', '') for t in settings.fcn.readlines() if t != '\n'])
        print(f'Categories file exists. {len(settings.cat_names)} categories included')

    else:
        settings.fcn = open(os.path.join(output_dir, 'category_names.txt'), 'a+', encoding='utf-8')
        print('Categories file does not exist')
        settings.cat_names = set()

    if os.path.exists(os.path.join(output_dir, 'category_links.txt')):
        settings.fcl = open(os.path.join(output_dir, 'category_links.txt'), 'r+', encoding='utf-8')
        settings.cat_links = set([t.replace('\n', '') for t in settings.fcl.readlines() if t != '\n'])
        print(f'Category links file exists. {len(settings.cat_links)} category links included')

    else:
        settings.fcl = open(os.path.join(output_dir, 'category_links.txt'), 'a+', encoding='utf-8')
        print('Category links file does not exist')
        settings.cat_links = set()
        settings.cat_links.add(primary_url)

    if os.path.exists(os.path.join(output_dir, 'done_links.txt')):
        settings.fdl = open(os.path.join(output_dir, 'done_links.txt'), 'r+', encoding='utf-8')
        settings.done_links = set([t.replace('\n', '') for t in settings.fdl.readlines() if t != '\n'])
        print(f'Done links file exists. {len(settings.done_links)} links processing completed')

    else:
        settings.fdl = open(os.path.join(output_dir, 'done_links.txt'), 'a+', encoding='utf-8')
        print('Done links file does not exist')
        settings.done_links = set()

    if os.path.exists(os.path.join(output_dir, 'page_links.txt')):
        settings.fpl = open(os.path.join(output_dir, 'page_links.txt'), 'r+', encoding='utf-8')
        settings.page_links = set([t.replace('\n', '') for t in settings.fpl.readlines() if t != '\n'])
        print(f'Page links file exists. {len(settings.page_links)} page links included')
    else:
        settings.fpl = open(os.path.join(output_dir, 'page_links.txt'), 'a+', encoding='utf-8')
        print('Page links file does not exist')
        settings.page_links = set()

    if os.path.exists(os.path.join(output_dir, 'page_names.txt')):
        settings.fpn = open(os.path.join(output_dir, 'page_names.txt'), 'r+', encoding='utf-8')
        settings.page_names = set([t.replace('\n', '') for t in settings.fpn.readlines() if t != '\n'])
        print(f'Page names file exists. {len(settings.page_names)} pages included')
    else:
        settings.fpn = open(os.path.join(output_dir, 'page_names.txt'), 'a+', encoding='utf-8')
        print('Page name file does not exist')
        settings.page_names = set()

    print('\n\n\n')


def initiate_file_opens(output_dir,primary_url):
    output_paths = check_paths(output_dir)
    open_files(primary_url, output_paths)


def write_files():
    settings.fcn.seek(0)
    settings.fcn.truncate()
    settings.fcn.write('\n'.join(settings.cat_names))

    settings.fcl.seek(0)
    settings.fcl.truncate()
    settings.fcl.write('\n'.join(settings.cat_links))

    settings.fdl.seek(0)
    settings.fdl.truncate()
    settings.fdl.write('\n'.join(settings.done_links))

    settings.fpl.seek(0)
    settings.fpl.truncate()
    settings.fpl.write('\n'.join(settings.page_links))

    settings.fpn.seek(0)
    settings.fpn.truncate()
    settings.fpn.write('\n'.join(settings.page_names))
