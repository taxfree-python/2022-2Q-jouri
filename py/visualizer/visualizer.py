#https://imagingsolution.net/program/python/tkinter/canvas_drawing_lines_circles_shapes/
#https://www.daniweb.com/programming/software-development/code/216929/saving-a-tkinter-canvas-drawing-python
#https://www.pytry3g.com/entry/2018/02/09/124143#%E6%96%87%E5%AD%97%E3%82%92%E6%9B%B8%E3%81%8F%E3%83%BCcreate_text

import tkinter as tk

class Visualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1500x1000")

        self.canvas = tk.Canvas(self.root, bg = 'white')
        self.canvas.pack(fill = tk.BOTH, expand = True)

    def ensemble(self, s, set_name = 'S'):
        self.canvas.create_oval(100, 140, 1400, 900, width = 3)
        self.canvas.create_rectangle(750 - 70 * len(set_name), 80, 750 + 70 * len(set_name), 220, fill = 'white', outline = 'white')
        self.canvas.create_text(750, 150, text = set_name, font = ('Helvetica',140))

        step = 140
        start_position_x = 750 - step / 2 * (min(7, len(s)) - 1)
        start_position_y = 510 - (len(s) // 7 - 1) * 60
        size = 80
        cnt = 0
        hei = 0

        for i in s:
            if cnt % 7 == 0:
                hei += 1
                cnt = 0
            self.canvas.create_text(start_position_x + step * cnt, start_position_y + 100 * (hei - 1), text = i, font = ("Helvetica", size))
            cnt += 1

        self.root.mainloop()


    def mapping(self, f, dom_name = 'A', codom_name = 'B'):
        self.canvas.create_oval(100, 140, 650, 900, width = 3)
        self.canvas.create_oval(850, 140, 1400, 900, width = 3)
        self.canvas.create_rectangle(375 - 70 * len(dom_name), 80, 375 + 70 * len(dom_name), 220, fill = 'white', outline = 'white')
        self.canvas.create_rectangle(1125 - 70 * len(dom_name), 80, 1125 + 70 * len(dom_name), 220, fill = 'white', outline = 'white')
        self.canvas.create_text(375, 150, text = dom_name, font = ('Helvetica',140))
        self.canvas.create_text(1125, 150, text = codom_name, font = ('Helvetica',140))

        if 'empty' in f:
            empty = f['empty']
            s = set(f['empty'])
            f.pop('empty')
        else:
            s = set()

        for i in f.values():
            for j in i:
                s.add(j)
        dom_size = 800 / (len(list(f.keys())) + 1)
        codom_size = 800 / (len(s) + 1)

        dom_position = dict()
        codom_positon = dict()

        cnt = 1
        for i in f.keys():
            dom_position[i] = 160 + dom_size * cnt
            cnt += 1
        cnt = 1
        for i in s:
            codom_positon[i] = 160 + codom_size * cnt
            cnt += 1

        size = 60
        check = set()
        for i in dom_position.keys():
            self.canvas.create_text(375, dom_position[i], text = i, font = ("Helvetica", size))
            for j in f[i]:
                self.canvas.create_line(375 + len(str(i)) * size / 2, dom_position[i], 1125 - len(str(j)) * size / 2, codom_positon[j], 
                                arrow = tk.LAST, arrowshape = (20, 30, 10), width = 5, activefill = "Red")
                if j in check:
                    continue
                self.canvas.create_text(1125, codom_positon[j], text = j, font = ("Helvetica",size))
                check.add(j)

        for i in s - check:
            self.canvas.create_text(1125, codom_positon[i], text = i, font = ("Helvetica",size))
        self.root.mainloop()


    def chain_mapping(self, f, g, dom_name = 'A', dom_name_f = 'B', codom_name = 'C'):
        s = 404
        m = 72
        self.canvas.create_oval(m, 140, s + m, 900, width = 3)
        self.canvas.create_oval(s + 2 * m, 140, 2 * (s + m), 900, width = 3)
        self.canvas.create_oval(2 * s + 3 * m, 140, 3 * (s + m), 900, width = 3)
        self.canvas.create_rectangle(s / 2 + m - 70 * len(dom_name), 80, s / 2 + m + 70 * len(dom_name), 220, fill = 'white', outline = 'white')
        self.canvas.create_rectangle(3 / 2 * s + 2 * m - 70 * len(dom_name), 80, 3 / 2 * s + 2 * m + 70 * len(dom_name), 220, fill = 'white', outline = 'white')
        self.canvas.create_rectangle(5 / 2 * s + 3 * m - 70 * len(dom_name), 80, 5 / 2 * s + 3 * m + 70 * len(dom_name), 220, fill = 'white', outline = 'white')
        self.canvas.create_text(s / 2 + m, 150, text = dom_name, font = ('Helvetica',140))
        self.canvas.create_text(3 / 2 * s + 2 * m, 150, text = dom_name_f, font = ('Helvetica',140))
        self.canvas.create_text(5 / 2 * s + 3 * m, 150, text = codom_name, font = ('Helvetica',140))

        if 'empty' in f:
            codom_f = set(f['empty'])
            f.pop('empty')
        else:
            codom_f = set()
        if 'empty' in g:
            codom_g = set(g['empty'])
            g.pop('empty')
        else:
            codom_g = set()

        for i in f.values():
            for j in i:
                codom_f.add(j)

        for i in g.keys():
            codom_f.add(i)

        for i in g.values():
            for j in i:
                codom_g.add(j)

        dom_size = 800 / (len(list(f.keys())) + 1)
        codom_size_f = 800 / (len(codom_f) + 1)
        codom_size_g = 800 / (len(codom_g) + 1)

        dom_position = dict()
        codom_positon_f = dict()
        codom_positon_g = dict()

        cnt = 1
        for i in f.keys():
            dom_position[i] = 160 + dom_size * cnt
            cnt += 1
        cnt = 1
        for i in codom_f:
            codom_positon_f[i] = 160 + codom_size_f * cnt
            cnt += 1
        cnt = 1
        for i in codom_g:
            codom_positon_g[i] = 160 + codom_size_g * cnt
            cnt += 1

        size = 60
        check_f = set()
        for i in dom_position.keys():
            self.canvas.create_text(s / 2 + m, dom_position[i], text = i, font = ("Helvetica", size))
            for j in f[i]:
                self.canvas.create_line(s / 2 + m + len(str(i)) * size / 2, dom_position[i], 3 / 2 * s + 2 * m - len(str(i)) * size / 2, codom_positon_f[j],
                                arrow = tk.LAST, arrowshape = (20, 30, 10), width = 5, activefill = "Red")
                if j in check_f:
                    continue
                self.canvas.create_text(3 / 2 * s + 2 * m, codom_positon_f[j], text = j, font = ("Helvetica",size))
                check_f.add(j)

        for i in codom_f - check_f:
            self.canvas.create_text(3 / 2 * s + 2 * m, codom_positon_f[i], text = i, font = ("Helvetica",size))

        check_g = set()
        for i in codom_positon_f.keys():
            if i not in check_f:
                self.canvas.create_text(3 / 2 * s + 2 * m, codom_positon_f[i], text = i, font = ("Helvetica", size))
            if i not in g:
                continue
            for j in g[i]:
                self.canvas.create_line(3 / 2 * s + 2 * m + len(str(i)) * size / 2, codom_positon_f[i], 5 / 2 * s + 3 * m - len(str(i)) * size / 2, codom_positon_g[j],
                                arrow = tk.LAST, arrowshape = (20, 30, 10), width = 5, activefill = "Red")
                if j in check_g:
                    continue
                self.canvas.create_text(5 / 2 * s + 3 * m, codom_positon_g[j], text = j, font = ("Helvetica",size))
                check_g.add(j)

        for i in codom_g - check_g:
            self.canvas.create_text(5 / 2 * s + 3 * m, codom_positon_g[i], text = i, font = ("Helvetica",size))

        self.root.mainloop()


# f = {1:(1, 3), 2:(4, 2), 3:(9, 6), 4:(16, )}
# n_8 = {i for i in range(8)}

# v = Visualizer()
# v.mapping(f)
# v.ensemble(n_8)