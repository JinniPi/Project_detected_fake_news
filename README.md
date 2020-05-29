
$requirement
- python 3.6
- underthesea
- vncorenlp

  pip3 install vncorenlp
  link cài chi tiết: https://github.com/vncorenlp/VnCoreNLP
  
  run cmd để bật service:
  
        $ vncorenlp -Xmx2g <FULL-PATH-to-VnCoreNLP-jar-file> -p 9000 -a "wseg,pos,ner"

- Thay đường dẫn data trong thư mục config
- Thay đường dẫn tới file config trong file src/RE/config.py

- chạy file test.py
  
