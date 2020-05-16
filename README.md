# netease_lyric
功能：
通过相关的网易云音乐API，获取歌词文件
根据提供的歌曲ID和歌曲名，自动创建相关的歌词文件，并将其命名为歌曲名.txt。
支持多曲目抓取，仅需要按照根目录下的ID.txt 的格式存入需要的歌曲ID和歌曲名。





通过将 歌曲ID：歌曲名 的格式存入ID.txt
并在当前路径下创建一个 lyric 文件夹，获取到的lyric歌词文件会自动保存在下面。（对无歌词的歌曲，增加了异常检测）







感谢 github.com/CeuiLiSA 提供的API接口。
感谢 不二小段 https://cloud.tencent.com/developer/article/1085978 提供的思路。
