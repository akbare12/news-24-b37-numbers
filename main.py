import os
from PIL import Image, ImageDraw, ImageFont
W, H = 1024, 1024
OUT = os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR', 'out'), 'entry.png')
CREAM, INK, RED, NAVY, GREEN, BLUE, GREY, ORANGE, GOLD = (247, 242, 231), (20, 20, 20), (178, 34, 34), (30, 58, 95), (34, 120, 60), (40, 90, 160), (110, 110, 110), (200, 100, 20), (180, 140, 20)
def F(p, s):
    try: return ImageFont.truetype(p, s)
    except Exception: return ImageFont.load_default()
SERIF = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'; SANS = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; SANSB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def wrap(d, t, f, w):
    ws, ln, cur = t.split(), [], ''
    for x in ws:
        s = (cur + ' ' + x).strip()
        if d.textlength(s, font=f) <= w: cur = s
        else: ln.append(cur); cur = x
    if cur: ln.append(cur)
    return ln
def txt(d, x, y, t, f, c=INK):
    d.text((x, y), t, font=f, fill=c); return y + f.size + 2
def chip(d, x, y, label, col):
    f = F(SANSB, 7); w = int(d.textlength(label, font=f)) + 8
    d.rounded_rectangle([x, y, x + w, y + 12], 3, fill=col); d.text((x + 4, y + 2), label, font=f, fill=(255, 255, 255)); return x + w + 4
def scene(d, x, y, w, h, kind):
    d.rectangle([x, y, x + w, y + h], fill=(210, 225, 240) if kind != 'court' else (225, 220, 205))
    if kind == 'tower':
        d.rectangle([x, y + h, x + w, y + h], fill=(40, 40, 60)); d.polygon([(x + w * .45, y + 8), (x + w * .55, y + 8), (x + w * .52, y + h * .8), (x + w * .48, y + h * .8)], fill=(60, 60, 90))
        for i in range(5): d.rectangle([x + w * .46, y + 15 + i * 12, x + w * .54, y + 23 + i * 12], fill=(255, 220, 120))
        d.ellipse([x + w * .68, y + 12, x + w * .78, y + 22], fill=(255, 140, 40)); d.ellipse([x + w * .60, y + 20, x + w * .86, y + 46], fill=(200, 200, 200)); d.rectangle([x, y + h - 14, x + w, y + h], fill=(30, 30, 45))
        for i in range(6): d.rectangle([x + 6 + i * 16, y + h - 26, x + 14 + i * 16, y + h - 14], fill=(50, 50, 70))
    elif kind == 'gate':
        d.rectangle([x, y + h * .55, x + w, y + h], fill=(150, 40, 40)); d.rectangle([x + w * .38, y + h * .25, x + w * .62, y + h * .75], fill=(180, 60, 50)); d.rectangle([x + w * .44, y + h * .4, x + w * .56, y + h * .75], fill=(90, 20, 20))
        d.rectangle([x + 8, y + 10, x + w - 8, y + 22], fill=(255, 255, 255)); d.rectangle([x + w * .2, y + h * .3, x + w * .3, y + h * .5], fill=(255, 255, 255)); d.rectangle([x + w * .7, y + h * .3, x + w * .8, y + h * .5], fill=(255, 255, 255))
    elif kind == 'court':
        d.rectangle([x, y + h * .6, x + w, y + h], fill=(120, 110, 95)); d.polygon([(x + 10, y + h * .6), (x + w / 2, y + 12), (x + w - 10, y + h * .6)], fill=(200, 180, 150))
        for i in range(4): d.rectangle([x + 18 + i * 22, y + h * .62, x + 26 + i * 22, y + h - 8], fill=(240, 235, 220))
        d.rectangle([x + w * .62, y + h * .45, x + w * .95, y + h * .6], fill=(255, 255, 255)); d.text((x + w * .64, y + h * .47), '10/12', font=F(SANSB, 11), fill=RED)
    else:
        d.rectangle([x, y + h * .7, x + w, y + h], fill=(90, 140, 90)); d.ellipse([x + w * .3, y + 6, x + w * .7, y + h * .55], fill=(255, 200, 80)); d.rectangle([x + w * .1, y + h * .5, x + w * .9, y + h * .62], fill=(60, 90, 140))
        d.polygon([(x + w * .15, y + h * .5), (x + w * .3, y + h * .3), (x + w * .45, y + h * .5)], fill=(40, 60, 100)); d.polygon([(x + w * .55, y + h * .5), (x + w * .7, y + h * .28), (x + w * .85, y + h * .5)], fill=(40, 60, 100))
