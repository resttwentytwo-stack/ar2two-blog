"""畫美麗島站到阿爾兔兔的區域示意圖，輸出 src/assets/diagrams/area-map.svg。
配置照 Ken 提供的停車場說明圖，畫法參考 Google 地圖平面樣式。改位置時改下面的座標再重跑。"""
from pathlib import Path

W, MAPH = 760, 600
H = MAPH + 96
BG, ROAD, EDGE, TXT = '#efe9df', '#ffffff', '#d9cfc2', '#5c5047'
ACC, DRV, ONE = '#c2410c', '#2563eb', '#16a34a'
FONT = "font-family=\"'Noto Sans TC','Microsoft JhengHei','PingFang TC',sans-serif\""

# 道路位置
X_ZILI, X_NANTAI, X_ZHONGSHAN = 110, 470, 660
Y_LIUHE, Y_ZHONGZHENG, Y_43, Y_DATONG = 70, 190, 300, 560
X_1NONG = 320
Y_TEMPLE_LANE = 425  # 廟下方通往嘟嘟房的路

s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" {FONT}>',
     f'<rect width="{W}" height="{H}" fill="#fffaf4"/>', f'<rect width="{W}" height="{MAPH}" fill="{BG}"/>']


def hroad(y, w, x1=0, x2=W):
    s.append(f'<rect x="{x1}" y="{y - w / 2}" width="{x2 - x1}" height="{w}" fill="{ROAD}" stroke="{EDGE}"/>')


def vroad(x, w, y1=0, y2=MAPH):
    s.append(f'<rect x="{x - w / 2}" y="{y1}" width="{w}" height="{y2 - y1}" fill="{ROAD}" stroke="{EDGE}"/>')


def text(x, y, t, size=15, color=TXT, weight=400, anchor='middle', halo=False):
    h = ' stroke="#fff" stroke-width="4" paint-order="stroke"' if halo else ''
    s.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}"{h}>{t}</text>')


def vtext(x, y, t, size=15, weight=700, color=TXT):
    for i, ch in enumerate(t.replace(' ', '')):
        text(x, y + i * (size + 3), ch, size, color, weight)


def poi(x, y, label, color, sym, dy=32, r=13, size=13):
    s.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" stroke="#fff" stroke-width="2.5"/>')
    text(x, y + size * 0.38, sym, size, '#fff', 700)
    if label:
        text(x, y + dy, label, 12.5, TXT, 700, halo=True)


# 道路
hroad(Y_LIUHE, 30); hroad(Y_ZHONGZHENG, 40); hroad(Y_DATONG, 30)
vroad(X_ZILI, 34); vroad(X_NANTAI, 28); vroad(X_ZHONGSHAN, 44)
hroad(Y_43, 22, X_ZILI, X_NANTAI); vroad(X_1NONG, 14, Y_43, Y_DATONG)
hroad(Y_TEMPLE_LANE, 20, X_NANTAI, X_ZHONGSHAN)

# 路名
text(290, Y_LIUHE + 5, '六合二路'); text(565, Y_LIUHE + 5, '六合二路')
text(290, Y_ZHONGZHENG + 6, '中正四路', 17, weight=700); text(565, Y_ZHONGZHENG + 6, '中正四路', 17, weight=700)
text(290, Y_DATONG + 5, '大同一路'); text(565, Y_DATONG + 5, '大同一路')
vtext(X_ZILI, 400, '自立二路', 16); vtext(X_NANTAI, 340, '南台路', 15); vtext(X_ZHONGSHAN, 470, '中山一路', 17)
text(215, Y_43 + 5, '南台路 43 巷', 12.5, weight=700)
vtext(X_1NONG - 22, 440, '43巷1弄', 12, weight=400)
text(380, Y_LIUHE - 18, '六合夜市（六合二路）', 13, color='#9a3412', weight=700)

