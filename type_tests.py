# -*- coding: utf-8 -*-
import random


words = ['Красный', 'Желтый', 'Синий', 'Зеленый', 'Фиолетовый']
colors = ['red', 'yellow', 'blue', 'green', 'purple']


def test_word(color='white'):
    rand_word = random.randint(0, 4)
    rand_color = random.randint(0, 4)
    while True:
        if rand_word != rand_color and colors[rand_color] != color:
            break
        rand_color = random.randint(0, 4)

    return(words[rand_word], colors[rand_color])


def next_test(name, color='white', word='white'):
    def pts(word):
        rand_word = random.randint(0, 4)
        if word == 'white':
            rand_color = random.randint(0, 4)
            while True:
                if rand_word != rand_color:
                    break
                rand_color = random.randint(0, 4)
            return(words[rand_word], colors[rand_color])
        else:
            ind = words.index(word)
            while True:
                if rand_word != ind:
                    break
                rand_word = random.randint(0, 4)
            return(words[rand_word], colors[ind])

    def dictator(color):
        rand_word = random.randint(0, 4)
        rand_color = random.randint(0, 4)
        while True:
            if rand_word != rand_color and colors[rand_color] != color:
                break
            rand_color = random.randint(0, 4)
        return(words[rand_word], colors[rand_color])

    def x(color):
        rand_color = random.randint(0, 4)
        str_w = ""
        while True:
            if colors[rand_color] != color:
                break
            rand_color = random.randint(0, 4)
        for i in range(1, random.randint(2, 8)):
            str_w = str_w + 'x'
        return(str_w, colors[rand_color])

    if name == 'pts':
        return(pts(word))
    if name == 'dictator':
        return(dictator(color))
    if name == 'x':
        return(x(color))