CONT = {'NA': [(-168, 66), (-140, 70), (-120, 71), (-95, 80), (-80, 73), (-60, 60), (-55, 47), (-70, 42), (-75, 35), (-80, 26), (-90, 21), (-97, 16), (-105, 20), (-115, 28), (-125, 40), (-125, 49), (-145, 60)], 'SA': [(-80, 10), (-72, 12), (-60, 8), (-50, 0), (-35, -8), (-40, -22), (-48, -28), (-58, -38), (-65, -45), (-70, -52), (-73, -40), (-72, -20), (-80, -5)], 'AF': [(-17, 15), (-10, 31), (0, 36), (10, 37), (20, 32), (32, 31), (35, 28), (43, 12), (51, 11), (48, 0), (40, -10), (35, -20), (28, -33), (20, -35), (15, -27), (12, -18), (9, -1), (-8, 4)], 'EU': [(-10, 36), (0, 39), (5, 44), (-2, 48), (0, 50), (5, 53), (8, 57), (10, 59), (18, 56), (21, 55), (28, 59), (30, 60), (30, 66), (40, 68), (55, 69), (70, 72), (90, 75), (110, 76), (130, 72), (160, 70), (178, 66), (170, 60), (160, 55), (158, 50), (142, 45), (140, 40), (135, 35), (127, 35), (122, 30), (120, 25), (108, 18), (105, 9), (100, 8), (97, 15), (92, 21), (88, 22), (80, 15), (77, 8), (73, 20), (66, 25), (60, 25), (57, 26), (52, 28), (48, 30), (43, 38), (36, 36), (30, 36), (27, 37), (22, 37), (18, 40), (12, 44), (8, 44), (3, 42), (0, 38), (-2, 37), (-9, 37), (-9, 43)], 'AU': [(113, -22), (114, -30), (115, -35), (124, -33), (129, -32), (137, -35), (140, -38), (147, -39), (150, -37), (153, -27), (146, -19), (142, -11), (136, -12), (132, -11), (126, -14), (122, -17), (118, -20)], 'GL': [(-45, 60), (-30, 68), (-20, 70), (-25, 76), (-40, 80), (-55, 76), (-58, 70)]}
HERO = [(1, 'RIYADH', 'MIDDLE EAST', 'CONFIRMED', GREEN, 'tower', "Houthi drone hits Riyadh's tallest tower again, 11 hurt", 'A Houthi drone hits the PIF tower, the tallest in Riyadh, for the second time in a week, injuring 11 people, including two Saudis, two Indians, three Nepalese and four Egyptians.', 'Saudi officials'), (2, 'SHANGHAI', 'ASIA', 'OFFICIAL', BLUE, 'gate', 'China probes Shanghai party chief Chen Jining', 'Chen Jining, 62, is probed for serious violations, the fourth Politburo member to fall in a party investigation this year.', 'CCDI'), (3, 'NEW YORK', 'US / TECH', 'CONFIRMED', GREEN, 'court', 'Huawei guilty on 10 of 12 counts', 'A US federal jury finds Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud, but clears it of racketeering.', 'US court')]
CARDS = [(4, 'ZAPORIZHZHIA', 'EUROPE / WAR', 'REPORTED', GREY, 'Russian attacks kill 9 across Ukraine in a day', 'Nine killed and 81 wounded as 96 drones are launched and 73 are shot down or jammed over Kyiv.', 'Ukraine officials'), (5, 'DAKAR', 'AFRICA / SPORT', 'OFFICIAL', BLUE, 'CAS hands Senegal back the AFCON title', 'Morocco forfeit 3-0, so Senegal win 1-0 and take the Africa Cup of Nations title back.', 'CAS'), (6, 'HORMUZ', 'MIDDLE EAST', 'REPORTED', GREY, 'IRGC attacks container ship in Hormuz', 'Navigation is cut at 18:58 UTC and a no-go area is set north of Khasab in Oman.', 'UKMTO'), (7, 'NEW YORK', 'WORLD / MARKETS', 'CONFIRMED', GREEN, 'Dow closes above 50,000 for the first time', 'The Dow closes at 50,018 while the Nasdaq falls 1.5% and the Taiex jumps a record 8.99%.', 'Market close'), (8, 'REDMOND', 'WORLD / TECH', 'REPORTED', GREY, "Microsoft declares 'Code Red' after historic outage", 'After a 24-hour outage, Microsoft targets global recovery in one hour with five workstreams.', 'Reuters'), (9, 'ESKISEHIR', 'EUROPE', 'REPORTED', GREY, 'Turkish military helicopter crash kills 5', 'An AS-532 helicopter comes down in Eskisehir at 19:52 UTC, killing all five on board.', 'Turkish officials'), (10, 'CARTAGENA', 'AMERICAS', 'REPORTED', GREY, 'Supermarket hostages: 25 held in Cartagena', 'Twenty-five people are held, five elderly women are freed, and airport landings pause for 45 minutes.', 'Colombia officials'), (11, 'ADEN', 'MIDDLE EAST', 'REPORTED', GREY, 'Houthis advance within 60 km of Aden', 'Houthi forces advance to within 60 km of Aden in Yemen at 16:51 UTC.', 'Wires'), (12, 'LAHJ', 'MIDDLE EAST', 'REPORTED', GREY, 'Saudi strikes kill 25, wound 6 in Yemen', 'Strikes on a bus and truck in Wadi Maabaq, Lahj, leave 25 dead or missing and six wounded.', 'Yemen officials'), (13, 'JIUQUAN', 'WORLD / SPACE', 'OFFICIAL', BLUE, 'China names first foreign astronaut for Tiangong', 'Tang Hongbo, Wu Yi and Muhammad Zeeshan Ali of Pakistan are named for Shenzhou-24.', 'CMSA')]
ALSO = [(14, 'Ankara', 'Haftar visits Turkey for the first time.', 'REPORTED', GREY), (15, 'London', 'UK sanctions Houthis and four officials.', 'OFFICIAL', BLUE), (16, 'Villavicencio', 'Car bomb injures 23 people.', 'REPORTED', GREY), (17, 'Gaza', 'Israel kills Hamas internal security chief.', 'REPORTED', GREY), (18, 'Baghdad', 'Iraq orders federal control of Kurdish oilfields.', 'OFFICIAL', BLUE), (19, 'Gaza', 'Meningitis epidemic alert, 272 cases in October.', 'OFFICIAL', BLUE), (20, 'DR Congo', 'Missing Cessna 208, rebels claim shootdown.', 'CLAIM', ORANGE), (21, 'Hanoi', 'Hot-pot explosion kills at least six.', 'REPORTED', GREY), (22, 'Gulf of Finland', 'Ukraine hits Russian ship Sparta II.', 'REPORTED', GREY), (23, 'Kuala Lumpur', 'Malaysia to return thousands of migrants.', 'OFFICIAL', BLUE), (24, 'Ulleungdo', 'S. Korea shelter order as Russian jets enter ADIZ.', 'OFFICIAL', BLUE), (25, 'Dhaka', 'Hasina plans return on 16 December.', 'REPORTED', GREY), (26, 'The Hague', '14 nations endorse ICJ Myanmar ruling.', 'REPORTED', GREY), (27, 'Jakarta', 'Indonesia nominates two VP candidates.', 'OFFICIAL', BLUE), (28, 'Beijing', 'China sentences official Ma to death for spying.', 'OFFICIAL', BLUE), (29, 'Brussels', 'NATO vows defence against space threat.', 'OFFICIAL', BLUE), (30, 'Mexico City', 'US drone aided weekend capture; Mexico to try him after his Fri 20 Nov arrest.', 'REPORTED', GREY), (31, 'San Salvador', 'Bukele names three soldiers killed in Haiti.', 'OFFICIAL', BLUE), (32, 'Ottawa', 'Pentagon rebukes Canada; only 41.9% of air fleet ready.', 'REPORTED', GREY), (33, 'Washington', 'US adds Megaspeed to trade blacklist.', 'OFFICIAL', BLUE), (34, 'Kyiv', 'Zelensky urges Ukraine, Russia, US and Europe talks soon.', 'REPORTED', GREY), (35, 'Ras Al Khaimah', 'UAE bus-truck crash kills 13.', 'REPORTED', GREY), (36, 'London', 'England record 5,258 heat deaths in summer 2026.', 'OFFICIAL', BLUE), (37, 'Kourou', 'Ariane 6 lofts 36 Amazon satellites.', 'OFFICIAL', BLUE), (38, 'Cikande', 'Factory-fire toll rises to 26.', 'REPORTED', GREY)]
UTC = [('02:15', 'NATO vows space defence'), ('08:16', 'Hanoi blast'), ('10:42', 'Saudi strikes Yemen'), ('14:27', 'Riyadh tower hit'), ('16:51', 'Houthis 60 km from Aden'), ('18:58', 'Hormuz ship attack'), ('20:41', 'Huawei guilty')]
NUMS = [('11', 'hurt in Riyadh'), ('9', 'killed in Ukraine'), ('50,018', 'Dow close'), ('+8.99%', 'Taiex record'), ('25', 'killed or missing, Yemen'), ('26', 'Cikande toll'), ('10/12', 'Huawei guilty'), ('96', 'drones launched')]
PINS = [(1, 'Riyadh', 24.71, 46.68, 0, 0), (2, 'Shanghai', 31.23, 121.47, 0, 0), (3, 'New York', 40.71, -74.01, 0, -14), (4, 'Zaporizhzhia', 47.83, 35.14, 0, 0), (5, 'Dakar', 14.69, -17.44, 0, 0), (6, 'Hormuz', 26.50, 56.25, 0, 0), (7, 'New York', 40.71, -74.01, 14, 10), (8, 'Redmond', 47.67, -122.12, 0, 0), (9, 'Eskisehir', 39.78, 30.52, 0, -13), (10, 'Cartagena', 10.39, -75.51, 0, 12), (11, 'Aden', 12.79, 45.03, 0, 0), (12, 'Lahj', 13.05, 44.88, -16, 12), (13, 'Jiuquan', 39.74, 98.49, 0, 0)]
REGIONS = [('Europe', 9, (178, 34, 34)), ('Middle East', 8, (200, 100, 20)), ('Asia', 8, (40, 90, 160)), ('Africa', 2, (34, 120, 60)), ('Americas', 7, (120, 60, 140)), ('World/Space', 4, (90, 90, 90))]
img = Image.new('RGB', (W, H), CREAM)
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 20], fill=RED)
d.text((10, 4), 'THE WORLD ON ONE DAY', font=F(SANSB, 11), fill=(255, 255, 255))
hdr = '38 STORIES \u00b7 6 REGIONS \u00b7 13 FIELDS'
d.text((W - 10 - d.textlength(hdr, font=F(SANSB, 11)), 4), hdr, font=F(SANSB, 11), fill=(255, 255, 255))
d.text((10, 26), 'Tuesday 24 November 2026', font=F(SERIF, 34), fill=INK)
d.text((10, 64), 'Riyadh tower hit again  \u00b7  Chen Jining probed  \u00b7  Huawei guilty on 10 of 12 counts', font=F(SERIF, 14), fill=RED)
x = 10
for nm, n, c in REGIONS:
    lab = f'{nm} {n}'; w = int(d.textlength(lab, font=F(SANSB, 10))) + 16; d.rounded_rectangle([x, 84, x + w, 102], 4, fill=c); d.text((x + 8, 87), lab, font=F(SANSB, 10), fill=(255, 255, 255)); x += w + 6
