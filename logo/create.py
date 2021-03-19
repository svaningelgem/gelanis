"""Creates an SVG of the Databench logo. Optionally also a png."""

import os
from pathlib import Path
import random

import svgwrite

# NEED TO HAVE imagemagick installed (this works on version 7.0.8 from https://imagemagick.org/)

# https://digitalsynopsis.com/design/beautiful-color-palettes-combinations-schemes/
# Color picker: http://paletton.com/
COLORS = [
    ('#42359C', '#42359C', '#42359C', '#42359C', '#FAE5A5'),  # 0. Default pysparkling colors
    ('#fe4a49', '#2ab7ca', '#fed766', '#e6e6ea', '#f4f4f8'),  # 1. Beach Towels
    ('#eee3e7', '#ead5dc', '#eec9d2', '#f4b6c2', '#f6abb6'),  # 2. Light Pink
    ('#011f4b', '#03396c', '#005b96', '#6497b1', '#b3cde0'),  # 3. Beautiful Blues
    ('#051e3e', '#251e3e', '#451e3e', '#651e3e', '#851e3e'),  # 4. So Many Lost Songs
    ('#dec3c3', '#e7d3d3', '#f0e4e4', '#f9f4f4', '#ffffff'),  # 5. She
    ('#4a4e4d', '#0e9aa7', '#3da4ab', '#f6cd61', '#fe8a71'),  # 6. Moonlight Bytes 6
    ('#2a4d69', '#4b86b4', '#adcbe3', '#e7eff6', '#63ace5'),  # 7. Number 3
    ('#fe9c8f', '#feb2a8', '#fec8c1', '#fad9c1', '#f9caa7'),  # 8. Pastellea
    ('#009688', '#35a79c', '#54b2a9', '#65c3ba', '#83d0c9'),  # 9. Android Lollipop
    ('#ee4035', '#f37736', '#fdf498', '#7bc043', '#0392cf'),  # 10. Rainbow Dash
    ('#faf0e6', '#fff5ee', '#fdf5e6', '#faf0e6', '#faebd7'),  # 11. Shades of White
    ('#ffffff', '#d0e1f9', '#4d648d', '#283655', '#1e1f26'),  # 12. Blueberry Basket
    ('#eeeeee', '#dddddd', '#cccccc', '#bbbbbb', '#aaaaaa'),  # 13. Five Shades of Grey
    ('#ffe9dc', '#fce9db', '#e0a899', '#dfa290', '#c99789'),  # 14. Anime Skin Tones
    ('#96ceb4', '#ffeead', '#ff6f69', '#ffcc5c', '#88d8b0'),  # 15. Beach
    ('#6e7f80', '#536872', '#708090', '#536878', '#36454f'),  # 16. Blue Grey
    ('#4b3832', '#854442', '#fff4e6', '#3c2f2f', '#be9b7b'),  # 17. Cappuccino
    ('#3b5998', '#8b9dc3', '#dfe3ee', '#f7f7f7', '#ffffff'),  # 18. Facebook
    ('#008744', '#0057e7', '#d62d20', '#ffa700', '#ffffff'),  # 19. Google Colors
    ('#008744', '#0057e7', '#d62d20', '#ffa700', '#000000'),  # 19. Google Colors -- heavy stroke
    ('#3385c6', '#4279a3', '#476c8a', '#49657b', '#7f8e9e'),  # 20. Gray Blue
    ('#d2d4dc', '#afafaf', '#f8f8fa', '#e5e6eb', '#c0c2ce'),  # 21. Grey Lavender Colors
    ('#a8e6cf', '#dcedc1', '#ffd3b6', '#ffaaa5', '#ff8b94'),  # 22. Pastel Rainbow
    ('#d11141', '#00b159', '#00aedb', '#f37735', '#ffc425'),  # 23. Metro UI Colors
    ('#6f7c85', '#75838d', '#7e8d98', '#8595a1', '#8c9da9'),  # 24. Greyso
    ('#ebf4f6', '#bdeaee', '#76b4bd', '#58668b', '#5e5656'),  # 25. The Water Bearer
    ('#ff77aa', '#ff99cc', '#ffbbee', '#ff5588', '#ff3377'),  # 26. Pinks
    ('#eeeeee', '#dddddd', '#cccccc', '#bbbbbb', '#29a8ab'),  # 27. Never Doubt
    ('#fff6e9', '#ffefd7', '#fffef9', '#e3f0ff', '#d2e7ff'),  # 28. Never Dreamed Of This
    ('#edc951', '#eb6841', '#cc2a36', '#4f372d', '#00a0b0'),  # 29. Program Catalog
    ('#84c1ff', '#add6ff', '#d6eaff', '#eaf4ff', '#f8fbff'),  # 30. Office Room 2
    ('#2e003e', '#3d2352', '#3d1e6d', '#8874a3', '#e4dcf1'),  # 31. Purple Skyline
    ('#8d5524', '#c68642', '#e0ac69', '#f1c27d', '#ffdbac'),  # 32. Skin Tones
    ('#343d46', '#4f5b66', '#65737e', '#a7adba', '#c0c5ce'),  # 33. Space Gray
    ('#bfd6f6', '#8dbdff', '#64a1f4', '#4a91f2', '#3b7dd8'),  # 34. The Armor Falls
    ('#fdfbfb', '#fbfdfb', '#fdfdff', '#fdf9f9', '#fdfbfb'),  # 35. White
    ('#e3c9c9', '#f4e7e7', '#eedbdb', '#cecbcb', '#cbdadb'),  # 36. Wrist Skin
]

