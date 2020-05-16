import requests
import json
import re

def du_qu_shu_ju(text_line):#读取每行数据，将其分为键值对并返回
	text_line = text_line
	index_maohao = text_line.index(":")
	key = text_line[:index_maohao]
	value = text_line[index_maohao+1:-2]
	return key,value

def huo_qu_lyric(music_id,music_name):#根据歌曲ID和歌曲名，获取并创建相关的歌词软件在相对路径下的lyric文件夹
	music_id = music_id
	music_name = music_name
	lrc_url = 'https://api.imjad.cn/cloudmusic/?type=lyric&id=' + music_id
	lyric = requests.get(lrc_url)
	json_obj = lyric.text
	j = json.loads(json_obj)
	try:#部分歌曲没有歌词，这里引入一个异常
		lrc = j['lrc']['lyric']
		#pat = re.compile(r'\[.*\]')
		#lrc = re.sub(pat, "", lrc)
		lrc = lrc.strip()
		data = open(r'./lyric/' + music_name + '.txt','w+',encoding='utf-8')
		data.writelines(lrc)
		data.close()
	except KeyError as e:
		pass

fr = open('ID.txt','rt',encoding='utf-8')


ID,name = [],[]#将ID.txt中的歌曲ID与歌曲名分别存入两个列表中。
for line in fr:	
	key,value = du_qu_shu_ju(line)
	ID += [key]
	name += [value]
fr.close()

nextpoint = 0
while(nextpoint<len(ID)):
	huo_qu_lyric(ID[nextpoint],name[nextpoint])
	nextpoint += 1

