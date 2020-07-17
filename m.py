import sys
import urllib3
from bs4 import BeautifulSoup
from datetime import date


class Problem:

    def __init__(self, index):
        self.index = index
        self.url = self._get_url(index)
        self.title = self._get_title(index)

    def _get_url(self, index):
        return f'https://www.acmicpc.net/problem/{index}'

    def _get_title(self, index):
        urllib3.disable_warnings()
        url = self._get_url(index)
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        soup = BeautifulSoup(r.data, 'html.parser')
        return soup.title.string.split("번: ")[1]

    def __str__(self):
        return f'{self.index} {self.url} {self.title}'


def get_date() -> str:
    today = date.today()
    return f'{today.year}년 {today.month}월 {today.day}일'


def get_templete(low: Problem, high: Problem) -> str:
    msg = get_date()
    msg += '\n'
    msg += '공지 및 이전 문제 정리 : https://www.notion.so/PS-da8977089c2344dba9bdbc3d0188d286\n'
    msg += '- 낮에는 (2시 ~8시) 풀고 인증합니다.\n'
    msg += '- 어려운 문제가 나왔을 때는, 4시부터 서로 힌트를 주고받습니다.\n'
    msg += '- 밤 8시 부터 푼 문제의 코드를 공개합니다.\n'
    msg += '중하급 \n'
    msg += low.title
    msg += '\n'
    msg += low.url
    msg += '\n'
    msg += '중상급 \n'
    msg += high.title
    msg += '\n'
    msg += high.url
    return msg


def get_notion_templete(low: Problem, high: Problem) -> str:
    msg = "### "
    msg += get_date()
    msg += '\n\n'
    msg += '- 중하급\n'
    msg += '    - '
    msg += low.title
    msg += '\n        - '
    low_url = low.url
    msg += low_url
    msg += '\n'
    msg += '- 중상급\n'
    msg += '    - '
    msg += high.title
    msg += '\n        - '
    high_url = high.url
    msg += high_url
    msg += '\n'
    return msg


if __name__ == '__main__':
    low = Problem(sys.argv[1])
    high = Problem(sys.argv[2])

    templete = get_templete(low, high)
    notion_templete = get_notion_templete(low, high)
    # print(templete)
    print(notion_templete)
    f = open(f'{get_date()}.txt', 'w')
    f.write(templete)
    f.close()