# 南台路單行道（往南）
s.append(f'<line x1="{X_NANTAI + 8}" y1="{Y_ZHONGZHENG + 26}" x2="{X_NANTAI + 8}" y2="{Y_DATONG - 26}" stroke="{ONE}" stroke-width="4" stroke-linecap="round"/>')
s.append(f'<path d="M{X_NANTAI + 1},{Y_DATONG - 34} L{X_NANTAI + 8},{Y_DATONG - 22} L{X_NANTAI + 15},{Y_DATONG - 34}" fill="none" stroke="{ONE}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
text(X_NANTAI + 22, 480, '單行道', 12.5, ONE, 700, 'start', halo=True)
text(X_NANTAI + 22, 497, '只能往南開', 11.5, ONE, 400, 'start', halo=True)

# 地標
poi(X_ZHONGSHAN - 52, Y_ZHONGZHENG + 50, '美麗島站 2 號出口', '#dc2626', 'M')
poi(X_NANTAI + 52, Y_ZHONGZHENG + 50, '三信銀行', '#6b7280', '$')
poi(424, 334, '加昕洗衣店', '#6b7280', '洗', dy=36, r=19, size=17)
poi(150, 336, '早安美之城', '#d97706', '早', dy=38, r=19, size=17)
poi(X_ZILI + 60, Y_ZHONGZHENG + 50, '中正自立停車場', '#1d4ed8', 'P')
poi(507, 384, '', '#6b7280', '廟', r=19, size=17)
poi(585, 364, '嘟嘟房停車場', '#1d4ed8', 'P', dy=34)

# 路線
ax, ay = X_1NONG + 56, Y_43 + 92
wx0 = X_ZHONGSHAN - 52
walk = (f'M{wx0},{Y_ZHONGZHENG + 36} L{wx0},{Y_ZHONGZHENG + 14} L{X_NANTAI - 7},{Y_ZHONGZHENG + 14} '
        f'L{X_NANTAI - 7},{Y_43 + 5} L{X_1NONG + 3},{Y_43 + 5} L{X_1NONG + 3},{ay + 10} L{ax - 18},{ay + 10}')
s.append(f'<path d="{walk}" fill="none" stroke="{ACC}" stroke-width="5" stroke-dasharray="9 7" stroke-linecap="round" stroke-linejoin="round"/>')
drive = f'M{W},{Y_ZHONGZHENG - 10} L{X_ZILI - 7},{Y_ZHONGZHENG - 10} L{X_ZILI - 7},{Y_43 - 5} L{X_1NONG - 10},{Y_43 - 5}'
s.append(f'<path d="{drive}" fill="none" stroke="{DRV}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" opacity="0.9"/>')
for (x, y, ang) in [(560, Y_ZHONGZHENG - 10, 180), (250, Y_ZHONGZHENG - 10, 180), (X_ZILI - 7, 250, 90), (170, Y_43 - 5, 0)]:
    s.append(f'<path d="M-6,-6 L4,0 L-6,6" transform="translate({x} {y}) rotate({ang})" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
text(W - 8, Y_ZHONGZHENG - 28, '← 從中正交流道', 12.5, DRV, 700, 'end', halo=True)
text(X_1NONG - 14, Y_43 - 16, '弄口下行李', 12.5, DRV, 700, 'end', halo=True)

# 阿爾兔兔
s.append(f'<path d="M{ax},{ay + 26} C{ax - 22},{ay} {ax - 22},{ay - 26} {ax},{ay - 26} C{ax + 22},{ay - 26} {ax + 22},{ay} {ax},{ay + 26} Z" fill="{ACC}" stroke="#fff" stroke-width="3"/>')
s.append(f'<circle cx="{ax}" cy="{ay - 6}" r="8" fill="#fff"/>')
s.append(f'<rect x="{ax - 48}" y="{ay + 32}" width="96" height="26" rx="13" fill="#fff" stroke="{ACC}" stroke-width="2"/>')
text(ax, ay + 50, '阿爾兔兔', 14, ACC, 700)
text(W - 12, 24, '↑ 北', 13, TXT, 700, 'end')

# 圖例
ly = MAPH + 14
s.append(f'<line x1="24" y1="{ly + 14}" x2="64" y2="{ly + 14}" stroke="{ACC}" stroke-width="5" stroke-dasharray="9 7" stroke-linecap="round"/>')
text(74, ly + 19, '走路：美麗島站 2 號出口到民宿，約 4 分鐘', 13, anchor='start')
s.append(f'<line x1="24" y1="{ly + 40}" x2="64" y2="{ly + 40}" stroke="{DRV}" stroke-width="5" stroke-linecap="round"/>')
text(74, ly + 45, '開車：開到 43 巷 1 弄弄口下行李，再去停車場', 13, anchor='start')
s.append(f'<line x1="24" y1="{ly + 66}" x2="64" y2="{ly + 66}" stroke="{ONE}" stroke-width="4" stroke-linecap="round"/>')
text(74, ly + 71, '單行道：南台路只能往南開', 13, anchor='start')
text(W - 14, ly + 71, '示意圖，非實際比例', 11.5, '#8a7d72', anchor='end')
s.append('</svg>')

out = Path(__file__).resolve().parent.parent / 'src' / 'assets' / 'diagrams' / 'area-map.svg'
out.write_text('\n'.join(s), encoding='utf-8')
print(out)
