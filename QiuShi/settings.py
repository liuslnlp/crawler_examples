"""
配置文件
"""

# 发件箱
FROM_MAIL = "XXXXXXXXX@126.com"

# 收件箱
TO_MAIL = "XXXXXXXX@126.com"

# smtp服务器
SMTP_SERVER = "smtp.126.com"

# 发件箱用户名（不包含@以后的部分）
FROM_MAIL_USERNAME = "XXXXXXXXX"

# 发件箱密码
FROM_MAIL_PASSWORD = "XXXXXXXXXXXXX"

# 每次抓取的页数，默认为5
PAGES = 5

#两次抓取的间隔时间，默认为12小时，即每天推送两次
INTERVALS = 43200