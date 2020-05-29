from src.RE.re import extract_relation


text = "bộ phim tài liệu Blackfish (2013) của đạo diễn Gabriela Cowperthwaite về tình trạng bạo hành cá voi tại công viên " \
       "giải trí SeaWorld thuộc bang Florida, Mỹ cũng tăng cao nhận thức cho con người về việc bảo vệ động vật. Cuối năm 2017, Wonder Woman của" \
       " đạo diễn Patty Jenkins đã trở thành một cú nổ lớn khi cán mốc 700 triệu USD trên toàn thế giới và trở thành bộ phim live-action có doanh thu cao nhất được làm ra bởi một nữ đạo diễn."
print(extract_relation(text))