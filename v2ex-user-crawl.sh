while [ 1 -eq 1 ] ; do 
  python v2ex-user-crawl.py >> v2ex-online.log; 
  date >> v2ex-online.log; 
  echo "" >> v2ex-online.log; 
  sleep 1800; 
done
