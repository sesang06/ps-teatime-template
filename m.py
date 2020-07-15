import sys
import urllib3
from bs4 import BeautifulSoup
from datetime import date


def get_date():
    today = date.today()
    return f'{today.year}년 {today.month}월 {today.day}일'

def get_url(index):
    return f'https://www.acmicpc.net/problem/{index}'
def get_title(index):
    urllib3.disable_warnings()
    url = get_url(index)
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data, 'html.parser')
    return soup.title.string.split("번: ")[1]


def get_templete(low, high):
    msg = get_date()
    msg += '\n'
    msg += '- 낮에는 (2시 ~8시) 풀고 인증합니다.\n'
    msg += '- 어려운 문제가 나왔을 때는, 4시부터 서로 힌트를 주고받습니다.\n'
    msg += '- 밤 8시 부터 푼 문제의 코드를 공개합니다.\n'
    msg += '중하급 \n'
    msg += get_title(low)
    msg += '\n'
    msg += get_url(low)
    msg += '\n'
    msg += '중상급 \n'
    msg += get_title(high)
    msg += '\n'
    msg += get_url(high)
    return msg

if __name__ == '__main__':
    low = sys.argv[1]
    high = sys.argv[2]

    templete = get_templete(low, high)
    print(templete)
    f = open(f'{get_date()}.txt', 'w')
    f.write(templete)
    f.close()
