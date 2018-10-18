from operator import itemgetter
from urllib import request

def main():
  file = '/home/xiaojie/Projects/data/yfcc100m/yfcc_top/yfcc10k.data'
  user_set = set()
  with open(file) as fin:
    while True:
      line = fin.readline()
      if not line:
        break
      fields = line.strip().split('\t')

      user = fields[1].upper()
      user_set.add(user)
  print(user_set)

def test():
  file = '/home/xiaojie/Projects/data/yfcc100m/yfcc_rnd/yfcc_rnd.data'
  # file = '/home/xiaojie/Projects/data/yfcc100m/yfcc_top/yfcc10k.data'
  # print('miscellaneous test')
  tag_count = {}
  with open(file) as fin:
    while True:
      line = fin.readline()
      if not line:
        break

      fields = line.strip().split('\t')
      tags = fields[-1].split()
      for tag in tags:
        tag_count[tag] = tag_count.get(tag, 0) + 1

  tag_count = sorted(tag_count.items(), key=itemgetter(1), reverse=True)
  for tag, count in tag_count:
    print('%s\t%d' % (tag, count))

if __name__ == '__main__':
  main()