DATA = [
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
]

USE_COLOR = COLORS[9]
ROTATION = 0
if ROTATION:
    USE_COLOR = USE_COLOR[ROTATION:] + USE_COLOR[:ROTATION]


def stroke_color():
    return '#000000'
    return USE_COLOR[4]


def color(x, y):
    """triangles."""
    return random.choice(USE_COLOR)

    if (x - 4) > (y - 4) and -(y - 4) <= (x - 4):
        # right
        return USE_COLOR[0]

    if (x - 4) > (y - 4) and -(y - 4) > (x - 4):
        # top
        return USE_COLOR[1]

    if (x - 4) <= (y - 4) and -(y - 4) <= (x - 4):
        # bottom
        return USE_COLOR[2]

    if (x - 4) <= (y - 4) and -(y - 4) > (x - 4):
        # left
        return USE_COLOR[3]

    # should not happen
    return 'black'


def simple(svg_document, x, y, v):
    if v == 1:
        svg_document.add(
            svg_document.rect(
                insert=(x * 16, y * 16),
                size=('16px', '16px'),
                # rx="2px",
                # stroke_width="1",
                # stroke=color(x, y),
                fill=color(x, y),
            )
        )


def smaller(svg_document, x, y, v, x_offset=0, y_offset=0):
    # from center
    distance2 = (x - 3.5) ** 2 + (y - 3.5) ** 2
    max_distance2 = 2 * 3.5 ** 2

    if v == 1:
        size = 16.0 * (1.0 - distance2 / max_distance2)
        if size == 0: size = 1
        number_of_cubes = int(16 ** 2 / (size ** 2))
        for i in range(number_of_cubes):
            xi = x * 16 + 1 + random.random() * (14.0 - size) + x_offset
            yi = y * 16 + 1 + random.random() * (14.0 - size) + y_offset
            sizepx = str(size) + 'px'
            svg_document.add(
                svg_document.rect(
                    insert=(xi, yi),
                    size=(sizepx, sizepx),
                    rx='2px',
                    stroke_width='1',
                    stroke=stroke_color(),
                    fill=color(x, y),
                )
            )


def generate_png(name, width, height):
    p1 = Path(f'{name}.svg')
    p2 = Path(f'{name}-w{width}.png')
    if p2.exists():
        p2.unlink()

    os.system(f'magick -background none {p1} -density 1200 -resize {width}x{height} {p2}')


def test_logos():
    global USE_COLOR
    for idx, _ in enumerate(COLORS):
        USE_COLOR = COLORS[idx]

        for rotation in range(len(USE_COLOR)):
            name = f'logo_{idx:02}_{rotation}'
            svg_document = svgwrite.Drawing(filename=f'{name}.svg', size=('128px', '128px'))

            for y, r in enumerate(DATA):
                for x, v in enumerate(r):
                    smaller(svg_document, x, y, v)

            svg_document.save()
            generate_png(name, 600, 600)

            USE_COLOR = USE_COLOR[1:] + USE_COLOR[:1]


def main():
    svg_favicon = svgwrite.Drawing(filename='favicon.svg', size=('128px', '128px'))
    svg_document = svgwrite.Drawing(filename='logo.svg', size=('128px', '128px'))
    svg_banner_white = svgwrite.Drawing(filename='banner_white.svg', size=('600px', '200px'))
    svg_banner_black = svgwrite.Drawing(filename='banner_black.svg', size=('600px', '200px'))

    for y, r in enumerate(DATA):
        for x, v in enumerate(r):
            simple(svg_favicon, x, y, v)
            smaller(svg_document, x, y, v)
            smaller(svg_banner_white, x, y, v, x_offset=20, y_offset=40)
            smaller(svg_banner_black, x, y, v, x_offset=20, y_offset=40)

    # add banner text
    g = svg_banner_white.g(style='font-size:40px; font-family:Arial; font-weight: bold; font-style: italic;')
    g.add(svg_banner_white.text('gelanis', insert=(180, 120), fill='#000000'),)
    svg_banner_white.add(g)

    g = svg_banner_black.g(style='font-size:40px; font-family:Arial; font-weight: bold; font-style: italic;')
    g.add(svg_banner_black.text('gelanis', insert=(180, 120), fill='#35a79c', stroke=stroke_color()),)
    svg_banner_black.add(g)

    # print(svg_document.tostring())
    svg_favicon.save()
    svg_document.save()
    svg_banner_white.save()
    svg_banner_black.save()

    # create pngs
    generate_png('logo', 100, 100)
    generate_png('logo', 600, 600)
    generate_png('banner_white', 500, 100)
    generate_png('banner_white', 500, 100)
    generate_png('banner_black', 1500, 400)
    generate_png('banner_black', 1500, 400)

    # generate favicons
    favicon_sizes = [16, 32, 48, 128, 256]
    for s in favicon_sizes:
        generate_png('favicon', s, s)

    png_favicon_names = [f'favicon-w{s}.png' for s in favicon_sizes]
    os.system('magick ' + (' '.join(png_favicon_names)) + ' -colors 256 favicon.ico')


if __name__ == '__main__':
    random.seed(42)
    # test_logos()
    main()
