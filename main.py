import json
with open('data/list.json', 'r', encoding='UTF-8') as f:
  handles = json.load(f)


input_list = set()
for handle in handles:
  input_list.add(handle['username'].strip('\n'))
print('input list', len(input_list))

dump_file = open('data/dump.txt', 'r')
dump_reader = dump_file.readlines()
dump_set = set()
for line in dump_reader:
  dump_set.add(line.strip('\n'))
dump_file.close()
print('dump list', len(dump_set))

diff_set = input_list.difference(dump_set)

# classification model goes here
print('diff ', len(diff_set))


final_file = open('list.txt', 'w')
for name in diff_set:
  final_file.write(name+'\n')
final_file.close()

final_file = open('data/dump.txt', 'a')
for name in diff_set:
  final_file.write(name+'\n')
final_file.close()