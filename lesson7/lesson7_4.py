import argparse

parser = argparse.ArgumentParser(description="請輸入姓名")
parser.add_argument("-n","--name",type=str,help="姓名")
args = parser.parse_args()

if not args.name:
    name = input("請輸入您的姓名:")
     
else:
   name = args.name

print(name)


