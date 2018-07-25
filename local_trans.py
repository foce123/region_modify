# coding = utf-8
# date: 20180724
# write by: zhangt

import argparse
import sys

filename = '/openstack-dashboard/openstack_dashboard/datacenter_locale/zh_CN/LC_MESSAGES/django.po'
flag = 0
count = 0

def data_list():
  global flag
  with open(filename ,'r') as f:
    data = f.readlines()
    for line in data:
      if line.strip()[:5] == 'msgid':
        flag = 1
        msg = line.split('"')
        print(msg[1])
      if flag == 1 and line.strip()[:6] == 'msgstr':
        msgt = line.split('"')
        print(msgt[1])

def data_add(aid,area):
  global count
  line_c = []
  lines = []
  with open(filename ,'r') as f:
    for line in f:
      count += 1
      lines.append(line)
      if line.strip()[:5] == 'msgid':
        line_c.append(count)
  lines.insert(line_c[-1]+1,'\n')
  lines.insert(line_c[-1]+2,'msgid "{}"\n'.format(aid))
  lines.insert(line_c[-1]+3,'msgstr "{}"\n'.format(area))
  data = ''.join(lines)
  with open(filename, 'w+') as fw:
    fw.write(data)
  print('Add area information successful !')

def data_delete(aid):
  global count
  lines = []
  with open(filename ,'r') as f:
    for line in f:
      count += 1
      lines.append(line)
      if line.strip()[:5] == 'msgid':
        if line.split('"')[1] == aid:
          line_c = count
    lines.pop(line_c-1)
    lines.pop(line_c-1)
    if lines[-1] == '\n':
      lines.pop(line_c-1)
    data = ''.join(lines)
    with open(filename, 'w+') as fw:
      fw.write(data)
    print('Delete area information successful !')

def data_update(aid,area):
  global count
  lines = []
  with open(filename ,'r') as f:
    for line in f:
      count += 1
      lines.append(line)
      if line.strip()[:5] == 'msgid':
        if line.split('"')[1] == aid:
          line_c = count
  lines[line_c] = 'msgstr "{}"\n'.format(area)
  data = ''.join(lines)
  with open(filename, 'w+') as fw:
    fw.write(data)
  print('Update area information successful !')

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-v','--version', action='store_true',help = 'version')
  parser.add_argument('-l','--list', action='store_true',help = 'list area informations')
  parser.add_argument('-a','--add', nargs = 2, type = str, metavar=('msgid','msgstr'),help = 'add area information')
  parser.add_argument('-d','--delete', nargs = 1, type = str, metavar=('msgid'),help = 'delete area information')
  parser.add_argument('-u','--update', nargs = 2, type = str, metavar=('msgid','msgstr'),help = 'update area information')
  args = parser.parse_args()
  if args.version:
    print('version 1.0')
  elif args.list:
    data_list()
  elif args.add:
    data_add(args.add[0],args.add[1])
  elif args.delete:
    data_delete(args.delete[0])
  elif args.update:
    data_update(args.update[0],args.update[1])
  else:
    parser.print_help()
