import crypt

pwd = crypt.crypt('egg','salt')
print(pwd)