d.text((10, 108), 'THE DAY IN UTC', font=F(SANSB, 10), fill=RED)
for i, (t, e) in enumerate(UTC):
    xx = 10 + i * 145; d.text((xx, 122), t, font=F(SANSB, 11), fill=RED); d.text((xx, 136), e, font=F(SANS, 8), fill=INK)
d.line([10, 154, W - 10, 154], fill=INK, width=1); d.text((10, 160), 'THE DAY IN NUMBERS', font=F(SANSB, 10), fill=RED)
for i, (v, lab) in enumerate(NUMS):
    xx = 10 + i * 127; d.text((xx, 174), v, font=F(SERIF, 20), fill=NAVY); d.text((xx, 196), lab, font=F(SANS, 8), fill=INK)
for i, (n, city, reg, ch, col, kind, head, deck, src) in enumerate(HERO):
    x = 10 + i * 338; w = 328; y = 214; d.rectangle([x, y, x + w, y + 178], outline=INK, width=1, fill=(255, 255, 255)); scene(d, x + 1, y + 1, w - 2, 82, kind); yy = y + 86
    d.text((x + 8, yy), f'{n}  {city} \u00b7 {reg}', font=F(SANSB, 10), fill=RED); yy += 14; xx = chip(d, x + 8, yy, ch, col); d.text((xx, yy + 1), f'({src})', font=F(SANS, 8), fill=GREY); yy += 15
    for ln in wrap(d, head, F(SANSB, 12), w - 16): yy = txt(d, x + 8, yy, ln, F(SANSB, 12))
    for ln in wrap(d, deck, F(SANS, 9), w - 16): yy = txt(d, x + 8, yy, ln, F(SANS, 9))
