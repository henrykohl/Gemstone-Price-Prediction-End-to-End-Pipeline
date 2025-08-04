import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs")

os.makedirs(log_path,exist_ok=True)

LOG_FILEPATH=os.path.join(log_path,LOG_FILE)


logging.basicConfig(level=logging.INFO, 
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    
)
            #[2024-01-10 15:57:26,997] 6 root - INFO -  this my second tesgting
# if __name__ == '__main__' # 不知為何 Lecture demo 時，直接執行 python test.py 會出錯  
#   logging.info("here again i am testing")

# 在其他檔案使用 from src.logger.logging import logging 就沒問題


