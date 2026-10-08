"""畫美麗島站到各演唱會場館的捷運示意圖（直式，給手機看），輸出 src/assets/diagrams/美麗島站到各場館-捷運示意圖-阿爾兔兔.svg。
站數、時間來自高雄捷運官網「站間行駛時間」（2026-03-02 版，2026-10-07 查證），出口來自各場館官網。
改站數或時間時改下面的文字，再重跑：python scripts/draw_concert_mrt_map.py"""
from pathlib import Path

W, H = 420, 900
BG, TXT, MUTED, ACC = '#fdfaf6', '#2b2420', '#7a6f66', '#b5651d'
RED, ORANGE, GREEN = '#d71f3b', '#f39800', '#6fae3a'
FONT = "font-family=\"'Noto Sans TC','Microsoft JhengHei','PingFang TC',sans-serif\""

MX, MY = 150, 520           # 美麗島站
HX, LX, LY = 40, 380, 700   # 哈瑪星 x、衛武營 x、真愛碼頭 y

s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" {FONT}>',
     f'<rect width="{W}" height="{H}" fill="{BG}"/>']


def text(x, y, t, size=16, color=TXT, weight=400, anchor='start'):
    s.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" '
             f'text-anchor="{anchor}" stroke="{BG}" stroke-width="4" paint-order="stroke">{t}</text>')


def line(x1, y1, x2, y2, color, width=10):
    s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>')


def station(x, y, color, r=10):
    s.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{color}" stroke-width="5"/>')


# 標題
text(W / 2, 40, '從美麗島站搭捷運', 22, weight=700, anchor='middle')
text(W / 2, 70, '到高雄各演唱會場館', 22, weight=700, anchor='middle')

# 路線
line(MX, MY, MX, 130, RED)
line(HX, MY, LX, MY, ORANGE)
line(HX, MY, HX, LY, GREEN)

# 世運：最多客人去的場館，加底色框
s.append(f'<rect x="{MX + 16}" y="104" width="240" height="56" rx="10" fill="#fdecef" stroke="{RED}" stroke-width="1.5"/>')

# 紅線各站（往北）
for y, name, sub in [
    (130, '世運站 → 世運主場館', '7 站・約 15 分・1 號出口'),
    (220, '左營站（高鐵左營站）', '6 站・約 13 分'),
    (310, '巨蛋站 → 高雄巨蛋', '4 站・約 8 分・5 號出口'),
    (400, '高雄車站', '1 站・約 2 分'),
]:
    station(MX, y, RED)
    text(MX + 24, y - 2, name, 18, weight=700)
    text(MX + 24, y + 20, sub, 15, MUTED)

# 橘線往東：衛武營
station(LX, MY, ORANGE)
text(LX + 12, MY - 42, '衛武營站 → 衛武營', 18, weight=700, anchor='end')
text(LX + 12, MY - 20, '5 站・約 9 分・6 號出口', 15, MUTED, anchor='end')

# 橘線往西：哈瑪星，轉輕軌到真愛碼頭
station(HX, MY, ORANGE)
s.append(f'<circle cx="{HX}" cy="{MY}" r="5" fill="{GREEN}"/>')
text(HX - 12, MY - 42, '哈瑪星站', 18, weight=700)
text(HX - 12, MY - 20, '3 站・約 6 分', 15, MUTED)
text(HX + 20, MY + 130, '轉輕軌，', 15, GREEN, 700)
text(HX + 20, MY + 150, '再 3 站', 15, GREEN, 700)
station(HX, LY, GREEN)
text(HX + 24, LY - 2, '真愛碼頭站（輕軌）', 18, weight=700)
text(HX + 24, LY + 20, '→ 高雄流行音樂中心', 15, MUTED)

# 美麗島站（交會站）與民宿
s.append(f'<circle cx="{MX}" cy="{MY}" r="18" fill="#fff" stroke="{TXT}" stroke-width="5"/>')
s.append(f'<circle cx="{MX}" cy="{MY}" r="7" fill="{ACC}"/>')
text(MX + 26, MY + 44, '美麗島站', 18, weight=700)
text(MX + 26, MY + 66, '紅線、橘線交會站', 15, MUTED)
text(MX + 26, MY + 94, '阿爾兔兔：2 號出口', 16, ACC, 700)
text(MX + 26, MY + 116, '走路 4 分鐘', 16, ACC, 700)

# 圖例
y = 770
for i, (color, label) in enumerate([(RED, '紅線'), (ORANGE, '橘線'), (GREEN, '輕軌')]):
    x = 40 + i * 120
    line(x, y, x + 36, y, color, 8)
    text(x + 46, y + 6, label, 15, weight=700)

# 註記
for i, t in enumerate(['示意圖，非實際比例。',
                       '時間是列車行駛時間，不含等車、轉乘、走路。',
                       '資料來源：高雄捷運官網、各場館官網',
                       '（2026 年 10 月查證）']):
    text(W / 2, 812 + i * 20, t, 13.5, MUTED, anchor='middle')

s.append('</svg>')
out = Path(__file__).resolve().parent.parent / 'src' / 'assets' / 'diagrams' / '美麗島站到各場館-捷運示意圖-阿爾兔兔.svg'
out.write_text('\n'.join(s), encoding='utf-8')
print(out)