for i, (n, city, reg, ch, col, head, deck, src) in enumerate(CARDS):
    x = 10 + (i % 5) * 203; y = 396 + (i // 5) * 112; w = 195; d.rectangle([x, y, x + w, y + 110], outline=INK, width=1, fill=(255, 255, 255)); scene(d, x + 1, y + 1, w - 2, 26, 'mini'); yy = y + 29
    d.text((x + 6, yy), f'{n}  {city} \u00b7 {reg}', font=F(SANSB, 7), fill=RED); yy += 10; xx = chip(d, x + 6, yy, ch, col); d.text((xx, yy + 1), f'({src})', font=F(SANS, 7), fill=GREY); yy += 13
    for ln in wrap(d, head, F(SANSB, 9), w - 12)[:2]: yy = txt(d, x + 6, yy, ln, F(SANSB, 9))
    for ln in wrap(d, deck, F(SANS, 8), w - 12)[:3]: yy = txt(d, x + 6, yy, ln, F(SANS, 8))
MX, MY, MW, MH = 10, 624, 450, 225; d.rectangle([MX, MY, MX + MW, MY + MH], outline=INK, width=1, fill=(185, 220, 235)); d.text((MX + 6, MY + 4), 'WORLD MAP \u2014 PINS 1\u201313', font=F(SANSB, 9), fill=NAVY)
def proj(lat, lon):
    return MX + (lon + 180) / 360 * MW, MY + 30 + (75 - lat) / 135 * (MH - 36)
for pts in CONT.values():
    d.polygon([proj(la, lo) for lo, la in pts], fill=(185, 209, 168), outline=(90, 120, 80))
for n, city, la, lo, dx, dy in PINS:
    px, py = proj(la, lo); qx, qy = px + dx, py + dy
    if dx or dy: d.line([px, py, qx, qy], fill=RED, width=1)
    d.ellipse([qx - 8, qy - 8, qx + 8, qy + 8], fill=RED, outline=(255, 255, 255)); d.text((qx - 3, qy - 6), str(n), font=F(SANSB, 8), fill=(255, 255, 255))
lx = 468; d.text((lx, 624), 'MAP LEGEND \u2014 1\u201313', font=F(SANSB, 10), fill=RED)
for n, city, la, lo, dx, dy in PINS:
    yy = 640 + (n - 1) * 16; d.ellipse([lx, yy, lx + 11, yy + 11], fill=RED); d.text((lx + 3, yy + 1), str(n), font=F(SANSB, 7), fill=(255, 255, 255)); d.text((lx + 15, yy + 1), city, font=F(SANS, 8), fill=INK)
ax = 610; d.text((ax, 624), 'ALSO ON TUESDAY 24 NOVEMBER \u2014 25 MORE STORIES', font=F(SANSB, 10), fill=RED)
for i, (n, city, txt_, ch, col) in enumerate(ALSO):
    yy = 640 + i * 9
    if yy > 880: break
    d.text((ax, yy), f'{n}. {city}: {txt_}', font=F(SANS, 7), fill=INK); d.text((1014, yy), ch, font=F(SANSB, 6), fill=col, anchor='ra')
d.rectangle([10, 888, W - 10, 972], outline=RED, width=2, fill=(255, 240, 240)); yy = txt(d, 18, 894, 'DATE CHECK', F(SANSB, 11), RED)
for ln in wrap(d, 'Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC.', F(SANS, 9), W - 36): yy = txt(d, 18, yy, ln, F(SANS, 9))
for ln in wrap(d, 'LEFT OUT (not 24 Nov): Hormuz mine claims (Mon 23 Nov); Huang returns as Nvidia CEO (Mon 23 Nov); EU sanctions package 22 (Mon 23 Nov); COP31 ends with no deal (Sun 22 Nov); corvette Merkury sinks (Sat 22 Nov); El Chapo Isidro arrested (Fri 20 Nov); Cikande factory fire starts (Sat 21 Nov); Trump hush-money appeal verdict (Mon 23 Nov); ATP Finals (Sun 22 Nov); Las Vegas GP (Sat 21 Nov).', F(SANS, 9), W - 36): yy = txt(d, 18, yy, ln, F(SANS, 9))
for ln in wrap(d, 'NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC); MPR session picks VP (11 Dec); Huawei sentencing (Sep 2027); Hasina returns (16 Dec).', F(SANS, 9), W - 36): yy = txt(d, 18, yy, ln, F(SANS, 9))
d.text((10, 980), 'Sources: Daily Summary of World News, Astrova News, Horizon, WSOC/AP, Reuters, UKMTO, CAS, CMSA.  CONFIRMED = 2+ outlets  \u00b7  OFFICIAL = on record  \u00b7  REPORTED = one outlet  \u00b7  CLAIM = one side.', font=F(SANS, 8), fill=GREY)
d.text((10, 994), 'Scenes are drawn illustrations, not photographs.  Map: equirectangular, real lat/lon.', font=F(SANS, 8), fill=GREY)
os.makedirs(os.path.dirname(OUT) or '.', exist_ok=True)
img.save(OUT)
print(OUT)
